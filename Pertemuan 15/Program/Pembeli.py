from db import DBConnection as mydb
class Pembeli:
    def __init__(self):
        self.__id=None
        self.__nama=None
        self.__alamat=None
        self.__jenis_kelamin=None
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
    def alamat(self):
        return self.__alamat
        
    @alamat.setter
    def alamat(self, value):
        self.__alamat = value
    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
        
    @jenis_kelamin.setter
    def jenis_kelamin(self, value):
        self.__jenis_kelamin = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama,self.__alamat,self.__jenis_kelamin)
        sql="INSERT INTO Pembeli (nama,alamat,jenis_kelamin) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama,self.__alamat,self.__jenis_kelamin, id)
        sql="UPDATE pembeli SET nama = %s,alamat = %s,jenis_kelamin = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateByNAMA(self, nama):
        self.conn = mydb()
        val = (self.__alamat,self.__jenis_kelamin, nama)
        sql="UPDATE pembeli SET alamat = %s,jenis_kelamin = %s WHERE nama=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM pembeli WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteByNAMA(self, nama):
        self.conn = mydb()
        sql="DELETE FROM pembeli WHERE nama='" + str(nama) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM pembeli WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama = self.result[1]
        self.__alamat = self.result[2]
        self.__jenis_kelamin = self.result[3]
        self.conn.disconnect
        return self.result
    def getByNAMA(self, nama):
        a=str(nama)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM pembeli WHERE nama='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama = self.result[1]
           self.__alamat = self.result[2]
           self.__jenis_kelamin = self.result[3]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama = ''
           self.__alamat = ''
           self.__jenis_kelamin = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM pembeli"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,alamat FROM pembeli"
        self.result = self.conn.findAll(sql)
        return self.result        
        