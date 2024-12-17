class Animal:
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    # Method Informasi
    def info_animal(self):
        print("Nama Hewan\t\t: ", self.nama,
              "\nMakanan\t\t\t: ", self.makanan,
              "\nHidup\t\t\t: ", self.hidup,
              "\nBerkembang Biak\t\t: ", self.berkembang_biak)
    
# # Objek
# kucing = Animal("Kucing", "Daging", "Hidup", "Melahirkan")

# kucing.info_animal()
