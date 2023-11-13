import tkinter as tk
from tkinter import Label, Entry, Button
from Modul import luas_kerucut, volume_kerucut
# Fungsi untuk menghitung luas permukaan dan volume kerucut
def hitung_kerucut():
    try:
        jari_jari = float(jari_jari_entry.get())
        tinggi = float(tinggi_entry.get())
        luas_permukaan = luas_kerucut (jari_jari, tinggi)
        volume = volume_kerucut (jari_jari, tinggi)
        hasil.config(text=f"Luas Permukaan: {luas_permukaan:.2f}\nVolume: {volume:.2f}")
    except ValueError:
        hasil.config(text="Masukkan angka yang valid")

# Membuat jendela utama
app = tk.Tk()
app.title("Kalkulator Kerucut")

# app.configure(bg="black")
app.geometry("400x300")


# Membuat label dan entry untuk jari-jari
jari_jari_label = Label(app, text="Jari-Jari Kerucut:")
jari_jari_label.pack()
jari_jari_entry = Entry(app)
jari_jari_entry.pack()

# Membuat label dan entry untuk tinggi
tinggi_label = Label(app, text="Tinggi Kerucut:")
tinggi_label.pack()
tinggi_entry = Entry(app)
tinggi_entry.pack()

# Tombol untuk menghitung
hitung_button = Button(app, text="Hitung", command=hitung_kerucut)
hitung_button.pack()

# Label untuk menampilkan hasil
hasil = Label(app, text="")
hasil.pack()

app.mainloop()
