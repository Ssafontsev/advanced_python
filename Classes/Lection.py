from pprint import pprint

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
        self.backpack = []

    def eat(self,food):
        if self.energy < 100:
            self.energy += food
        else:
            print('Not hungry')

    def do_exercise(self, hours):
        if self.energy > 0:
            self.energy -= hours * 2
            self.power += hours *2
        else:
            print('Too tired')

    def change_alias(self, new_alias):
        print(self)
        self.alias = new_alias

    def beat_up(self,foe):
        if not isinstance(foe, Character):
            return
        if foe.power < self.power:
            foe.status = 'defeated'
            self.status = 'winner'
        else:
            print('Retreat')

peter = Character('Peter PArker', 80)
bruce = Character('Bruce Wayne', 85)

bruce.beat_up(peter)

class Person:
    def __init__(self, id):
        self.id = id

some_person = Person(100)
some_person.__dict__['age'] = 30

class Income:
    def __init__(self, id_):
        self.id_ = id_
        id_ = 100
income_1 = Income(1000)

class Character:
    def __init__(self, name, power, energy=100, hands=2):
        self.name = name
        self.power = power
        self.energy = energy
        self.hands = hands
    def move(self):
        print('Moving on 2 squares')

    def attack(self, foe):
        foe.health -= 10

class Spider:
    def __init__(self, power, energy=50, hands=8):
        self.power = power
        self.energy = energy
        self.hands = hands
    def webshoot(self):
        print('Pew-Pew!')
    def move(self):
        self.webshoot()
        print('Moving on 1 square')
    def atack(self, foe):
        foe.status = 'stunned'

class SpiderMan(Character, Spider):
    def __init__(self, name, power):
        super().__init__(name, power)
        self.backpack = []
    def turn_spider_sense(self):
        self.energy -= 10
        self.power += 20
    def webshoot(self):
        if 'web' in self.backpack:
            super().webshoot()
        else:
            print('no web')
    def move(self):
        self.webshoot()
        print('Moving on 3 squares')

    def attack(self, foe):
        super().attack(foe)
        Spider.atack(self, foe)

peter_parker = SpiderMan('Peter Parker', 80)
enemy = Character('Some Enemy', 10)
enemy.health = 100
peter_parker.attack(enemy)

print(enemy.health)
print(enemy.status)