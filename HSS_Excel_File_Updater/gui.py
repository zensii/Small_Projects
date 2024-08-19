import FreeSimpleGUI

label_main = FreeSimpleGUI.Text("select main file    ")
input_box_main = FreeSimpleGUI.InputText(tooltip='select main file')
add_button_main = FreeSimpleGUI.Button('Add')

label_new = FreeSimpleGUI.Text("select the new file")
input_box_new = FreeSimpleGUI.InputText(tooltip='select the new file')
add_button_new = FreeSimpleGUI.Button('Add')

open_explorer_main = FreeSimpleGUI.Button('Open')
open_explorer_new = FreeSimpleGUI.Button('Open')

window = FreeSimpleGUI.Window('Excel Updater', layout=[[label_main, input_box_main, open_explorer_main, add_button_main],
                                                       [label_new, input_box_new, open_explorer_new, add_button_new]])
window.read()
window.close()
