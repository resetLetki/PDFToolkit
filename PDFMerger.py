missing = []
import os
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

############################################## Warning: No error handling
############################################## actual functionality #######################################

def create_pdf():
    pass

def merge(file1,file2,out):
    base_p = os.path.split(file1)[0]

    merger = PdfFileMerger()

    #file1 = file1.replace("\\","\\\\")
    #file2 = file2.replace("\\","\\\\")
    merger.append(file1)
    merger.append(file2)

    # Write to an output PDF document
    output = open(base_p+"/"+out+".pdf", "wb")
    merger.write(output)

def processPDFs(vals):
    if(vals["file_2_k"]!=""):
        merge(vals["file_1_k"],vals["file_2_k"],vals["out_k"])

    if(vals["Deckb_k"]):
        print("deckblatt wird generiert!")
        #TODO: create and merge with end
    

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
