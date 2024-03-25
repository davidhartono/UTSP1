angka = int(input("Masukkan angka: "))

hasil = 1

for i in range(1, angka + 1):
    hasil *= i

print(f"Hasil dari 1 - {angka}: {hasil}")
