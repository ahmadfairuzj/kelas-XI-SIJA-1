#DAFFIN RAYYAN AL ZAFIR
class Perpustakaan:

    def __init__(self, nama):
        self.nama = nama
        self.__buku = [] 

    def tambah_buku(self, Buku):
        self.__buku.append(Buku)
    def tampilkan_buku(self):
        for Buku in self.__buku:
            print(Buku.info())
    def __str__(self):
        return f"Perpustakaan: {self.nama}"
class Buku: 

    def __init__ (self, judul, penulis):
        self.judul = judul
        self.penulis =  penulis

    def info(self):
        return f"Buku: {self.judul} oleh (self.penulis)"
class BukuFiksi(Buku):

    def __init__(self, judul, penulis, genre):
        super().__init__(judul, penulis)
        self.genre = genre

    def info(self):
        return f"BukuFiksi: {self. judul} oleh {self.penulis}  genre: {self.genre}"
class BukuNonFiksi(Buku):
    def __init__(self, judul, penulis, topik):
        super(). __init__(judul, penulis)
        self.topik = topik
    def info(self):
        return f"Buku Non-Fiksi: {self.judul}cla oleh {self. penulis}, Topik {self.topik}"
perpustakaan = Perpustakaan("Perpustakaan Kota")

Buku1 = BukuFiksi("Harry Potter", "J.K Rowling","Fantasi")
Buku2 = BukuNonFiksi("Sapiens","Yuval Noah Harari", "Sejarah")
    
perpustakaan.tambah_buku(Buku1)
perpustakaan.tambah_buku(Buku2)
print(perpustakaan)
perpustakaan.tampilkan_buku()