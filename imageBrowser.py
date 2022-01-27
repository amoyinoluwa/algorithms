from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog

class ImageBrowser(EasyFrame):

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Image Browser")
        self.setSize(220, 200)
        self.imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
        self.addButton(text = "Find image", row = 1, column = 0, columnspan = 2, command = self.findImage)

    def findImage(self):
        """Pops up an open file dialog, and if a file is selected, displays its image in the label and its pathname in the title bar."""
        # Write your code here
        inputFile = ('png files', '.gif') #could add more files
        fileName = tkinter.filedialog.askopenfilename(parent = self, filetypes = inputFile)
        if (fileName != ""):
            #this is only for image files
            self.image = PhotoImage(file = fileName)
            self.imageLabel["image"] = self.image
            self.setTitle(fileName)
        else:
            self.imageLabel["text"] = "No file selected"

def main():
    """Instantiate and pop up the window."""
    ImageBrowser().mainloop()

if __name__ == "__main__":
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("\nProgram closed.")
    
