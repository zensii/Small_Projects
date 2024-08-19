import pandas as pd
import xlwings as xw
from time import sleep
import numpy as np
import os
import sys
#import FreeSimpleGUI


def get_filepath():

    # Determine the directory where the script or executable is located
    if getattr(sys, 'frozen', False):
        # If the script is running as a bundled executable (via PyInstaller)
        script_dir = os.path.dirname(sys.executable)
    else:
        # If the script is running as a .py file
        script_dir = os.path.dirname(os.path.abspath(__file__))

    return script_dir


def check_for_updated(filename):

    if '(UPDATED)' in filename:
        print('An updated file is already present in the current directory!')
        print('Please, delete the UPDATED file and try again.')
        print("Press 'Enter' key to quit.")
        input()
        sys.exit()


def check_for_df(dataframes):
    if dataframes:
        pass
    else:
        print('Files not found! Script terminating...')
        sys.exit()


def get_df(script_dir):
    """Function to scan the active dir and extract the needed dataframes for each of the Excel files"""
    dataframes = {}
    df_main = None
    main_file = None
    counter = 1

    for filename in os.listdir(script_dir):
        file_path = os.path.join(script_dir, filename)

        check_for_updated(filename)  # exit if updated file is present

        try:
            if not filename.endswith('.py') and not filename.startswith('~$'):
                df_main = pd.read_excel(f'{file_path}', sheet_name='raw date per vendor')  # locate the main data_frame file
                # Try to connect to an already open workbook
                main = xw.apps.active
                if main:
                    print('Main file already open - connecing...')
                    main_file = main.books[filename]
                    sleep(2)
                else:
                    # If the workbook is not open, open it
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

    return dataframes, df_main, main_file


def get_period(dataframes, file_year, file_period=None):
    """  get year and period from the file that has it (it is the one that has 'GL') """

    for key, df in dataframes.items():
        if 'GL' in df.columns:
            if file_year is None:
                file_year = int(df['Year'][0])
                file_period = int(df['Period'][0])
    return file_year, file_period


def clean_data(dataframes, columns):
    print('Cleaning data...')

    for key, df in dataframes.items():

        if 'GL' in df.columns:  # only the file we need to rename contains the 'GL' column name
            # dataframes[key] = this is also possible as rename() does not modify in place by default (I used inplace=True)
            df.rename(columns={'GL': 'G/L Account', 'Vendor Name': 'Name 1', 'Amount_Act': 'Amount in Loc.Crcy 2'},
                      inplace=True)

            # replace empty values with '' - needed as otherwise in the pivot grand total is not correct as the rows with no data are omitted?!
        for col in columns:
            df[col] = df[col].replace(np.nan, '')


def create_sub_pivots(dataframes):
    pv_tables = []
    print('Creating pivot tables...')
    # creating a list with the pivot tables of all files to be added in the folder
    for key, df in dataframes.items():
        pv_tables = [pd.pivot_table(df, values=['Amount in Loc.Crcy 2', 'Amount in Local Currency'],
                                    index=['Company Code', 'G/L Account', 'Vendor', 'Name 1'],
                                    aggfunc='sum').reset_index()]
    return pv_tables


def create_main_pivot(pv_tables, file_year):
    # Create the combined pivot table

    pivot = pd.concat(pv_tables, ignore_index=True)

    file_year, file_period = get_period(dataframes, file_year)

    pivot['Year'] = file_year
    pivot['Period'] = file_period

    return pivot


def get_columns_to_update(pivot):
    print('Normalizing file formats...')
    # Defining the columns to update the main file with
    vendors = pivot['Vendor'].apply(
        lambda x: f"'{x}")  # adding ' in front of the numbers to be interpreted as text (needed for main Excel file logic)
    g_l = pivot['G/L Account'].apply(
        lambda x: f"'{x}")  # adding ' in front of the numbers to be interpreted as text (needed for main Excel file logic)
    name = pivot['Name 1']
    amount = pivot['Amount in Local Currency']
    year = pivot['Year']
    period = pivot['Period']

    return vendors, g_l, name, amount, year, period


def prep_update_package():
    data = []
    # save the data to be added as list in order to paste it in the Excel file in one shot
    vendors, g_l, name, amount, year, period = get_columns_to_update(pivot)
    print('Preparing data package...')
    for g, v, n, a, y, p in zip(g_l.values, vendors.values, name.values, amount.values, year.values, period.values):
        data.append([g, v, n, None, None, None, None, a, y, p])

    return data


def get_main_sheet(main_file):
    # which sheet we will update in the main file
    sheet = main_file.sheets['raw date per vendor']

    return sheet


def get_start_row(df_main):
    start_row = len(df_main.iloc[:, 0]) + 2  # find the first empty row

    return start_row


def update(data):
    print('Updating main file. Please wait...')
    sheet.range(f'B{start_row}').value = data  # write data to Excel file
    sleep(10)  # wait for the Excel to update formulas


file_year = None
file_period = None
cols = ['Company Code', 'G/L Account', 'Vendor', 'Name 1']

script_dir = get_filepath()
dataframes, df_main, main_file = get_df(script_dir)
clean_data(dataframes, cols)
check_for_df(dataframes)
pv_tables = create_sub_pivots(dataframes)
pivot = create_main_pivot(pv_tables, file_year)
data = prep_update_package()
sheet = get_main_sheet(main_file)
start_row = get_start_row(df_main)
update(data)

print('Saving...')
main_file.save(f'(UPDATED){main_file.name}')  # save the Excel file
print('All DONE!')
print('Quitting...')

app = xw.apps.active  # To quit Excel if needed
app.quit()
