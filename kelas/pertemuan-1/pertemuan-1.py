# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price
        
#     def show_info(self):
#         print(f"Brand: {self.brand}")
#         print(f"Price: {self.price}")
        
#     def change_price(self, new_price):
#         self.price = new_price
        

# asus = Laptop("Asus", "10000000")
# asus.show_info()

# class Tim:
#     nama_liga = "MPL Indonesia"
    
#     def __init__(self, nama, ceo):
#         self.nama = nama
#         self.ceo = ceo

# rrq = Tim("RRQ Hoshi", "Pak AP")
# evos = Tim("Evos Legends", "Hartman Harris")
# alter_ego = Tim("Alter Ego", "Koh Delwyn")

# print(f"{rrq.nama} (CEO: {rrq.ceo}) - Liga: {Tim.nama_liga}\n")
# print(f"{evos.nama} (CEO: {evos.ceo}) - Liga: {Tim.nama_liga}\n")
# print(f"{alter_ego.nama} (CEO: {alter_ego.ceo}) - Liga: {Tim.nama_liga}\n")

# rrq.ceo = "Pak AP Manullang"

# print(f"{rrq.nama} (CEO: {rrq.ceo}) - Liga: {Tim.nama_liga}\n")
# Tim.nama_liga = "MPL Indonesia Season 15"

# print(f"{rrq.nama} (CEO: {rrq.ceo}) - Liga: {Tim.nama_liga}\n")
# print(f"{evos.nama} (CEO: {evos.ceo}) - Liga: {Tim.nama_liga}\n")
# print(f"{alter_ego.nama} (CEO: {alter_ego.ceo}) - Liga: {Tim.nama_liga}\n")

# class Pertandingan:
#     def __init__(self, tim_a, tim_b):
#         self.tim_a = tim_a
#         self.tim_b = tim_b
#         self.skor_a = 0
#         self.skor_b = 0
#         self.selesai = False
        
#     def tambah_skor(self, tim, poin=1):
#         if tim == self.tim_a:
#             self.skor_a += poin
#         elif tim == self.tim_b:
#             self.skor_b += poin
#         else:
#             print(f"{tim} tidak terdaftar di pertandingan ini!")
        
#     def selesaikan(self):
#         self.selesai = True
        
#     def tampilkan_hasil(self):
#         status = "Selesai" if self.selesai else "Berlangsung"
#         print(f"{self.tim_a} {self.skor_a} - {self.skor_b} {self.tim_b}({status})")

# final = Pertandingan("RRQ", "Evos Legends")
# final.tambah_skor("RRQ", 2)
# final.tambah_skor("Evos Legends", 1)
# final.selesaikan()
# final.tampilkan_hasil() # RRQ 2 - 1 Evos Legends (Selesai)

# class Jadwal:
#     musim_liga = "MPL Indonesia Season 14"
#     def __init__(self, tim_a, tim_b, tanggal):
#         self.tim_a = tim_a
#         self.tim_b = tim_b
#         self.tanggal = tanggal
    
#     # Class method sebagai factory method -- buat objek dari dictionary
#     @classmethod    
#     def dari_dict(cls, data):
#         """Alternatif konstruktor: buat Jadwal dari data berbentuk
#         dictionary."""
#         return cls(data["tim_a"], data["tim_b"], data["tanggal"])
    
#     @classmethod
#     def ganti_musim(cls, musim_baru):
#         """Mengubah musim liga aktif, berlaku untuk seluruh objek
#         Jadwal."""
#         cls.musim_liga = musim_baru
        
#     def info(self):
#         print(f"{self.tim_a} vs {self.tim_b} - {self.tanggal}({Jadwal.musim_liga})\n")

# data_laga = {"tim_a": "RRQ", "tim_b": "Evos Legends", "tanggal": "12 September 2026"}
# data_laga2 = {"tim_a": "ONIC", "tim_b": "Alter Ego", "tanggal": "13 September 2026"}
# laga1 = Jadwal.dari_dict(data_laga)
# laga2 = Jadwal.dari_dict(data_laga2)
# laga1.info() # RRQ vs Evos Legends - 12 September 2026 (MPL Indonesia Season 14)
# laga2.info() # ONIC vs Alter Ego - 13 September 2026 (MPL Indonesia Season 14)

# Jadwal.ganti_musim("MPL Indonesia Season 15")
# laga1.info() # RRQ vs Evos Legends - 12 September 2026 (MPL Indonesia Season 15)
# laga2.info() # ONIC vs Alter Ego - 13 September 2026 (MPL Indonesia Season 15)

# class UtilitasPertandingan:
#     @staticmethod
#     def validasi_nama_tim(nama_tim):
#         tim_terdaftar = ["RRQ", "Evos Legends", "Alter Ego", "ONIC"]
#         return nama_tim in tim_terdaftar

#     @staticmethod
#     def tentukan_pemenang(tim_a, skor_a, tim_b, skor_b):
#         if skor_a > skor_b:
#             return tim_a
#         elif skor_b > skor_a:
#             return tim_b
#         return "Seri"

# print(UtilitasPertandingan.validasi_nama_tim("RRQ")) # True
# print(UtilitasPertandingan.validasi_nama_tim("Team Baru")) # False
# print(UtilitasPertandingan.tentukan_pemenang("RRQ", 2, "Evos Legends", 1)) # RRQ

#Kode Secara Keseluruhan
class Pertandingan:
    musim_liga = "MPL Indonesia Season 14"
    def __init__(self, tim_a, tim_b):
        self.tim_a = tim_a
        self.tim_b = tim_b
        self.skor_a = 0
        self.skor_b = 0
        self.selesai = False
        
    def tambah_skor(self, tim, poin=1):
        if tim == self.tim_a:
            self.skor_a += poin
        elif tim == self.tim_b:
            self.skor_b += poin
        else:
            print(f"{tim} tidak terdaftar di pertandingan ini!")
    
    def selesaikan(self):
        self.selesai = True
        
    def tampilkan_hasil(self):
        status = "Selesai" if self.selesai else "Berlangsung"
        print(f"{self.tim_a} {self.skor_a} - {self.skor_b} {self.tim_b} "
        f"({status}, {Pertandingan.musim_liga})")

    @classmethod
    def dari_dict(cls, data):
        return cls(data["tim_a"], data["tim_b"])
    
    @classmethod
    def ganti_musim(cls, musim_baru):
        cls.musim_liga = musim_baru
        
    @staticmethod
    def validasi_nama_tim(nama_tim):
        tim_terdaftar = ["RRQ", "Evos Legends", "Alter Ego", "ONIC"]
        return nama_tim in tim_terdaftar

    @staticmethod
    def tentukan_pemenang(tim_a, skor_a, tim_b, skor_b):
        if skor_a > skor_b:
            return tim_a
        elif skor_b > skor_a:
            return tim_b
            return "Seri"

print(Pertandingan.validasi_nama_tim("RRQ"))
print(Pertandingan.validasi_nama_tim("Team Baru"))

final = Pertandingan("RRQ", "Evos Legends")
final.tambah_skor("RRQ", 2)
final.tambah_skor("Evos Legends", 1)
final.selesaikan()
final.tampilkan_hasil()

data_laga = {"tim_a": "ONIC", "tim_b": "Alter Ego"}
laga2 = Pertandingan.dari_dict(data_laga)
laga2.tambah_skor("ONIC", 2)
laga2.tampilkan_hasil()

Pertandingan.ganti_musim("MPL Indonesia Season 15")
final.tampilkan_hasil()
laga2.tampilkan_hasil()
pemenang = Pertandingan.tentukan_pemenang("RRQ", final.skor_a, "Evos Legends", final.skor_b)
print(f"Pemenang: {pemenang}")