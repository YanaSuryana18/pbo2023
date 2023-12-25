print("Konversi Suhu Fahrenheit")

def get_celcius(suhu):
    C = (float(suhu) - 32) * (5/9)
    return C

def get_reamur(suhu):
    R = (float(suhu) - 32) * (4/9)
    return R

def get_kelvin(suhu):
    K = (float(suhu) + 459.67) * (5/9)
    return K

# Entry
suhu = input("Masukkan suhu dalam Fahrenheit: ")

# rumus
C = get_celcius(suhu)
R = get_reamur(suhu)
K = get_kelvin(suhu)

# Output
print(suhu + " Fahrenheit sama dengan " + str(C) + " Celcius")
print(suhu + " Fahrenheit sama dengan " + str(R) + " Reamur")
print(suhu + " Fahrenheit sama dengan " + str(K) + " Kelvin")