print()
# Program menentukan bilangan ganjil dan genap
print('## 1. Program Bilangan Ganjil dan Genap ##')
print()

# Input Bilangan
bilangan = int(input('Masukan bilangan anda: '))

# Proses dan Output
if bilangan % 2 == 0:
    print(bilangan, 'Merupakan bilangan genap')
else:
    print(bilangan, 'Merupakan bilangan ganjil')

print()
# Program menentukan nilai ujian
print('## 2. Program menentukan nilai ujian ##')
print()

# Input Nilai
nilai_ujian = int(input('Masukan Nilai Anda: '))

# Proses dan Output
if nilai_ujian >= 75: #false
    print('Kamu dinyatakan Lulus')
else:
    print('Kamu dinyatakan Tidak Lulus')

print()
# Program menentukan nilai ujian
print('## 3. Program menentukan usia dan status ##')
print()

# Input usia
usia = int(input('Masukan usia Anda: '))

# Proses dan Output
if usia >= 18:
    print('Kamu Dewasa')
elif usia >= 13 and usia <=17:
    print('Kamu Remaja')
else:
    print('Kamu Anak-Anak')

print()
# Program menentukan nilai ujian
print('## 4. Program status menentukan Keanggotaan ##')
print()

# Input Status
status_anggota = input("""Daftar Keanggotaan Dibawah ini
1. Gold
2. Silver
3. Bronze
Masukan Pilihan Kamu: """).lower()

# Proses dan Output
if status_anggota == 'gold' or status_anggota == 'silver':
    print('Selamat! Anda Mendapatkan diskon.')
elif status_anggota == 'bronze':
    print('Maaf Anda tidak mendapatkan diskon')
else:
    print('Masukan Kata dengan benar')

print()
# Program menentukan nilai ujian
print('## 5. Program pembelian diskon 10% ##')
print()

# Barang
minyak = 25000 # Variabel Minyak menyimpan nilai 25000
indomie = 5000

# Input
jumlah_pembelian_minyak = int(input("Masukkan jumlah pembelian minyak: ")) # Program meminta pengguna untuk memasukkan jumlah pembelian. 
jumlah_pembelian_indomie = int(input("Masukkan jumlah pembelian indomie: "))

# Proses Kondisi & cetak tambahan diskonnya
total_harga = (minyak * jumlah_pembelian_minyak) + (indomie * jumlah_pembelian_indomie)
diskon = 0.1

# Cek apakah total pembelian lebih dari 100 dengan shorthand if
total_diskon = total_harga * diskon if (jumlah_pembelian_minyak + jumlah_pembelian_indomie) > 100 else 0
total_harga -= total_diskon

print()
# Cetak hasil
print(f"Anda mendapatkan diskon sebesar 10%: Rp {total_diskon}" if total_diskon > 0 else "Tidak ada diskon yang diberikan.")
print(f"Total harga setelah diskon (jika ada): Rp {total_harga}") # Cetak Total Harga yang dibayarkan
