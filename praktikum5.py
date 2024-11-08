print()
print('------------------------')
print('Soal Nomor 1.')
# Nomer 1

kendaraan = ['motor', 'ninja', 250, 'merah', 2]
print(kendaraan)

kendaraan = ['motor', 'ninja', 250, 'merah', 2]
kendaraan.append('250 Juta')
print(kendaraan)

kendaraan = ['motor', 'ninja', 250, 'merah', 2]
kendaraan.append('250 Juta')
kendaraan.append('Kopling')
print(kendaraan)

kendaraan = ['motor', 'ninja', 250, 'merah', 2]
kendaraan.append('250 Juta')
kendaraan.append('Kopling')
kendaraan.insert(2,'Kawasaki')
print(kendaraan)

print()
print('------------------------')
print('Soal Nomor 2.')
# Nomer 2

print ("""Selamat datang di aplikasi menghitung luas
bangun datar. Silahkan pilih salah satu menu dibawah ini:
1. Menghitung Luas persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
""")

pilihan = int(input('Masukan pilihan kamu: '))

match pilihan:
    case 1:
        print('Kamu memilih 1, Menghitung Luas Persegi')
        sisi = int(input('Masukan Sisi Persegi: '))
        Lpersegi = sisi * sisi
        print ('Luas Persegi dengan', sisi, 'adalah', Lpersegi)
    case 2:
        print('Kamu memilih 2, Menghitung Luas Lingkaran')
        r = float(input('Masukan Jari-jari Linkaran: '))
        Llingkaran = 3.14 * r * r
        print ('Luas Lingkaran dengan', r, 'adalah', int(Llingkaran))
    case 3:
        print('Kamu memilih 3, Menghitung Luas Segitiga')
        alas = int(input('Masukan Alas Segitiga: '))
        tinggi = int(input('Masukan Tinggi Segitiga: '))
        Lsegitiga= 1/2 * alas * tinggi
        print ('Luas Segitiga adalah', int(Lsegitiga))
    case _:
        print('Kamu salah memasukan pilihan')

print()