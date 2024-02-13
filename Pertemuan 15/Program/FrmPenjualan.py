import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Penjualan import Penjualan
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry
class FormPenjualan:   
    def __init__(self, parent):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title("Aplikasi Data Penjualan")
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        
         # int 
        Label(mainFrame, text='ID_OBAT:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        # Textbox ID_OBAT
        self.txtID_OBAT = Entry(mainFrame) 
        self.txtID_OBAT.grid(row=0, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='ID_PEMBELI:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        # Textbox ID_PEMBELI
        self.txtID_PEMBELI = Entry(mainFrame) 
        self.txtID_PEMBELI.grid(row=1, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL_OBAT:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_OBAT
        self.txtTOTAL_OBAT = Entry(mainFrame) 
        self.txtTOTAL_OBAT.grid(row=2, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='HARGA:').grid(row=3, column=0, sticky=W, padx=5, pady=5)
        # Textbox HARGA
        self.txtHARGA = Entry(mainFrame) 
        self.txtHARGA.grid(row=3, column=1, padx=5, pady=5)
                
         # int 
        Label(mainFrame, text='TOTAL_HARGA:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        # Textbox TOTAL_HARGA
        self.txtTOTAL_HARGA = Entry(mainFrame) 
        self.txtTOTAL_HARGA.grid(row=4, column=1, padx=5, pady=5) 
        self.txtTOTAL_HARGA.bind("<Return>",self.onCari) # menambahkan event Enter key
                
         # date 
        Label(mainFrame, text='WAKTU:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        # Date Input WAKTU
        self.txtWAKTU = DateEntry(mainFrame, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern='y-mm-dd') 
        self.txtWAKTU.grid(row=5, column=1, padx=5, pady=5)
                    
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id','id_obat','id_pembeli','total_obat','harga','total_harga','waktu')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width="30")
        self.tree.heading('id_obat', text='id_obat')
        self.tree.column('id_obat', width="100")
        self.tree.heading('id_pembeli', text='id_pembeli')
        self.tree.column('id_pembeli', width="100")
        self.tree.heading('total_obat', text='total_obat')
        self.tree.column('total_obat', width="100")
        self.tree.heading('harga', text='harga')
        self.tree.column('harga', width="100")
        self.tree.heading('total_harga', text='total_harga')
        self.tree.column('total_harga', width="30")
        self.tree.heading('waktu', text='waktu')
        self.tree.column('waktu', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtID_OBAT.delete(0,END)
        self.txtID_OBAT.insert(END,"")
                                
        self.txtID_PEMBELI.delete(0,END)
        self.txtID_PEMBELI.insert(END,"")
                                
        self.txtTOTAL_OBAT.delete(0,END)
        self.txtTOTAL_OBAT.insert(END,"")
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,"")
                                
        self.txtTOTAL_HARGA.delete(0,END)
        self.txtTOTAL_HARGA.insert(END,"")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data penjualan
        obj = Penjualan()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('',END, values=row)
            
    def onCari(self, event=None):
        total_harga = self.txtTOTAL_HARGA.get()
        obj = Penjualan()
        res = obj.getByTOTAL_HARGA(total_harga)
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
        total_harga = self.txtTOTAL_HARGA.get()
        obj = Penjualan()
        res = obj.getByTOTAL_HARGA(total_harga)
            
        self.txtID_OBAT.delete(0,END)
        self.txtID_OBAT.insert(END,obj.id_obat)
                                
        self.txtID_PEMBELI.delete(0,END)
        self.txtID_PEMBELI.insert(END,obj.id_pembeli)
                                
        self.txtTOTAL_OBAT.delete(0,END)
        self.txtTOTAL_OBAT.insert(END,obj.total_obat)
                                
        self.txtHARGA.delete(0,END)
        self.txtHARGA.insert(END,obj.harga)
                                
        self.txtWAKTU.delete(0,END)
        self.txtWAKTU.insert(END,obj.waktu)
                                
        self.btnSimpan.config(text="Update")
    def onSimpan(self, event=None):
        id_obat = self.txtID_OBAT.get()
        id_pembeli = self.txtID_PEMBELI.get()
        total_obat = self.txtTOTAL_OBAT.get()
        harga = self.txtHARGA.get()
        total_harga = self.txtTOTAL_HARGA.get()
        waktu = self.txtWAKTU.get()       
        obj = Penjualan()
        obj.id_obat = id_obat
        obj.id_pembeli = id_pembeli
        obj.total_obat = total_obat
        obj.harga = harga
        obj.total_harga = total_harga
        obj.waktu = waktu
        if(self.ditemukan==True):
            res = obj.updateByTOTAL_HARGA(total_harga)
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
        total_harga = self.txtTOTAL_HARGA.get()
        obj = Penjualan()
        obj.total_harga = total_harga
        if(self.ditemukan==True):
            res = obj.deleteByTOTAL_HARGA(total_harga)
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
    aplikasi = FormPenjualan(root)
    root.mainloop() 