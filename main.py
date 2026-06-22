 # --uac-admin
import os
import sys
import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
import subprocess
import threading

current_ver = 'v1.1.0'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

def blockHostsFile():
    tasks = subprocess.check_output('tasklist').splitlines()
    currentLenOfTasks = len(tasks)

    while True:
        newListOftasks = subprocess.check_output('tasklist').splitlines()
        if len(newListOftasks) > currentLenOfTasks:
            for i in newListOftasks:
                if b'notepad.exe' in i:
                    os.system('taskkill /f /im notepad.exe')
        currentLenOfTasks = len(newListOftasks)

def changeHosts(siteURL):
    if siteURL == "" or siteURL == " " or not "." in siteURL or " " in siteURL:
        messagebox.showerror('Enter correct url', f'It seems {siteURL} isnt a valid url...')
        return

    answer = messagebox.askyesno('Are You sure?', 'You really want to PERMANENTLY block ' + siteURL + "?")

    if not answer:
        root = tk.Tk()
        root.withdraw()

        messagebox.showinfo('You declined blocking', 'You declined blocking ' + siteURL)
    else:
        try:
            with open(hosts_path, 'a', encoding='utf-8') as h:
                h.write(f'\n127.0.0.1 {siteURL.strip()}')
            messagebox.showinfo('Success', f'{siteURL} was successfully blocked on Your PC')
            webbrowser.open_new_tab('https://github.com/YuraPataridze/tunguska')
        except Exception as e:
            return f'Unknown error: {e}'

def main():
    root = tk.Tk()
    root.title("TUNGUSKA " + current_ver)
    root.geometry("400x200")
    root.resizable(False, False)

    #чтоб оно вообще открылось ебать меня блять заебало всё меян уже
    root.deiconify()
    root.lift()
    root.focus_force()

    main_frame = ttk.Frame(root, padding="20")
    main_frame.pack(fill="both", expand=True)

    label_instruction = ttk.Label(main_frame, text="Enter site url You want to block(e.g, 1xbet.com)")
    label_instruction.pack(pady=(0, 5), anchor="w")

    text_input = ttk.Entry(main_frame, width=30)
    text_input.pack(fill="x", pady=(0, 15))
    text_input.focus()

    submit_button = ttk.Button(main_frame, text="Block it", command=lambda: changeHosts(text_input.get()))
    submit_button.pack(pady=(0, 15))

    spacer = ttk.Label(main_frame, text="")
    spacer.pack(fill="both", expand=True)

    footer_text = f"TUNGUSKA {current_ver} was created by YuraPataridze"
    footer_label = tk.Label(
        main_frame,
        text=footer_text,
        font=("Helvetica", 9, "underline"),
        fg="blue",
        cursor="hand2"
    )
    footer_label.pack(side="bottom", pady=(10, 0))

    def openLink(event):
        webbrowser.open_new_tab("https://github.com/YuraPataridze")

    footer_label.bind("<Button-1>", openLink)

    root.mainloop()

if __name__ == "__main__":
    monitoring = threading.Thread(target=blockHostsFile, daemon=True)
    monitoring.start()

    main()