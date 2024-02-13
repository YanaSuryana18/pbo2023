from db import DBConnection as mydb
class Penjualan:
    def __init__(self):
        self.__id=None
        self.__id_obat=None
        self.__id_pembeli=None
        self.__total_obat=None
        self.__harga=None
        self.__total_harga=None
        self.__waktu=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def id_obat(self):
        return self.__id_obat
        
    @id_obat.setter
    def id_obat(self, value):
        self.__id_obat = value
    @property
    def id_pembeli(self):
        return self.__id_pembeli
        
    @id_pembeli.setter
    def id_pembeli(self, value):
        self.__id_pembeli = value
    @property
    def total_obat(self):
        return self.__total_obat
        
    @total_obat.setter
    def total_obat(self, value):
        self.__total_obat = value
    @property
    def harga(self):
        return self.__harga
        
    @harga.setter
    def harga(self, value):
        self.__harga = value
    @property
    def total_harga(self):
        return self.__total_harga
        
    @total_harga.setter
    def total_harga(self, value):
        self.__total_harga = value
    @property
    def waktu(self):
        return self.__waktu
        
    @waktu.setter
    def waktu(self, value):
        self.__waktu = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__id_obat,self.__id_pembeli,self.__total_obat,self.__harga,self.__total_harga,self.__waktu)
        sql="INSERT INTO Penjualan (id_obat,id_pembeli,total_obat,harga,total_harga,waktu) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__id_obat,self.__id_pembeli,self.__total_obat,self.__harga,self.__total_harga,self.__waktu, id)
        sql="UPDATE penjualan SET id_obat = %s,id_pembeli = %s,total_obat = %s,harga = %s,total_harga = %s,waktu = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByTOTAL_HARGA(self, total_harga):
        self.conn = mydb()
        val = (self.__id_obat,self.__id_pembeli,self.__total_obat,self.__harga,self.__waktu, total_harga)
        sql="UPDATE penjualan SET id_obat = %s,id_pembeli = %s,total_obat = %s,harga = %s,waktu = %s WHERE total_harga=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM penjualan WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByTOTAL_HARGA(self, total_harga):
        self.conn = mydb()
        sql="DELETE FROM penjualan WHERE total_harga='" + str(total_harga) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM penjualan WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__id_obat = self.result[1]
        self.__id_pembeli = self.result[2]
        self.__total_obat = self.result[3]
        self.__harga = self.result[4]
        self.__total_harga = self.result[5]
        self.__waktu = self.result[6]
        self.conn.disconnect
        return self.result
    def getByTOTAL_HARGA(self, total_harga):
        a=str(total_harga)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM penjualan WHERE total_harga='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__id_obat = self.result[1]
           self.__id_pembeli = self.result[2]
           self.__total_obat = self.result[3]
           self.__harga = self.result[4]
           self.__total_harga = self.result[5]
           self.__waktu = self.result[6]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__id_obat = ''
           self.__id_pembeli = ''
           self.__total_obat = ''
           self.__harga = ''
           self.__total_harga = ''
           self.__waktu = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM penjualan"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,id_pembeli FROM penjualan"
        self.result = self.conn.findAll(sql)
        return self.result        
        