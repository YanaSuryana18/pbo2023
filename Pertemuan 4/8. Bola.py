import tkinter as tk
from tkinter import ttk
import math
from Modul import luas_bola, volume_bola

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())

        # Hitung luas permukaan bola
        luas_permukaan = luas_bola (jari_jari)

        # Hitung volume bola
        volume = volume_bola (jari_jari)

        # Tampilkan hasil
        hasil_label.config(text=f"Luas Permukaan Bola: {luas_permukaan:.2f}\nVolume Bola: {volume:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan nilai yang valid!")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Kalkulator Bola")

# Membuat label dan input field
jari_jari_label = ttk.Label(root, text="Jari-Jari Bola:")
entry_jari_jari = ttk.Entry(root)

# Membuat tombol hitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(root, text="Hasil akan ditampilkan di sini")

# Menyusun elemen-elemen dalam grid
jari_jari_label.grid(row=0, column=0)
entry_jari_jari.grid(row=0, column=1)
hitung_button.grid(row=1, columnspan=2)
hasil_label.grid(row=2, columnspan=2)

root.mainloop()
