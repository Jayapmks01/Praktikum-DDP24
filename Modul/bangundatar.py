import math

def l_persegi(sisi):
    luas = sisi*sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas Persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling Persegi adalah {keliling}')
    
def persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    print("hasil luas persegi panjang dari", panjang, "x", lebar, "=", luas)
    
def l_segitiga(alas, tinggi):
    luas = 0.5 * alas * tinggi 
    print(f'Luas Segitiga {0.5} * {alas} * {tinggi} = {alas}')
    
def l_lingkaran(r1, r2):
    luas = 3.14 * r1 *r2
    print(f'Luas Lingkaran ini adalah phi * {r1} *{r2} = {luas}')
    
def l_jajargenjang (alas, tinggi):
    luas = alas * tinggi
    print(f'luas jajargenjang {alas} * {tinggi} = {luas}')
    