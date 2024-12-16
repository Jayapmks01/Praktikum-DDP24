from Gempa import *

# Membuat Objek Gempa dengan Lokasi dan Skala
gempa1 = Gempa('Banten', 1.2)
gempa2 = Gempa('Palu', 6.1)
gempa3 = Gempa('Medan', 4.2)
gempa4 = Gempa('Ternate', 3.5)
gempa5 = Gempa('Mariana', 5.4)

# Info Gempa
print('## Gempa Bumi Info ##')
print()
gempa1.dampak() # Memanggil Method dampak()

print()
print('## Gempa Bumi Info ##')
print()
gempa2.dampak() # Memanggil Method dampak()

print()
print('## Gempa Bumi Info ##')
print()
gempa3.dampak() # Memanggil Method dampak()

print()
print('## Gempa Bumi Info ##')
print()
gempa4.dampak() # Memanggil Method dampak()

print()
print('## Gempa Bumi Info ##')
print()
gempa5.dampak() # Memanggil Method dampak()
