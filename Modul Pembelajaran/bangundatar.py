import math

# Deklarasi
def persegi(sisi): 
    hasil = sisi * sisi 
    print('Luas Persegi adalah ', hasil)
    
def persegi_panjang(p, l): 
    hasil = p * l 
    print('Luas Persegi Panjang adalah ', hasil)
    
def lingkaran(r): 
    hasil = math.pi * r * r 
    print('Luas Lingkaran adalah ', hasil)
    
def segitiga(a, t): 
    hasil = 1/2 * a * t 
    print('Luas Segitiga adalah ', hasil)
    
def belah_ketupat(d1, d2): 
    hasil = 1/2 * d1 * d2 
    print('Luas Belah Ketupat adalah ', hasil)