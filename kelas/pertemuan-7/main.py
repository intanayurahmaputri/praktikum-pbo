class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def serang(self, target): # tugas 1: pertarungan
        target.health -= 10
    def tampilkan_status(self): # tugas 2: tampilan
        print(f"{self.name} | HP {self.health}")
    def simpan(self, nama_file): # tugas 3: penyimpanan
        with open(nama_file, "a") as f:
            f.write(f"{self.name},{self.health}\n")

class Hero: # hanya
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def serang(self, target):
        target.health -= 10

class TampilanHero: # hanya tampilan
    def tampilkan(self, hero):
        print(f"{hero.name} | HP {hero.health}")

class PenyimpanHero: # hanya penyimpanan
    def simpan(self, hero, nama_file):
        with open(nama_file, "a") as f:
            f.write(f"{hero.name},{hero.health}\n")

layla = Hero("Layla", 70)
Hero("Balmond", 120).serang(layla)
TampilanHero().tampilkan(layla)
PenyimpanHero().simpan(layla, "data_hero.txt")

def hitung_damage(role, attack):
    if role == "fighter":
        return attack + 5
    elif role == "mage":
        return attack * 2
# role baru = ubah fungsi ini lagi
    return 0

print(hitung_damage("fighter", 10))
print(hitung_damage("mage", 10))
print(hitung_damage("assassin", 10))

class Hero:
    def __init__(self, attack):
        self.attack = attack
    def hitung_damage(self):
        return self.attack

class Fighter(Hero):
    def hitung_damage(self):
        return self.attack + 5
# from abc import ABC, abstractmethod

# class BisaHeal(ABC): # ISP: kemampuan terpisah
#     @abstractmethod
#     def heal(self, target):
#         pass

# class Hero(ABC): # OCP + LSP
#     def __init__(self, name, health, attack):
#         self.name = name
#         self.health = health
#         self.attack = attack
        
#     @abstractmethod
#     def hitung_damage(self):
#         pass
    
# class Fighter(Hero):
#     def hitung_damage(self):
#         return self.attack + 5

# class Support(Hero, BisaHeal):
#     def hitung_damage(self):
#         return self.attack
    
#     def heal(self, target):
#         target.health += 20
        
# class PapanSkorKonsol: # SRP: hanya tampilan
#     def catat(self, pesan):
#         print(f"[ARENA] {pesan}")
        
# class Arena:
#     def __init__(self, papan_skor): # DIP: disuntikkan
#         self.papan_skor = papan_skor
        
#     def adu(self, penyerang, target):
#         target.health -= penyerang.hitung_damage()
#         self.papan_skor.catat(f"{target.name} HP {target.health}")
        
# balmond = Fighter("Balmond", 120, 15)
# estes = Support("Estes", 90, 10)

# arena = Arena(PapanSkorKonsol())
# arena.adu(balmond, estes)
# arena.adu(estes, balmond)