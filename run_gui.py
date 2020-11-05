import json
import gtjt 
import tkinter as tk
from tkinter import filedialog, Text
import os.path
import sys
  

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def getOutputDirectory():
  #Creates OutputDirectory
  out_directory = "output"
  os.makedirs(resource_path(out_directory), exist_ok=True)
  return resource_path(out_directory)


app = { 
  'title':"ConvertFile - Google Taks JSON to TXT",
  'width':600,
  'height':400,
  'background_color':"#373a40",
  'foreground_color':"#ffffff",
  'font_color':"#ffffff",
  'font':["Helvetica", 16],
  'button_color':"#686d76",
  'output_directory': getOutputDirectory()
}

root = tk.Tk()
root.title(app['title'])
root.iconbitmap(resource_path('icon.ico'))
gtask_file = tk.StringVar()
gtask_file.set("<not selected>")



def printOutput(string,append=True):
    if append:    
      txt_Output.insert(tk.END, string + "\n")
    else:
      txt_Output.delete('1.0', tk.END)
      txt_Output.insert(tk.END, string + "\n")
    

def buttonConvertFile_click(file):
    if os.path.isfile(file):
      printOutput('Processing Files ...')
      if gtjt.ConvertFile(file,app['output_directory']):
        printOutput('Done.')
        printOutput('The lists have been extracted to the default Output directory')
      else:
        printOutput('Unable to process file. File is either invalid or inacessible.')  
    else:
      printOutput('Invalid File')
      

def buttonOpenFile_click():
  filename = filedialog.askopenfilename(initialdir="/", title="Selecte Gtask JSON File",
                                       filetype=(("JSON Object","*.JSON"),("all files","*.*")))
  gtask_file.set(filename)
  printOutput(filename)
  
def buttonOpenOutputFolder_click():
  path = os.path.realpath(app['output_directory'])
  os.startfile(path)


canvas = tk.Canvas(root,height=app['height'],width=app['width'],bg=app['background_color'])
canvas.pack()

topFrame = tk.Frame(root,bg=app['background_color'])
topFrame.place(relwidth=0.94,relheight=0.6,relx=0.03,rely=0.03)

bottomFrame = tk.Frame(root)
bottomFrame.pack(side='bottom')

label_GTaskFile = tk.Label(topFrame, text="Google Tasks JSON to TXT Parser", 
                                  font=app['font'],bg=app['background_color'],
                                  fg=app["font_color"],
                                  justify="left")

txt_Output = tk.Text(topFrame, height=30, width=400, wrap='word')

label_GTaskFile.grid(row=0,column=0)
txt_Output.grid(row=2,column=0,columnspan=10,pady=4)                             

buttonOpenFile = tk.Button(root, text="Select JSON File", 
                            padx=10, 
                            pady=5, 
                            fg=app['foreground_color'],
                            bg=app['button_color'],
                            command=buttonOpenFile_click)

buttonConvertFile = tk.Button(root, text="Extract Lists", 
                              padx=10, 
                              pady=5, 
                              fg=app['foreground_color'],
                              bg=app['button_color'],
                              command=lambda: buttonConvertFile_click(gtask_file.get()))

buttonOpenOutputFolder = tk.Button(root, text="Open Output Folder", 
                              padx=10, 
                              pady=5, 
                              fg=app['foreground_color'],
                              bg=app['button_color'],
                              command=buttonOpenOutputFolder_click)

buttonOpenOutputFolder.pack(side="right",padx=1,pady=1)
buttonConvertFile.pack(side="right",padx=1,pady=1)
buttonOpenFile.pack(side="right",padx=1,pady=1)

printOutput("To begin, please select the Google Tasks JSON file obtained trough Google TakeOut")


root.mainloop()

