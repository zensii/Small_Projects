import pandas as pd
import xlwings as xw
from time import sleep
import numpy as np
import os
import sys
import FreeSimpleGUI

# Determine the directory where the script or executable is located
if getattr(sys, 'frozen', False):
    # If the script is running as a bundled executable (via PyInstaller)
    script_dir = os.path.dirname(sys.executable)
else:
    # If the script is running as a .py file
    script_dir = os.path.dirname(os.path.abspath(__file__))


dataframes = {}
counter = 1

for filename in os.listdir(script_dir):
    file_path = os.path.join(script_dir, filename)

    if '(UPDATED)' in filename:
        print('An updated file is already present in the current directory!')
        print('Please, delete the UPDATED file and try again.')
        print("Press 'Enter' key to quit.")
        input()
        sys.exit()

    try:
        if not filename.endswith('.exe'):
            df_main = pd.read_excel(f'{file_path}', sheet_name='raw date per vendor')  # locate the main data_frame file
            print('Opening main file in Excel. Please wait...')
            main_file = xw.Book(file_path)  # start excel using xlwings
            sleep(20)  # waiting for Excel to open
    except ValueError:  # fill a dict with dataframes from the files in the folder
        print('Additional file located. Opening... ')
        key = f'df_to_add{counter}'
        dataframes[key] = pd.read_excel(file_path, sheet_name='Sheet1', converters={'GL': str, 'Vendor': str})  # when reading, define the data type per column
        counter += 1
    except FileNotFoundError:
        print(f'{filename} not found!')


if dataframes:
    pass

else:
    print('Files not found! Script terminating...')
    sys.exit()

pv_tables = []
file_year = None
file_period = None
print('Cleaning data...')
for key, df in dataframes.items():
    cols = ['Company Code', 'G/L Account', 'Vendor', 'Name 1']
    if 'GL' in df.columns:
        # dataframes[key] = this is also possible as rename() does not modify in place by default (I used inplace=True)
        df.rename(columns={'GL': 'G/L Account', 'Vendor Name': 'Name 1', 'Amount_Act': 'Amount in Loc.Crcy 2'},
                  inplace=True)

        # get year and period from the file that has it (its the one that has 'GL')
        if file_year is None:
            file_year = int(df['Year'][0])
            file_period = int(df['Period'][0])

    # replace empty values with '' - needed as otherwise in the pivot grand total is not correct as the rows with no data are ommited?!
    print('Creating pivot tables...')
    for col in cols:
        df[col] = df[col].replace(np.nan, '')
    # creating a list with the pivot tables of all files to be added in the folder
    pv_tables.append(pd.pivot_table(df, values=['Amount in Loc.Crcy 2', 'Amount in Local Currency'],
                                    index=['Company Code', 'G/L Account', 'Vendor', 'Name 1'],
                                    aggfunc='sum').reset_index())

# Create the combined pivot table

pivot = pd.concat(pv_tables, ignore_index=True)
pivot['Year'] = file_year
pivot['Period'] = file_period

print('Normalizing file formats...')
# Defining the columns to update the main file with
vendors = pivot['Vendor'].apply(
    lambda x: f"'{x}")  # adding ' in front of the numbers to be interpreted as text (needed for main excel file logic)
g_l = pivot['G/L Account'].apply(
    lambda x: f"'{x}")  # adding ' in front of the numbers to be interpreted as text (needed for main excel file logic)
name = pivot['Name 1']
amount = pivot['Amount in Local Currency']
year = pivot['Year']
period = pivot['Period']

# save the data to be added as list in order to paste it in the excel file in one shot
data = []
print('Preparing data package...')
for g, v, n, a, y, p in zip(g_l.values, vendors.values, name.values, amount.values, year.values, period.values):
    data.append([g, v, n, None, None, None, None, a, y, p])

# which sheet we will update in the main file
sheet = main_file.sheets['raw date per vendor']

start_row = len(df_main.iloc[:, 0]) + 2  # find the first empty row
print('Updating main file. Please wait...')
sheet.range(f'B{start_row}').value = data  # write data to excel file
sleep(10)  # wait for the excel to update formulas
print('Saving...')
main_file.save(f'(UPDATED){main_file.name}')  # save the excel file
print('All DONE!')
print('Quitting...')
input()
app = xw.apps.active  # To quit Excel if needed
app.quit()
