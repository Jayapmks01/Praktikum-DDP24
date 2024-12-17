from Animal import Animal

class Fish(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, bernapas, habitat):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bernapas = bernapas
        self.habitat = habitat
        
    def info_fish(self):
        super().info_animal()
        print("Bernapas menggunakan\t: ", self.bernapas,
              "\nHabitat Di\t\t: ", self.habitat)
        
# Objek 1
print()
fish = Fish("Hiu", "Daging", "Laut", "Melahirkan", "Insang", "Air Asin")
print("=============================================")
print("## Info Fish ##")
fish.info_fish()

# Objek 2
print()
fish1 = Fish("Lumba-Lumba", "Daging", "Laut", "Melahirkan", "Insang", "Air Asin")
print("=============================================")
print("## Info Fish ##")
fish1.info_fish()