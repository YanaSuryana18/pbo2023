print("Konversi Suhu Kelvin")
def get_reamur(suhu):
    R = (4/5) * (float(suhu) - 273)
    return R

def get_celcius(suhu):
    C = (float(suhu) - 273)
    return C

def get_fahrenheit(suhu):
    F = (9/5) * (float(suhu) - 273) + 32
    return F

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit :")

# Rumus
R = get_reamur(suhu)
C = get_celcius(suhu)
F = get_fahrenheit(suhu)

# Output
print(suhu + " Kelvin Sama Dengan ")
print(str(R) + " Reamur ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")