from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmPrismaSegitiga:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x200")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()

    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # pasang Label
        Label(mainFrame, text='Alas Segitiga:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Segitiga:").grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Tinggi Prisma:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Segitiga:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Luas Permukaan:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Volume:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)

        # pasang textbox
        self.txtAlasSegitiga = Entry(mainFrame) 
        self.txtAlasSegitiga.grid(row=0, column=1, padx=5, pady=5)  
        self.txtTinggiSegitiga = Entry(mainFrame) 
        self.txtTinggiSegitiga.grid(row=1, column=1, padx=5, pady=5)
        self.txtTinggiPrisma = Entry(mainFrame) 
        self.txtTinggiPrisma.grid(row=2, column=1, padx=5, pady=5) 
        self.txtLuasSegitiga = Entry(mainFrame) 
        self.txtLuasSegitiga.grid(row=4, column=1, padx=5, pady=5)
        self.txtLuasPermukaan = Entry(mainFrame) 
        self.txtLuasPermukaan.grid(row=5, column=1, padx=5, pady=5)
        self.txtVolume = Entry(mainFrame) 
        self.txtVolume.grid(row=6, column=1, padx=5, pady=5) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)


    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self, event=None):
        alas_segitiga = int(self.txtAlasSegitiga.get())
        tinggi_segitiga = int(self.txtTinggiSegitiga.get())
        tinggi_prisma = int(self.txtTinggiPrisma.get())
        luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga
        luas_permukaan = 2 * alas_segitiga * tinggi_segitiga + 3 * alas_segitiga * tinggi_prisma
        volume = luas_segitiga * tinggi_prisma
        self.txtLuasSegitiga.delete(0,END)
        self.txtLuasSegitiga.insert(END,str(luas_segitiga))
        self.txtLuasPermukaan.delete(0,END)
        self.txtLuasPermukaan.insert(END,str(luas_permukaan))
        self.txtVolume.delete(0,END)
        self.txtVolume.insert(END,str(volume))

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmPrismaSegitiga(root, "Program Luas Dan Volume Permukaan Prisma Segitiga")
    root.mainloop()