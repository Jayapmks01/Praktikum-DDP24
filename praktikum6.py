print('')
print('Tugas Nomer 1')
print('')

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725,
    547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390,
    984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236,
    375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219,
    918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815,
    67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
    742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440,
    380, 126, 721, 328, 753, 470, 743, 527
]

index = 0 # Mendeklarasikan variabel bernama bilangan menetapkan nilainya menjadi 0
while index < len(numbers): # perulangan while yang akan berulang selama nilai index lebih kecil dari panjang daftar numbers.
    if numbers[index] % 2 != 0: # Memeriksa apakah angka pada posisi index dalam daftar numbers adalah angka ganjil. 
        print(numbers[index], end=(' ')) # Jika True Maka Cetak angka tersebut diikuti spasi (end=(' ')) untuk menjaga output dalam satu baris.
    if numbers[index] == 553:  # Hentikan loop jika angka sama dengan 553
        break # Jika Kondisi true Program Berhenti
    index += 1 # Tambah index 1 pada variabel Index


print()
print('')
print('Nomor 2')
print('')

bilangan = [1,3,5,7,9,11,13,15,17,19] # List Daftar bilangan
hasil = 0 # Variabel untuk menyimpan hasil penjumlahan
for i in bilangan: # Setiap elemen (angka) dalam daftar bilangan diambil satu per satu dan disimpan dalam variabel i.
    hasil += i # Operator += digunakan untuk menambahkan nilai i (angka saat ini dari bilangan) ke variabel hasil.
print('1 + 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 =', hasil) # Hasilnya adalah jumlah dari semua angka dalam daftar bilangan.


print('')
print('Nomer 3')
print('')

value = int(input('Masukan Jumlah Baris: ')) # meminta pengguna untuk memasukkan jumlah baris yang diinginkan 
for a in range (value): # Variabel a dimulai dari 0 dan akan berlanjut hingga kurang dari value.
    for b in range(a+1): # menentukan jumlah bintang yang dicetak pada setiap baris. baris a, jumlah iterasi pada loop b adalah a + 1
        print(' *', end='') # Baris ini mencetak simbol bintang (*) dengan spasi di depannya
    print()


baris = int(input("Masukkan jumlah baris: "))
for i in range(1, baris + 1):
    for j in range(1, baris - i + 1):
        print(" ", end="")
    for j in range(1, 2 * i):
        print("*", end="")
    print()