missing = []
from sys import argv
try:    
    from PyPDF2 import PdfFileMerger
except:
    missing.append("PyPDF2")
try:
    import PySimpleGUI as sg
except:
    missing.append("PySimpleGUI")

if(len(missing)>0): print("Missing module(s): ")
for mod in missing:
    print(mod)

del missing 

###############################################

layout = [
    [sg.Text("Deckblatt erstellen")],
    [sg.Text("Kurs"),sg.InputText()],
    [sg.Text("Gruppe"),sg.InputText()],
    [sg.Text("Blatt"),sg.InputText()],
    [sg.Text("Mitglieder"),sg.InputText()],
    [sg.FilesBrowse("Dateien")]
]

sel_file = [[sg.Text('PDF File')], [sg.Input(), sg.FileBrowse()]]

window = sg.Window("PDFMerger",layout)

while(True):
    print()
    event, values = window.read()
    if event in (None, "Cancel"):
        break

window.close(); 

def create_pdf():
    pass

def merge():
    args = argv

    merger = PdfFileMerger()

    for arg in args[1:-1]:
        file_p = arg.replace("\\","\\\\")
        print(file_p)
        merger.append(file_p)

    # Write to an output PDF document
    output = open(args[-1]+".pdf", "wb")
    merger.write(output)