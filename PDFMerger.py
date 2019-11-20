
from __future__ import print_function
from reportlab.pdfgen import canvas
import os  
from PyPDF2 import PdfFileMerger
import PySimpleGUI as sg


############################################## Warning: No error handling
############################################## actual functionality #######################################

def create_pdf(vals):
    TEXT = """
    a wonderful file
    created with Sample_Code/makesimple.py"""
    output_filename = "TEST.pdf"
    point = 1
    inch = 72
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch))
    c.setStrokeColorRGB(0,0,0)
    c.setFillColorRGB(0,0,0)
    c.setFont("Helvetica", 12 * point)
    v = 10 * inch
    for subtline in TEXT.split( '\n' ):
        c.drawString( 1 * inch, v, subtline )
        v -= 12 * point
    c.showPage()
    c.save()
    print("Created Deckblatt")


def merge(file1,file2,out):
    merger = PdfFileMerger()

    merger.append(file1)
    merger.append(file2)

    # Write to an output PDF document
    output = open(out, "wb")
    merger.write(output)

def processPDFs(vals):
    output_f = os.path.split(vals["file_1_k"])[0]
    output_f += "/"+vals["out_k"]+".pdf"

    if(vals["file_2_k"]!=""):
        merge(vals["file_1_k"],vals["file_2_k"],output_f)

    if(vals["Deckb_k"]):
        #merge(output_f,_DECKBLATT_,output_f) #output_f kann evtl vorher noch nicht generiert worden sein
        create_pdf(vals)
    

############################################### UI ######################################################

layout = [
    [sg.Text("Deckblatt erstellen")],
    [sg.Text("Kurs")],
    [sg.Input(key="kurs_k")],
    [sg.Text("Gruppe")],
    [sg.Input(key="gruppe_k")],
    [sg.Text("Blatt")],
    [sg.Input(key="blatt_k")],
    [sg.Text("Mitglieder")],
    [sg.Input(key="mitgl_k")],
    [sg.Text('PDF File')], 
    [sg.Input(key="file_1_k"), sg.FileBrowse()],
    [sg.Text('Optional File 2')], 
    [sg.Input(key="file_2_k"), sg.FileBrowse()],
    [sg.Text("Output filename")],
    [sg.Input(key="out_k")],
    [sg.Checkbox("Deckblatt generieren",default=True,key="Deckb_k"),sg.Button("Process")]
]

window = sg.Window("PDF Toolkit",layout)

while(True):
    print()
    event, values = window.read()
    if(event == "Process"):
        processPDFs(values)
    if event in (None, "Cancel"):
        break

window.close()

#################################################### END OF UI STUFF #################################
