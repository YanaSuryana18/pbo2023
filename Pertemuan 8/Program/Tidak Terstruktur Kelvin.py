print("Konversi Suhu Kelvin")

# Entry
suhu = input("Masukkan Suhu Dalam Kelvin")

# Rumus
R = (4/5) * (float(suhu) - 273)
F = (9/5) * (float(suhu) - 273) + 32
C = (float(suhu) - 273) 

# Output
print(suhu + " Kelvin Sama Dengan ")
print(str(R) + " Reamur ")
print(str(C) + " Celcius ")
print(str(F) + " Fahrenheit ")