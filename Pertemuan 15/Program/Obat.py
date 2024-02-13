# filename : Obat.py
from db import DBConnection as mydb
class Obat:
    def __init__(self):
        self.__id=None
        self.__nama=None
        self.__jenis=None
        self.__harga=None
        self.__stok=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jenis(self):
        return self.__jenis
        
    @jenis.setter
    def jenis(self, value):
        self.__jenis = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    @property
    def stok(self):
        return self.__stok
        
    @stok.setter
    def stok(self, value):
        self.__stok = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama,self.__jenis,self.__harga,self.__stok)
        sql="INSERT INTO Obat (nama,jenis,harga,stok) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama,self.__jenis,self.__harga,self.__stok, id)
        sql="UPDATE obat SET nama = %s,jenis = %s,harga = %s,stok = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA(self, nama):
        self.conn = mydb()
        val = (self.__jenis,self.__harga,self.__stok, nama)
        sql="UPDATE obat SET jenis = %s,harga = %s,stok = %s WHERE nama=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA(self, nama):
        self.conn = mydb()
        sql="DELETE FROM obat WHERE nama='" + str(nama) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama = self.result[1]
        self.__jenis = self.result[2]
        self.__harga = self.result[3]
        self.__stok = self.result[4]
        self.conn.disconnect
        return self.result
    def getByNAMA(self, nama):
        a=str(nama)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM obat WHERE nama='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama = self.result[1]
           self.__jenis = self.result[2]
           self.__harga = self.result[3]
           self.__stok = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama = ''
           self.__jenis = ''
           self.__harga = ''
           self.__stok = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,jenis FROM obat"
        self.result = self.conn.findAll(sql)
        return self.result        