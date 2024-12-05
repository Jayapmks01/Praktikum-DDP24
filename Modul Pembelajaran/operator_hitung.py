import math

# Deklarasi
def tambah(bil1, bil2):
    hasil = bil1 + bil2 
    print(f'Hasil Penjumlahan {bil1} + {bil2} = {hasil}')
    
def kurang(bil1, bil2):
    hasil = bil1 - bil2 
    print(f'Hasil Pengurangan {bil1} - {bil2} = {hasil}')
    
def bagi(bil1, bil2):
    hasil = bil1 / bil2 
    print(f'Hasil Pembagian {bil1} / {bil2} = {hasil}')
    
def kali(bil1, bil2):
    hasil = bil1 * bil2 
    print(f'Hasil Perkalian {bil1} * {bil2} = {hasil}')

def pangkat(bil1, bil2):
    hasil = math.pow(bil1, bil2)
    print(f'Hasil Pangkat {bil1} " {bil2} = {hasil}')

