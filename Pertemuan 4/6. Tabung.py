import tkinter as tk
from tkinter import ttk
import math
from Modul import luas_tabung, volume_tabung

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        luas_permukaan = luas_tabung (jari_jari, tinggi)
        volume = volume_tabung (jari_jari, tinggi)

        hasil_label.config(text=f"Luas Permukaan Tabung: {luas_permukaan:.2f}\nVolume Tabung: {volume:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan nilai yang valid!")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Kalkulator Tabung")

# Membuat label dan input fields
jari_jari_label = ttk.Label(root, text="Jari-jari:")
entry_jari_jari = ttk.Entry(root)
tinggi_label = ttk.Label(root, text="Tinggi:")
entry_tinggi = ttk.Entry(root)

# Membuat tombol hitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(root, text="Hasil akan ditampilkan di sini")

# Menyusun elemen-elemen dalam grid
jari_jari_label.grid(row=0, column=0)
entry_jari_jari.grid(row=0, column=1)
tinggi_label.grid(row=1, column=0)
entry_tinggi.grid(row=1, column=1)
hitung_button.grid(row=2, columnspan=2)
hasil_label.grid(row=3, columnspan=2)

root.mainloop()
