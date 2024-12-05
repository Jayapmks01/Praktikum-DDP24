import operator_hitung

print()
print('## Penjumlahan ##')
bil1 = int(input('Masukan Bilangan 1: '))
bil2 = int(input('Masukan Bilangan 2: '))
operator_hitung.tambah(bil1, bil2)

print()
print('## Pengurangan ##')
bil1 = int(input('Masukan Bilangan 1: '))
bil2 = int(input('Masukan Bilangan 2: '))
operator_hitung.kurang(bil1, bil2)

print()
print('## Perkalian ##')
bil1 = int(input('Masukan Bilangan 1: '))
bil2 = int(input('Masukan Bilangan 2: '))
operator_hitung.kali(bil1, bil2)

print()
print('## Pembagian ##')
bil1 = int(input('Masukan Bilangan 1: '))
bil2 = int(input('Masukan Bilangan 2: '))
operator_hitung.bagi(bil1, bil2)

print()
print('## Pangkat ##')
bil1 = int(input('Masukan Bilangan 1: '))
bil2 = int(input('Masukan Bilangan 2: '))
operator_hitung.pangkat(bil1, bil2)


print()
print('====================')
import bangundatar

print()
print('## Luas Persegi ##')
sisi = int(input('Masukan Sisi Persegi: ')) 
bangundatar.persegi(sisi)

print()
print('## Luas Persegi Panjang ##')
p = int(input('Masukan Bilangan 1: ')) 
l = int(input('Masukan Bilangan 2: ')) 
bangundatar.persegi_panjang(p, l)

print()
print('## Luas Lingkaran ##')
r = int(input('Masukan Jari- Jari Linkaran: ')) 
bangundatar.lingkaran(r)

print()
print('## Luas Segitiga ##')
a = int(input('Masukan Bilangan 1: ')) 
t = int(input('Masukan Bilangan 2: ')) 
bangundatar.segitiga(a, t)

print()
print('## Luas Belah Ketupat ##')
d1 = int(input('Masukan Bilangan 1: ')) 
d2 = int(input('Masukan Bilangan 2: ')) 
bangundatar.belah_ketupat(d1, d2)

print()
print('====================')
import bangunruang

print()
print('## Luas Kubus ##')
sisi = int(input('Masukan Sisi Kubus: ')) 
bangunruang.kubus(sisi)

print()
print('## Luas Balok ##')
p = int(input('Masukan Bilangan 1: ')) 
l = int(input('Masukan Bilangan 2: ')) 
t = int(input('Masukan Bilangan 3: ')) 
bangunruang.belah_ketupat(p, l, t)