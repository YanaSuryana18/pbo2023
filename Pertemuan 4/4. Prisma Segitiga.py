import tkinter as tk
from tkinter import ttk
import math
from Modul import luas_prismasegitiga, volume_prismasegitiga

def hitung():
    try:
        panjang_alas_segitiga = float(entry_panjang_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())

        luas_permukaan = luas_prismasegitiga (panjang_alas_segitiga, tinggi_segitiga, tinggi_prisma) 
        volume = volume_prismasegitiga (panjang_alas_segitiga, tinggi_segitiga, tinggi_prisma)

        hasil_label.config(text=f"Luas Permukaan Prisma Segitiga: {luas_permukaan:.2f}\nVolume Prisma Segitiga: {volume:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan nilai yang valid!")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Kalkulator Prisma Segitiga")

# Membuat label dan input fields
panjang_alas_segitiga_label = ttk.Label(root, text="Panjang Alas Segitiga:")
entry_panjang_alas_segitiga = ttk.Entry(root)
tinggi_segitiga_label = ttk.Label(root, text="Tinggi Segitiga:")
entry_tinggi_segitiga = ttk.Entry(root)
tinggi_prisma_label = ttk.Label(root, text="Tinggi Prisma:")
entry_tinggi_prisma = ttk.Entry(root)

# Membuat tombol hitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(root, text="Hasil akan ditampilkan di sini")

# Menyusun elemen-elemen dalam grid
panjang_alas_segitiga_label.grid(row=0, column=0)
entry_panjang_alas_segitiga.grid(row=0, column=1)
tinggi_segitiga_label.grid(row=1, column=0)
entry_tinggi_segitiga.grid(row=1, column=1)
tinggi_prisma_label.grid(row=2, column=0)
entry_tinggi_prisma.grid(row=2, column=1)
hitung_button.grid(row=3, columnspan=2)
hasil_label.grid(row=4, columnspan=2)

root.mainloop()
