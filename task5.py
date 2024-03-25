with open("input.txt", "r") as file:
    angka = [int(line.strip()) for line in file]

hasil = sum(angka)

print(f"{hasil:,.3f}")
