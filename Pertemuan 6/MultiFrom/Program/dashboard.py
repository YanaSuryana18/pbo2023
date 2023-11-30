import tkinter as tk
from tkinter import Menu
from FrmPersegi import *
from FrmSegitiga import *
from FrmLingkaran import *
from FrmBola import *
from FrmKubus import *
from FrmBalok import *
from FrmLimasSegiempat import *
from FrmLimasSegitiga import *
from FrmPrismaSegitiga import *
from FrmTabung import *
from FrmKerucut import *


# root window
root = tk.Tk()
root.title('Menu Demo')
#root.attributes('-fullscreen', True)
root.geometry("900x400")
# create a menubar
menubar = Menu(root)
root.config(menu=menubar)

# create a menu
file_menu = Menu(menubar)
app_menu = Menu(menubar)
data_menu = Menu(menubar)

# add a menu item to the menu
file_menu.add_command(
    label='File Open', command=root.destroy
)

file_menu.add_command(
    label='Exit', command=root.destroy
)

app_menu.add_command(
    label='App Persegi', command= lambda: new_window("Luas Persegi", FrmPersegi)
)
app_menu.add_command(
    label='App Segitiga', command= lambda: new_window("Luas Segitiga", FrmSegitiga)
)
app_menu.add_command(
    label='App Lingkaran', command= lambda: new_window("Luas Lingkaran", FrmLingkaran)
)
app_menu.add_command(
    label='App Bola', command= lambda: new_window("Bola", FrmBola)
)
app_menu.add_command(
    label='App Kubus', command= lambda: new_window("Kubus", FrmKubus)
)
app_menu.add_command(
    label='App Balok', command= lambda: new_window("Balok", FrmBalok)
)
app_menu.add_command(
    label='App Limas Segiempat', command= lambda: new_window("Limas Segiempat", FrmLimasSegiempat)
)
app_menu.add_command(
    label='App Limas Segitiga', command= lambda: new_window("Limas Segitiga", FrmLimasSegitiga)
)
app_menu.add_command(
    label='App Prisma Segitiga', command= lambda: new_window("Prisma Segitiga", FrmPrismaSegitiga)
)
app_menu.add_command(
    label='App Tabung', command= lambda: new_window("Tabung", FrmTabung)
)
app_menu.add_command(
    label='App Kerucut', command= lambda: new_window("Kerucut", FrmKerucut)
)


def new_window( number, _class):
    new = tk.Toplevel()
    new.transient()
    new.grab_set()
    _class(new, number)

# add the File menu to the menubar
menubar.add_cascade(
    label="File", menu=file_menu
)
menubar.add_cascade(
    label="App", menu=app_menu
)

root.mainloop()