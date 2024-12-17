from Animal import Animal

class Bird(Animal):
    # Konstruktor Properti
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna, paruh):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna = warna
        self.paruh = paruh
        
    # Method Info
    def info_bird(self):
        super().info_animal()
        print("Warna\t\t\t: ", self.warna,
              "\nJenis Paruh\t\t: ", self.paruh)

# Objek 1
print()
bird = Bird("Elang", "Daging", "Ditebing", "Menghasilkan telur", "Coklat", "Bengkok dan Lancip")
print("=============================================")
print("## Info Bird ##")
bird.info_bird()

# Objek 2
print()
bird1 = Bird("Pelatuk", "Biji-Bijian", "Pohon", "Menghasilkan telur", "Hitam", "Lancip")
print("=============================================")
print("## Info Bird ##")
bird1.info_bird()

