# Soal UTS Nomor 1
# print('=== 1. Program Pemesanan ===')
# nama = input('Masukan Nama Kamu: ') # Lia
# no_hp = input('Masukan Nomer Telpon Kamu: ') # 08678652456
# pesanan = input("""Masukan Kategori Pesanan Kamu =  
# 1. Makanan
# 2. Minuman
# (Pilih 1 atau 2):  """) # 1
# print()

# if pesanan == '1':
#     print('Kamu memilih menu makanan')
#     menu = int(input("""Masukan Pilihan Menu = 
#     1. Nasi Goreng - 15000
#     2. Mie Goreng - 12000
#     3. Ayam Geprek - 18000 
#     (Pilih 1, 2, 3): """)) # 1
#     print()
#     if menu == 1:
#         print('=== Kamu Memilih Menu Makanan Nasi Goreng ===')
#         harga = 15000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: ')) # 4
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Nasi Goreng dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     elif menu == 2:
#         print('=== Kamu Memilih Menu Makanan Mie Goreng ===')
#         harga = 12000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Mie Goreng dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     elif menu == 3:
#         print('=== Kamu Memilih Menu Makanan Ayam Geprek ===')
#         harga = 18000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Ayam Geprek dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     else:
#         print('Tidak ada menu pilihan, Silahkan Ulangi!')
# elif pesanan == '2':
#     print('=== Kamu Memilih Menu Minuman ===')
#     menu = int(input("""Masukan Pilihan Menu = 
#     1. Es Teh Manis - 5000
#     2. Good Day - 6000
#     3. Es Jeruk - 6000 
#     (Pilih 1, 2, 3): """))
#     print()
#     if menu == 1:
#         print('=== Kamu Memilih Menu Minuman Es Teh Manis ===')
#         harga = 5000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     elif menu == 2:
#         print('=== Kamu Memilih Menu Minuman Good Day ===')
#         harga = 6000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     elif menu == 3:
#         print('=== Kamu Memilih Menu Minuman Es Jeruk ===')
#         harga = 6000
#         # uang = int(input('Masukan Uang Kamu: '))
#         jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
#         pembayaran = harga*jumlah_pesanan
#         # kembalian = uang - pembayaran
#         print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
#         # print('Uang Kembalian: ', kembalian)
#     else:
#         print('Tidak ada menu pilihan, Silahkan Ulangi!')
# else:
#     print('Masukan Kata Dengan Benar!')

print()
# Soal UTS Nomor 2
print('=== 2. Program Perjalanan ===')
nama_kendaraan = input('Masukan Nama Kendaraan Kamu: ') # Mobil
jenis_bensin = input('Masukan Jenis Bensin: ') .lower() # Pertalite

match jenis_bensin: # Pertalite
    case 'pertalite':
        print('Bensin Yang Kamu Gunakan Adalah Pertalite')
        harga_bensin = 10000
        jarak_bensin = 12
        kota_tujuan = input('Masukan Kota Tujuan: ').lower() # Bekasi
        if kota_tujuan == 'jakarta':
            print('Kota Tujuan Kamu Adalah Jakarta')
            jarak_kota = 20
            pemakaian_bensin = jarak_kota / jarak_bensin
            total_harga = pemakaian_bensin * harga_bensin
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Jakarta Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan)
            print('Jenis Bensin: ', jenis_bensin)
            print('Kota Tujuan: ', kota_tujuan)
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter')
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah')
        elif kota_tujuan == 'bekasi':
            print('Kota Tujuan Kamu Adalah Bekasi')
            jarak_kota = 35.7
            pemakaian_bensin = jarak_kota / jarak_bensin # 35.7 / 12 = 2.97 Liter 
            total_harga = pemakaian_bensin * harga_bensin # 2.97 * 10000 = 29.700 Rupiah
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Bekasi Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan) # Mobil
            print('Jenis Bensin: ', jenis_bensin) # Pertalite
            print('Kota Tujuan: ', kota_tujuan) # Bekasi
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter') # 2.97 Liter
            # print('Pemakaian Bensin: ', pemakaian_bensin, 'Liter') # 2.97 Liter
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah') # 29.700
        elif kota_tujuan == 'depok':
            print('Kota Tujuan Kamu Adalah Depok')
            jarak_kota = 99
            pemakaian_bensin = jarak_kota / jarak_bensin
            total_harga = pemakaian_bensin * harga_bensin
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Depok Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan)
            print('Jenis Bensin: ', jenis_bensin)
            print('Kota Tujuan: ', kota_tujuan)
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter')
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah')
        else:
            print('Masukan Kata Dengan Benar')
    case 'pertamax':
        print('Bensin Yang Kamu Gunakan Adalah Pertamax')
        harga_bensin = 14000
        jarak_bensin = 13
        kota_tujuan = input('Masukan Kota Tujuan: ').lower() # Bekasi
        if kota_tujuan == 'jakarta':
            print('Kota Tujuan Kamu Adalah Jakarta')
            jarak_kota = 20
            pemakaian_bensin = jarak_kota / jarak_bensin
            total_harga = pemakaian_bensin * harga_bensin
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Jakarta Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan)
            print('Jenis Bensin: ', jenis_bensin)
            print('Kota Tujuan: ', kota_tujuan)
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter')
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah')
        elif kota_tujuan == 'bekasi':
            print('Kota Tujuan Kamu Adalah Bekasi')
            jarak_kota = 35.7
            pemakaian_bensin = jarak_kota / jarak_bensin # 27.4 Liter
            total_harga = pemakaian_bensin * harga_bensin # 383.600
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Bekasi Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan) # Motor
            print('Jenis Bensin: ', jenis_bensin) # Pertamax
            print('Kota Tujuan: ', kota_tujuan) # Bekasi
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter') # 27.4 Liter
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah') # 383.600
        elif kota_tujuan == 'depok':
            print('Kota Tujuan Kamu Adalah Depok')
            jarak_kota = 99
            pemakaian_bensin = jarak_kota / jarak_bensin
            total_harga = pemakaian_bensin * harga_bensin
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Depok Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan)
            print('Jenis Bensin: ', jenis_bensin)
            print('Kota Tujuan: ', kota_tujuan)
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter')
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah')
        else:
            print('Masukan Kata Dengan Benar')
    case _:
        print('Masukan Kata Dengan Benar!')

# print()
# # Soal UTS Nomor 3
# print('=== 3. Program Perhitungan Kelipatan 3 ===')

# for i in range(1, 21):
#   if i % 3 == 0:
#     print('Nurul Fikri')
#   else:
#     print(i)

# a = 1
# while a <= 20:
#     if a % 3 == 0:
#         print('STT Nurul Fikri')
#     else:
#         print(a)
#     a+=1

# print()
# # Program Pemesanan Makanan Dengan Dictionary
# print('=== 4. Program Pemesanan Dictionary ===')
# menu_makanan={
#   "Nasi Goreng":15000,
#   "Mie Goreng":12000,
#   "Ayam Goreng":10000
# }

# menu_minuman={
#   "Es Teh":5000,
#   "Es Jeruk":7000,
#   "Es Kopi":6000
# }

# nama=input("Masukkan nama anda: ")
# no_hp=input("Masukkan nomor handphone anda: ")
# pesan=input("Masukkan pesanan anda (Makanan/Minuman): ").lower()

# harga=0
# if pesan=="makanan":
#   print("Kamu Memesan Menu Makanan")
#   for i in menu_makanan:
#     print(i,menu_makanan[i])
#   pesanan_makanan = input("Masukkan pesanan makanan: ")
#   if pesanan_makanan in menu_makanan:
#     harga += menu_makanan[pesanan_makanan]
#   else:
#     print("Pesanan makanan tidak valid")
    
# elif pesan=="minuman":
#   print("Kamu Memesan Menu Minuman")
#   for i in menu_minuman:
#     print(i,menu_minuman[i])
#   pesanan_minuman = input("Masukkan pesanan minuman: ")
#   if pesanan_minuman in menu_minuman:
#     harga += menu_minuman[pesanan_minuman]
#   else:
#     print("Pesanan minuman tidak valid")
    
# else:
#   print("Pesanan tidak valid")
  
# print("Total biaya: Rp", harga)
