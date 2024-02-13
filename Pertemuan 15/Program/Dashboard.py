import tkinter as tk
from tkinter import ttk
from FrmObat import *
from FrmPembeli import *
from FrmPenjualan import *

def new_window(_class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new)

# Window
window = tk.Tk()
window.title("Multiform")
window.geometry("300x200")

# Frame
frame = ttk.Frame(window, padding=10, style="My.TFrame")  # Tambahkan padding dan gunakan style untuk memberikan warna latar belakang
frame.pack()

nama = ttk.Label(frame, text="Yana Suryana", style="My.TLabel")  # Gunakan style untuk memberikan warna latar belakang
nama.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)

nim = ttk.Label(frame, text="220511110", style="My.TLabel")  # Gunakan style untuk memberikan warna latar belakang
nim.grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)

kelas = ttk.Label(frame, text="TIF22E", style="My.TLabel")  # Gunakan style untuk memberikan warna latar belakang
kelas.grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)

# Bar Menu
menu = tk.Menu(window)
window.config(menu=menu)

# Menambahkan style untuk memberikan warna latar belakang pada menu
window.tk_setPalette(background="#FF0000")

# Menu Calculator
menu.apotek = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="APOTEK PENJUALAN OBAT", menu=menu.apotek)
menu.apotek.add_command(label="Obat", command=lambda: new_window(FormObat))
menu.apotek.add_command(label="Pembeli", command=lambda: new_window(FormPembeli))
menu.apotek.add_command(label="Penjual", command=lambda: new_window(FormPenjualan))

# Menambahkan style untuk memberikan warna latar belakang pada menu
window.tk_setPalette(background="#FF0000")

# Menambahkan style untuk frame dan label
style = ttk.Style()
style.configure("My.TFrame", background="#000000")  # Ganti warna latar belakang frame sesuai keinginan
style.configure("My.TLabel", background="#FF0000")  # Ganti warna latar belakang label sesuai keinginan

window.mainloop()
