import math 
# Fungsi untuk menghitung luas permukaan dan volume kubus
def luas_kubus(sisi):
    luas_permukaan1 = 6 * (sisi ** 2)
    return luas_permukaan1
def volume_kubus (sisi):
    volume1 = sisi ** 3
    return volume1

# Fungsi untuk menghitung luas permukaan dan volume balok
def luas_balok(panjang, lebar, tinggi):
    luas_permukaan2 = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    return luas_permukaan2
def volume_balok (panjang, lebar, tinggi):
    volume2 = panjang * lebar * tinggi
    return volume2

# Fungsi untuk menghitung luas permukaan dan volume limas segiempat
def luas_limasSegiempat (panjang, lebar, tinggi):
    luas_permukaan3 = panjang * lebar + panjang * math.sqrt((lebar/2)**2 + tinggi**2) + lebar * math.sqrt((panjang/2)**2 + tinggi**2)
    return luas_permukaan3
def volume_limasSegiempat (panjang, lebar, tinggi):
    volume3 = (panjang * lebar * tinggi) / 3
    return volume3


# Fungsi untuk menghitung luas permukaan dan volume limas prismaSegitiga
def luas_prismasegitiga (panjang_alas_segitiga, tinggi_segitiga, tinggi_prisma) :
    luas_permukaan4 = (2 * panjang_alas_segitiga * tinggi_segitiga + (panjang_alas_segitiga * tinggi_prisma))
    return luas_permukaan4
def volume_prismasegitiga (panjang_alas_segitiga, tinggi_segitiga, tinggi_prisma) :
    volume4 = (panjang_alas_segitiga * tinggi_segitiga* tinggi_prisma) / 2
    return volume4

# Fungsi untuk menghitung luas permukaan dan volume limassegitiga
def luas_limassegitiga (panjang_alas_segitiga, tinggi_segitiga) :
    luas_permukaan5 = panjang_alas_segitiga ** 2 + 3 * (panjang_alas_segitiga * math.sqrt((panjang_alas_segitiga / 2) ** 2 + tinggi_segitiga ** 2))
    return luas_permukaan5
def volume_limassegitiga (panjang_alas_segitiga, tinggi_limas) :
    volume5 = (panjang_alas_segitiga ** 2 * tinggi_limas) / 6
    return volume5

# Fungsi untuk menghitung luas permukaan dan volume tabung
def luas_tabung (jari_jari, tinggi) :
    luas_permukaan6 = 2 * math.pi * jari_jari * (jari_jari + tinggi)
    return luas_permukaan6
def volume_tabung (jari_jari, tinggi) :
    volume6 = math.pi * jari_jari**2 * tinggi
    return volume6

# Fungsi untuk menghitung luas permukaan dan volume tabung
def luas_kerucut (tinggi, jari_jari) :
    luas_permukaan7 = 3.14 * jari_jari * (jari_jari + ((tinggi ** 2 + jari_jari ** 2) ** 0.5))
    return luas_permukaan7
def volume_kerucut (tinggi, jari_jari) :
    volume7 = (1/3) * 3.14 * jari_jari**2 * tinggi
    return volume7


def luas_bola (jari_jari) :
    luas_permukaan8 = 4 * math.pi * jari_jari ** 2
    return luas_permukaan8
def volume_bola (jari_jari) :
    volume8 = (4/3) * math.pi * jari_jari ** 3
    return volume8