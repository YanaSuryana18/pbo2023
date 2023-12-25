print("Konversi Suhu Reamur")

# Entry
suhu = input("Masukkan Suhu Dalam Reamur")

# Rumus
F = (9/4 * float(suhu)) + 32
C = (5/4 * float(suhu))
K = (5/4 * float(suhu)) + 273

# Output
print(suhu + " Reamur Sama Dengan ")
print(str(F) + " Fahrenheit ")
print(str(C) + " Celcius ")
print(str(K) + " Kelvin ")