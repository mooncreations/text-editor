import tkinter as tk
from customtkinter import *

# Initialization and app setup
class MainApp(CTk):
    def __init__(self):
        super().__init__()

        self.geometry("700x400")
        self.title("Unitled - Text Editor")
        self.wm_iconbitmap("icon.ico")

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
    def on_closing(self):
        self.quit()
        self.destroy()

app = MainApp()
tk = tk.Tk()

tk.withdraw()

currentFile = "Untitled"

# Main text area
textarea = CTkTextbox(app, width=700, height=375, corner_radius=0, font=("Consolas", 16))
textarea.place(x=0, y=25)

# Save menu
saveFrame = CTkFrame(app, fg_color="transparent", width=120, height=25, corner_radius=0)
saveFrame.place(x=60, y=0)

saveFrame.place_forget()

# Change detection
def changed(event):
    global currentFile

    app.title(currentFile + "* - Text Editor")

textarea.bind("<KeyPress>", changed)

# File button function
menuShown = False

def fileMenu():
    global menuShown

    if menuShown:
        menuShown = False
        saveFrame.place_forget()
    else:
        menuShown = True
        saveFrame.place(x=60, y=0)

# Top menu buttons
fileBtn = CTkButton(app, width=60, height=25, text="File", corner_radius=0, font=("Consolas", 14, "bold"), command=fileMenu)
fileBtn.place(x=0, y=0)

# Save and load functions
def saveFile(event):
    global menuShown
    global currentFile

    saveFrame.place_forget()
    menuShown = False

    if (currentFile != "Untitled"):
        with open(currentFile, "w", encoding="utf-8") as file:
            file.write(textarea.get("0.0", "end"))
            app.title(currentFile + " - Text Editor")
    else:
        filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")], title="Save As")
        
        if filePath:
            with open(filePath, "w", encoding="utf-8") as file:
                currentFile = filePath

                file.write(textarea.get("0.0", "end"))
                app.title(currentFile + " - Text Editor")

def loadFile():
    global menuShown
    
    saveFrame.place_forget()
    menuShown = False

    filePath = filedialog.askopenfilename(title="Choose file", filetypes=[("All Files", "*.*")])

    if filePath:
        with open(filePath, "r", encoding="utf-8") as file:
            global currentFile
    
            textarea.delete("0.0", "end")
            textarea.insert("0.0", file.read())
    
            currentFile = filePath
            app.title(filePath + " - Text Editor")
    
# Save and load buttons
saveBtn = CTkButton(saveFrame, width=60, height=25, text="Save", corner_radius=0, font=("Consolas", 14, "bold"), command=saveFile)
saveBtn.place(x=0, y=0)

loadBtn = CTkButton(saveFrame, width=60, height=25, text="Load", corner_radius=0, font=("Consolas", 14, "bold"), command=loadFile)
loadBtn.place(x=60, y=0)

app.bind("<Control-s>", saveFile)

# App loop
app.mainloop()