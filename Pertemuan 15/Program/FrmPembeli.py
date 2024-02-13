import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pembeli import Pembeli
class FormPembeli:   
    def __init__(self, parent):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title("Aplikasi Data Pembeli")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # varchar 
        Label(mainFrame, text='NAMA:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox NAMA
        self.txtNAMA = Entry(mainFrame) 
        self.txtNAMA.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNAMA.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # varchar 
        Label(mainFrame, text='ALAMAT:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox ALAMAT
        self.txtALAMAT = Entry(mainFrame) 
        self.txtALAMAT.grid(row=1, column=1, padx=5, pady=5)
                
         # enum 
        Label(mainFrame, text='JENIS_KELAMIN:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Combo Box
        self.txtJENIS_KELAMIN = StringVar()
        CboJENIS_KELAMIN = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJENIS_KELAMIN) 
        CboJENIS_KELAMIN.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboJENIS_KELAMIN['values'] = ('Laki laki','Perempuan')
        CboJENIS_KELAMIN.current()
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','nama','alamat','jenis_kelamin')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('nama', text='nama')
        self.tree.column('nama', width="30")
        self.tree.heading('alamat', text='alamat')
        self.tree.column('alamat', width="100")
        self.tree.heading('jenis_kelamin', text='jenis_kelamin')
        self.tree.column('jenis_kelamin', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA.delete(0,END)
        self.txtNAMA.insert(END,"")
                                
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,"")
                                
        self.txtJENIS_KELAMIN.set("")
            
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pembeli
        obj = Pembeli()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        nama = self.txtNAMA.get()
        obj = Pembeli()
        res = obj.getByNAMA(nama)
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            # self.txtNama.focus()
        return res
            
    def TampilkanData(self, event=None):
        nama = self.txtNAMA.get()
        obj = Pembeli()
        res = obj.getByNAMA(nama)
            
        self.txtALAMAT.delete(0,END)
        self.txtALAMAT.insert(END,obj.alamat)
                                
        self.txtJENIS_KELAMIN.set(obj.jenis_kelamin)
            
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        nama = self.txtNAMA.get()
        alamat = self.txtALAMAT.get()
        jenis_kelamin = self.txtJENIS_KELAMIN.get()       
        obj = Pembeli()
        obj.nama = nama
        obj.alamat = alamat
        obj.jenis_kelamin = jenis_kelamin
        if(self.ditemukan==True):
            res = obj.updateByNAMA(nama)
            ket = 'Diperbarui'
            
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
            
        rec = obj.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        nama = self.txtNAMA.get()
        obj = Pembeli()
        obj.nama = nama
        if(self.ditemukan==True):
            res = obj.deleteByNAMA(nama)
            rec = obj.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
 
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormPembeli(root)
    root.mainloop() 
    