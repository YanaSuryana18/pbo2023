print("Konversi Suhu Fahrenheit")
def get_reamur(suhu):
    R = (4/9) * (float(suhu) - 32)
    return R

def get_celcius(suhu):
    C = (5/9) * (float(suhu) - 32)
    return C

def get_kelvin(suhu):
    K = (5/9) * (float(suhu) - 32) + 273
    return K

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit :")

# Rumus
R = get_reamur(suhu)
C = get_celcius(suhu)
K = get_kelvin(suhu)

# Output
print(suhu + " Reamur Sama Dengan ")
print(str(R) + " Reamur ")
print(str(C) + " Celcius ")
print(str(K) + " Kelvin ")