import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser

current_ver = 'v2.0.1'
hosts_path = r'C:\Windows\System32\drivers\etc\hosts'

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
                h.write(f'\n10.255.255.1 {siteURL.strip()}')
            messagebox.showinfo('Success', f'{siteURL} was successfully blocked on Your PC')
            webbrowser.open_new_tab('https://github.com/YuraPataridze/tunguska')
        except Exception as e:
            return f'Unknown error: {e}'

def main():
    root = tk.Tk()
    root.title("TUNGUSKA " + current_ver)
    root.geometry("400x250")
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

    def openLink(event):
        webbrowser.open_new_tab("https://github.com/YuraPataridze")

    # --- Footer 2: Informational Notice (Packed first, so it sits HIGHER) ---
    footer_text2 = (
        "Especially RECOMMENDED: install auto-closing hosts file "
        "if you use this program for 'parental control'. "
        "If that additional file is running (in startup), "
        "someone else will NOT be able to change the hosts file."
    )
    footer_label2 = tk.Label(
        main_frame,
        text=footer_text2,
        font=("Helvetica", 8),  # Dropped to size 8 so it fits nicely
        fg="#555555",
        justify="center",
        wraplength=360  # Wrapped to 360 to match frame padding limits
    )
    footer_label2.pack(side="bottom", pady=(5, 0))

    # --- Footer 1: Author Link (Packed second, so it sits at the VERY BOTTOM) ---
    footer_text = f"TUNGUSKA {current_ver} was created by YuraPataridze"
    footer_label = tk.Label(
        main_frame,
        text=footer_text,
        font=("Helvetica", 9, "underline"),
        fg="blue",
        cursor="hand2"
    )
    footer_label.pack(side="bottom", pady=(5, 0))
    footer_label.bind("<Button-1>", openLink)

    root.mainloop()

if __name__ == "__main__":
    main()