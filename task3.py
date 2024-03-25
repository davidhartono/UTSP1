import datetime

hari = int(input("Masukkan jumlah hari: "))

tanggal_setelah = datetime.datetime.now() + datetime.timedelta(days=hari)
format_tanggal = tanggal_setelah.strftime("%A on %d %B %Y")

print(format_tanggal)
