class Gempa:
    # Konstruktor Inisialisasi atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    # Method Penentu Skala Gempa
    def dampak(self):
        # Logika/Statement
        if self.skala < 2:
            print('Gempa Tidak Berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa Berdampak Bangunan Retak')
        elif 4 <= self.skala <= 6:
            print('Gempa Berdampak Bangunan Roboh')
        elif self.skala > 6:
            print('Gempa Besar Berpotensi Tsunami')

        # Menampilkan Lokasi dan Skala Gempa
        print(f'Lokasi Gempa: {self.lokasi}')
        print(f'Skala Gempa: {self.skala}')