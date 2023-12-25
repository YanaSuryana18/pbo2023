print("Konversi Suhu Celcius")

# Entry
suhu = input("Masukkan Suhu Dalam Celcius")

# Rumus
F = (9/5 * float(suhu)) + 32
R = (4/5 * float(suhu))
K = float(suhu) + 273

# Output
print(suhu + " Celcius Sama Dengan ")
print(str(F) + " Fahrenheit ")
print(str(R) + " Reamur ")
print(str(K) + " Kelvin ")