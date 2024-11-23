print()
print('## Nomor 1 ##')
# Definisi Fungsi celcius_ke_fahrenheit yang menerima satu Parameter (Parameter celcius adalah suhu yang mewakili suhu celcius.)
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32 # Mengkonversi Suhu dari celcius ke Fahrenheit
    return fahrenheit # Mengembalikan nilai Fahrenheit

# Fungsi cek_kelulusan dipanggil dengan argumen 80.
print(f'Suhu Celcius 0 Sama Dengan {celcius_ke_fahrenheit(0)}') # Cetak dan Memanggil Fungsi
print(f'Suhu Celcius 100 Sama Dengan {celcius_ke_fahrenheit(100)}') # Cetak dan Memanggil Fungsi

print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0 # Menentukan bilangan ganjil atau genap
    return hitung # Mengembalikan nilai hitung

print(f'Bilangan 4 Genap? {genap_ganjil(4)}') # Cetak dan Memanggil Fungsi
print(f'Bilangan 7 Genap? {genap_ganjil(7)}') # Cetak dan Memanggil Fungsi

print()
print('## Nomor 3 ##')

# Definisi Fungsi cek_kelulusan yang menerima satu Parameter (Parameter nilai adalah angka yang mewakili nilai seseorang.)
def cek_kelulusan(nilai): 
    # Logika Pengambilan Keputusan
    if nilai > 60:
        return 'Lulus'
    else:
        return 'Gagal'


print(f'Nilai: 80, Status: {cek_kelulusan(80)}') # Cetak dan Memanggil Fungsi
print(f'Nilai: 60, Status: {cek_kelulusan(60)}') # Cetak dan Memanggil Fungsi

print()
print('## Nomor 4 ##')
def bilangan_ganjil(number):
    for a in range(1, number, 2): # 1, 3, 5.. 19
        print(a, end=" ") # 1, 3, 5.. 19

bilangan_ganjil(20)