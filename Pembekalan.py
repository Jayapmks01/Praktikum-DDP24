# # 1. Program Perhitungan Jarak Tempuh Kendaraan
# print('=== Program Perhitungan Jarak tempuh ===')
# nama_kendaraan = input('Masukkan Jenis Kendaraan: ')
# jenis_bensin = input('Masukkan Jenis Bensin: ') 

# match jenis_bensin:
#     case 'pertalite':
#         print('Bensin yang kamu gunakan adalah pertalite')
#         harga_bensin = 10000
#         jarak_tempuh = 12
#         kota_tujuan = input('Masukkan Kota Tujuan: ').lower() 
#         if kota_tujuan == 'jakarta':
#             print('Kota Tujuan Kamu Adalah Jakarta')
#             jarak = 20
#             pemakaian_bensin = jarak / jarak_tempuh
#             total_harga = pemakaian_bensin * harga_bensin
#             print()
#             print('Rincian kendaraan dan Biaya Perjalanan Menuju Jakarta Adalah: ')
#             print('Nama Jenis Kendaraan', nama_kendaraan)
#             print('Jenis Bensin', jenis_bensin)
#             print('Kota Tujuan', kota_tujuan)
#             print('Pemakaian Bensin', "{:.2f}".format(pemakaian_bensin), 'Liter')
#             print('Total Harga', "{:.2f}".format(total_harga), 'Rupiah')
#             print(f'Kamu memilih bensin {jenis_bensin}')
#         elif kota_tujuan == 'bogor':
#             print('Kota Tujuan Kamu Adalah Bogor')
#         else:
#             print('Kota Tujuan Tidak Ditemukan')
#     case 'pertamax':
#         print('Bensin Yang Kamu Gunakan Adalah Pertamax')
#     case _:
#         print('Jenis Bensin Tidak Ditemukan!')

print()
# # 2. Program Pemesanan Makanan dan Minuman
print('=== Program Pemesanan Makanan dan Minuman ===')

nama = input('Masukkan Nama Anda: ')
no_hp = input('Masukkan Nomor HP Anda: ')
pesanan = input("""Masukkan Kategori Pesanan Kamu: 
1. Makanan
2. Minuman
(Pilih 1 Atau 2): """)

if pesanan == '1':
    print('Anda memilih menu makanan')
    menu = int(input("""Masukkan Pilihan Menu: 
                     1. Nasi Goreng - 15.000
                     2. Mie Goreng - 12.000
                     3. Ayam Geprek - 18.000
                     (Pilih 1, 2, 3): """))
    if menu == 1:
        print('=== Anda Memilih Menu Makanan Nasi Goreng')
        harga = 15000
        jml_pesanan = int(input('Masukkan Jumlah Pesanan Anda: '))
        pembayaran = harga * jml_pesanan
        print(f'Nota: Pemesanan Atas Nama {nama} dengan Nomor HP {no_hp} memilih pesanan {menu} yaitu Nasi Goreng dengan jumlah pesanan {jml_pesanan} dan jumlah pembayaran yang harus dibayarkan adalah {pembayaran}')
    elif menu == 2:
        print('=== Anda Memilih Menu Makanan Mie Goreng')
        harga = 12000
        jml_pesanan = int(input('Masukkan Jumlah Pesanan Anda: '))
        pembayaran = harga * jml_pesanan
        print(f'Nota: Pemesanan Atas Nama {nama} dengan Nomor HP {no_hp} memilih pesanan {menu} yaitu Nasi Goreng dengan jumlah pesanan {jml_pesanan} dan jumlah pembayaran yang harus dibayarkan adalah {pembayaran}')
    else:
        print('Masukkan Kata Dengan Benar!')



# 3. Program Bilangan Kelipatan 3
# print('=== Program Bilangan Kelipatan 3 ===')
# for i in range(1, 20):
#     if i % 3 == 0:
#         print('STT Nurul Fikri')
#     else:
#         print(i)