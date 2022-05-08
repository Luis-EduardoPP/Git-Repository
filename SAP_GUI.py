import win32com.client
import subprocess
import time
from tkinter import *
from tkinter import messagebox



class SapGui(object):
    def __init__(self):
        self.path = r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplgpad.exe"
        subprocess.Popen(self.path)

        self.SapGuiAuto = win32com.client.GetObject("SAPGUI")
        application = self.SapGuiAuto.GetScriptingEngine

        self.connection = application.OpenConnection("01 ")

        time.sleep(3)
        self.session = self.connection.Children(0)
        self.session.findById("wnd[0]").maximize

if __name__ == '__main__':
    window = Tk()
    window.geometry("200x50")
    bot = Button(window, text="Login SAP",command= lambda : SapGui().sapLogin())
    bot.pack()
    mainloop()



