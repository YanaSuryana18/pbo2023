import tkinter as tk
from tkinter import ttk
import math
from Modul import luas_limassegitiga, volume_limassegitiga

def hitung():
    try:
        panjang_alas_segitiga = float(entry_panjang_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_limas = float(entry_tinggi_limas.get())

        # Hitung luas permukaan limas segitiga
        luas_permukaan = luas_limassegitiga (panjang_alas_segitiga, tinggi_segitiga)

        # Hitung volume limas segitiga
        volume = volume_limassegitiga (panjang_alas_segitiga, tinggi_segitiga)

        # Tampilkan hasil
        hasil_label.config(text=f"Luas Permukaan Limas Segitiga: {luas_permukaan:.2f}\nVolume Limas Segitiga: {volume:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan nilai yang valid!")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Kalkulator Limas Segitiga")

# Membuat label dan input fields
panjang_alas_segitiga_label = ttk.Label(root, text="Panjang Alas Segitiga:")
entry_panjang_alas_segitiga = ttk.Entry(root)
tinggi_segitiga_label = ttk.Label(root, text="Tinggi Segitiga:")
entry_tinggi_segitiga = ttk.Entry(root)
tinggi_limas_label = ttk.Label(root, text="Tinggi Limas:")
entry_tinggi_limas = ttk.Entry(root)

# Membuat tombol hitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(root, text="Hasil akan ditampilkan di sini")

# Menyusun elemen-elemen dalam grid
panjang_alas_segitiga_label.grid(row=0, column=0)
entry_panjang_alas_segitiga.grid(row=0, column=1)
tinggi_segitiga_label.grid(row=1, column=0)
entry_tinggi_segitiga.grid(row=1, column=1)
tinggi_limas_label.grid(row=2, column=0)
entry_tinggi_limas.grid(row=2, column=1)
hitung_button.grid(row=3, columnspan=2)
hasil_label.grid(row=4, columnspan=2)

root.mainloop()
