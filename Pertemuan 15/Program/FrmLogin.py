import tkinter as tk
from tkinter import messagebox

class FormLogin(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("LOGIN APOTEK PEJUALAN OBAT")
        self.geometry("300x150")

        self.username_label = tk.Label(self, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(self)
        self.username_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self, text="Login", command=self.check_login)
        self.login_button.pack()

    def check_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Ganti kondisi ini dengan pengecekan sesuai kebutuhan aplikasi Anda
        if username == "yana suryana" and password == "yanasuryana18":
            messagebox.showinfo("Login", "Login berhasil!")
        else:
            messagebox.showerror("Login", "Username atau password salah")

if __name__ == "__main__":
    app = FormLogin()
    app.mainloop()
