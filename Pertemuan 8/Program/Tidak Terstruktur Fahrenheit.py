print("Konversi Suhu Fahrenheit")

# Entry
suhu = input("Masukkan Suhu Dalam Fahrenheit")

# Rumus
R = (4/9) * (float(suhu) - 32)
C = (5/9) * (float(suhu) - 32)
K = (5/9) * (float(suhu) - 32) + 273

# Output
print(suhu + " Fahrenheit Sama Dengan ")
print(str(R) + " Reamur ")
print(str(C) + " Celcius ")
print(str(K) + " Kelvin ")