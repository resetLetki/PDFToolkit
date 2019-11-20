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
    [sg.Text("Kurs")],
    [sg.Input()],
    [sg.Text("Gruppe")],
    [sg.Input()],
    [sg.Text("Blatt")],
    [sg.Input()],
    [sg.Text("Mitglieder")],
    [sg.Input()],
    [sg.Text('PDF File')], 
    [sg.Input(), sg.FileBrowse()],
    [sg.Text('Optional File 2')], 
    [sg.Input(), sg.FileBrowse()],
    [sg.Text("Output filename")],
    [sg.Input()],
    [sg.Button("Create")]
]

window = sg.Window("PDF Toolkit",layout)

while(True):
    print()
    event, values = window.read()
    print(event,values)
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