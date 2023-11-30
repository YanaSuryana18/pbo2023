import tkinter as tk
from pygame import mixer

def play_music():
    # Ganti path file audio dengan path file Anda
    file_path = r'C:\Users\LENOVO\OneDrive\Documents\Tugas PBO\\LINGSIR WENGI.mp3'
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()

def stop_music():
    mixer.music.stop()

# Membuat jendela
root = tk.Tk()
root.title("Pemutar Musik")

# Membuat tombol play
play_button = tk.Button(root, text="Play", command=play_music)
play_button.pack(pady=20)

# Membuat tombol stop
stop_button = tk.Button(root, text="Stop", command=stop_music)
stop_button.pack(pady=10)

# Menjalankan loop utama
root.mainloop()
