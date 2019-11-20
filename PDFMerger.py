
from __future__ import print_function
from reportlab.pdfgen import canvas
import os  
from PyPDF2 import PdfFileMerger
import PySimpleGUI as sg


############################################## Warning: No error handling
############################################## actual functionality #######################################

#from: https://github.com/mstamy2/PyPDF2/blob/master/Sample_Code/makesimple.py
def create_deckblatt(vals):
    TEXT = ""
    for key in ["Kurs","Gruppe","Blatt","Aufgabe"]:
        if(vals[key]!=""):
            TEXT += key+": "+vals[key]+"\n"
    TEXT += "Mitglieder :\n"+vals["Mitglieder"]
    output_filename = "temp_deckblatt.pdf" #Created at file location
    point = 1
    inch = 72
    title = output_filename
    c = canvas.Canvas(output_filename, pagesize=(8.5 * inch, 11 * inch)) #funktioniert nur wenn 8.5 und 11, kein plan warum docs nicht gelesen lul
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

    comb_pdfs = ( len(vals["file_2_k"])!=0 )
    create_dckb = vals["Deckb_k"]

    
    if(comb_pdfs):
        if(create_dckb):
            merge(vals["file_1_k"],vals["file_2_k"],"temppdf.pdf")
            merge("temp_deckblatt.pdf","temppdf.pdf",output_f)
        else:
            merge(vals["file_1_k"],vals["file_2_k"],output_f)
    else:
        if(create_dckb):
            create_deckblatt(vals)
            merge("temp_deckblatt.pdf",vals["file_1_k"],output_f)
        else:
            print("why even use this?")

     

############################################### UI ######################################################

layout = [
    [sg.Text("Deckblatt erstellen")],
    [sg.Text("Kurs")],
    [sg.Input(key="Kurs")],#suboptimal macht aber file schreiben easier
    [sg.Text("Gruppe")],
    [sg.Input(key="Gruppe")],
    [sg.Text("Blatt")],
    [sg.Input(key="Blatt")],
    [sg.Text("Aufgabe")],
    [sg.Input(key="Aufgabe")],
    [sg.Text("Mitglieder")],
    [sg.Multiline(key="Mitglieder")],
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
