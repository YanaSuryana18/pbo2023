import tkinter as tk
from tkinter import ttk
from Modul import luas_balok, volume_balok

def hitung():
    try:
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())

        luas_permukaan = luas_balok (panjang, lebar, tinggi)
        volume = volume_balok (panjang, lebar, tinggi )

        hasil_label.config(text=f"Luas Permukaan Balok: {luas_permukaan:.2f}\nVolume Balok: {volume:.2f}")
    except ValueError:
        hasil_label.config(text="Masukkan nilai yang valid!")

# Membuat jendela Tkinter
root = tk.Tk()
root.title("Kalkulator Balok")

# Membuat label dan input fields
panjang_label = ttk.Label(root, text="Panjang:")
entry_panjang = ttk.Entry(root)
lebar_label = ttk.Label(root, text="Lebar:")
entry_lebar = ttk.Entry(root)
tinggi_label = ttk.Label(root, text="Tinggi:")
entry_tinggi = ttk.Entry(root)

# Membuat tombol hitung
hitung_button = ttk.Button(root, text="Hitung", command=hitung)

# Membuat label untuk menampilkan hasil
hasil_label = ttk.Label(root, text="Hasil akan ditampilkan di sini")

# Menyusun elemen-elemen dalam grid
panjang_label.grid(row=0, column=0)
entry_panjang.grid(row=0, column=1)
lebar_label.grid(row=1, column=0)
entry_lebar.grid(row=1, column=1)
tinggi_label.grid(row=2, column=0)
entry_tinggi.grid(row=2, column=1)
hitung_button.grid(row=3, columnspan=2)
hasil_label.grid(row=4, columnspan=2)

root.mainloop()
