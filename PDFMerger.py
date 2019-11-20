from sys import argv
from PyPDF2 import PdfFileMerger
import PySimpleGUI as sg 

layout = [
    [sg.Text("Deckblatt erstellen")],
    [sg.Text("Kurs"),sg.InputText()],
    [sg.Text("Gruppe"),sg.InputText()],
    [sg.Text("Blatt"),sg.InputText()],
    [sg.Text("Mitglieder"),sg.InputText()],
    [sg.FilesBrowse("Dateien")]
]

sel_file = sg.Window('Select File').Layout(
    [[sg.Text('PDF File')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]])

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