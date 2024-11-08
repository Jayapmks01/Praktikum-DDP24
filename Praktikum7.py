# Soal UTS Nomor 1
print('=== 1. Program Pemesanan ===')
nama = input('Masukan Nama Kamu: ')
no_hp = input('Masukan Nomer Telpon Kamu: ')
pesanan = input("""Masukan Kategori Pesanan Kamu =  
1. Makanan
2. Minuman
(Pilih 1 atau 2):  """) 
print()

if pesanan == '1':
    print('Kamu memilih menu makanan')
    menu = int(input("""Masukan Pilihan Menu = 
    1. Nasi Goreng - 15000
    2. Mie Goreng - 12000
    3. Ayam Geprek - 18000 
    (Pilih 1, 2, 3): """))
    print()
    if menu == 1:
        print('=== Kamu Memilih Menu Makanan Nasi Goreng ===')
        harga = 15000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Nasi Goreng dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    elif menu == 2:
        print('=== Kamu Memilih Menu Makanan Mie Goreng ===')
        harga = 12000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Mie Goreng dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    elif menu == 3:
        print('=== Kamu Memilih Menu Makanan Ayam Geprek ===')
        harga = 18000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Ayam Geprek dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    else:
        print('Tidak ada menu pilihan, Silahkan Ulangi!')
elif pesanan == '2':
    print('=== Kamu Memilih Menu Minuman ===')
    menu = int(input("""Masukan Pilihan Menu = 
    1. Es Teh Manis - 5000
    2. Good Day - 6000
    3. Es Jeruk - 6000 
    (Pilih 1, 2, 3): """))
    print()
    if menu == 1:
        print('=== Kamu Memilih Menu Minuman Es Teh Manis ===')
        harga = 5000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    elif menu == 2:
        print('=== Kamu Memilih Menu Minuman Good Day ===')
        harga = 6000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    elif menu == 3:
        print('=== Kamu Memilih Menu Minuman Es Jeruk ===')
        harga = 6000
        # uang = int(input('Masukan Uang Kamu: '))
        jumlah_pesanan = int(input('Masukan Jumlah Pesanan: '))
        pembayaran = harga*jumlah_pesanan
        # kembalian = uang - pembayaran
        print("Nota : Pemesanan atas nama", nama, "dengan nomor handphone", no_hp, "memilih menu pesanan", menu, "yaitu Es Teh Manis dengan jumlah pesanan", jumlah_pesanan, "dan jumlah pembayaran yang harus dibayarkan berjumlah", pembayaran)
        # print('Uang Kembalian: ', kembalian)
    else:
        print('Tidak ada menu pilihan, Silahkan Ulangi!')
else:
    print('Masukan Kata Dengan Benar!')

print()
# Soal UTS Nomor 2
print('=== 2. Program Perjalanan ===')
nama_kendaraan = input('Masukan Nama Kendaraan Kamu: ') # Motor
jenis_bensin = input('Masukan Jenis Bensin: ') .lower() # Pertamax

match jenis_bensin:
    case 'pertalite':
        print('Bensin Yang Kamu Gunakan Adalah Pertalite')
        harga_bensin = 10000
        jarak_bensin = 12
        kota_tujuan = input('Masukan Kota Tujuan: ').lower()
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
            pemakaian_bensin = jarak_kota / jarak_bensin
            total_harga = pemakaian_bensin * harga_bensin
            print()
            print('Rincian Kendaraan dan Biaya Perjalanan Menuju Bekasi Adalah: ')
            print('Nama Kendaraan: ', nama_kendaraan)
            print('Jenis Bensin: ', jenis_bensin)
            print('Kota Tujuan: ', kota_tujuan)
            print('Pemakaian Bensin: ', "{:.2f}".format(pemakaian_bensin), 'Liter')
            print('Total Harga: ', "{:.2f}".format(total_harga), 'Rupiah')
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

print()
# Soal UTS Nomor 3
print('=== 3. Program Perhitungan Kelipatan 3 ===')

for i in range(1, 20):
  if i % 3 == 0:
    print('Nurul Fikri')
  else:
    print(i)
