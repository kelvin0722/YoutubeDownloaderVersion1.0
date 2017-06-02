#!./env/bin/python
import pafy
from Tkinter import *
import tkMessageBox
import tkFileDialog
import os

class MainWindow(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent,background="")
        self.parent = parent
        self.parent.clipboard_append("copy url")
        self.initUI() 
        self.default_path = os.getcwd()
    def initUI(self):
        self.parent.title("YoutubeDownloader")
        self.welcome_label = Label(self.parent,text="Welcome")
        self.welcome_label.grid(row=0, column=3)
        self.browse = Button(self.parent,text="Select file location",command=self.browse) 
        self.browse.grid(row = 7, column=2) 
        self.input = Entry(self.parent)
        self.input.grid(row = 7, column=3) 
        self.download = Button(self.parent,text="Download",command=self.downloadfile)
        self.download.grid(row = 9, column=3)                      
        self.insertClipBoard()
    
    def browse(self):
        directory = tkFileDialog.askdirectory(initialdir=self.default_path)
        if len(directory) == 0:
            pass
        else:
            self.default_path = directory   
    def insertClipBoard(self):
        clipboard_text = self.parent.clipboard_get()
        self.input.insert("insert",clipboard_text)
    def downloadfile(self):
        print("Downloading....")
        input_text = self.input.get()
        try:
            myvid = pafy.new(str(input_text))
            video_count = myvid.viewcount
            title = myvid.title
            print ("Title:%s"%(title))
            print ("Total number of views:{:,}".format(myvid.viewcount))
        except:
            tkMessageBox.showerror("Url Error","Check the file url")
            
        try:
            best_vid = myvid.getbest()
            best_audio = myvid.getbestaudio(preftype="m4a",ftypestrict=True)
        
            best_vid.download(filepath=self.default_path,quiet=False)   
            best_audio.download(filepath=self.default_path,quiet=False) 
            self.input.insert("insert","")
            tkMessageBox.showinfo("Success","File successfully downloaded")
        except:
            tkMessageBox.showerror("Failed","Check the file format")
            print("Check  the file  format")


        
def main():
    root = Tk()
    root.geometry("380x80+300+300")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()




