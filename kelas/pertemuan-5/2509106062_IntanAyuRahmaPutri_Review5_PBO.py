class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def serang(self, target):
        target.health -= self.attack
        print(f"{self.name} menyerang {target.name}")


class Mage(Hero):
    def __init__(self, name, health, attack, mana):
        super().__init__(name, health, attack)
        self.mana = mana

    def serang(self, target):
        target.health -= self.attack
        print(f"{self.name} menyerang {target.name} dengan magis")


class Assasin(Hero):
    def __init__(self, name, health, attack, critical_chance):
        super().__init__(name, health, attack)
        self.critical_chance = critical_chance


class AssasinEnergy(Assasin):
    def __init__(self, name, health, attack, critical_chance, energy):
        super().__init__(name, health, attack, critical_chance)
        self.energy = energy

    def serang(self, target):
        target.health -= self.attack
        print(f"{self.name} menyerang {target.name} dengan energi")


class DoubleRole(Assasin, Mage):
    def __init__(self, name, health, attack, critical_chance, mana, jarak):
        Hero.__init__(self, name, health, attack)
        self.critical_chance = critical_chance
        self.mana = mana
        self.jarak = jarak

    def serang(self, target, jarak):
        if jarak < 50:
            target.health -= self.attack
            print(f"{self.name} menyerang {target.name} dengan jarak dekat")
        else:
            target.health -= self.attack
            print(f"{self.name} menyerang {target.name} dengan ")

Balmond = Hero("Balmond", 100, 10)
Eudora = Hero("Eudora", 100, 15)
Balmond.serang(Eudora)

Lylia = Mage("Lylia", 100, 10, 20)
Odette = Mage("Odette", 100, 15, 30)
Lylia.serang(Odette)

Karina = Assasin("Karina", 100, 20, 0.3)
Fanny = AssasinEnergy("Fanny", 100, 25, 0.4, 50)
Fanny.serang(Karina)

Aamon = DoubleRole("Aamon", 100, 30, 0.5, 100, 40)
Selena = DoubleRole("Selena", 100, 35, 0.6, 150, 60)
Aamon.serang(Selena, 40)