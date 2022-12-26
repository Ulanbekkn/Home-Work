from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    LIFE_STEEL = 5
    SURIKEN = 6
    RESURRECTION = 7


class GameEntity:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None

    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        if hero.health <= 0:
            self.choose_defence(heroes)
        else:
            self.__defence = hero.super_ability

    def hit(self, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.health = hero.health - self.damage

    def __str__(self):
        return f'BOSS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            raise ValueError("Ability must be of type SuperAbility")
        else:
            self.__super_ability = super_ability

    def hit(self, boss):
        boss.health = boss.health - self.damage

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_power(self, boss, heroes):
        pass


class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coefficient = randint(2, 5)
        boss.health = boss.health - self.damage * coefficient
        print(f'Warrior hits critically: {self.damage * coefficient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for i in heroes:
            if i.health > 0 and i.damage != 0:
                i.damage += 5
        print(f'{self.name}: damage of all heroes improved')


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, SuperAbility.HEAL)
        self.__heal_points = heal_points

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0 and self != hero:
                hero.health = hero.health + self.__heal_points
        print(f'{self.name}: all heroes healing + {self.__heal_points} hp')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_power(self, boss, heroes):
        def_dmg = boss.damage // randint(2, 5)
        self.health += def_dmg
        boss.health -= def_dmg
        print(f'{self.name} save and hit: {def_dmg}')


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.LIFE_STEEL)

    def apply_super_power(self, boss, heroes):
        if round_counter % 2 == 0:
            rob_health = 20
            rand_hero = choice(heroes)
            boss.health -= rob_health
            rand_hero.health += rob_health
            print(f'hacker stole and gave to {rand_hero.name} - 20 hp')


class Samurai(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SURIKEN)

    def apply_super_power(self, boss, heroes):
        rand_suriken = randint(1, 2)
        if rand_suriken == 1:
            boss.health -= 10
            print(f'{self.name}\'s suriken type - "virus"')
        else:
            boss.health += 10
            print(f'{self.name}\'s suriken type - "vaccine"')


class Witcher(Hero):
    def __init__(self, name, health, damage=0):
        super().__init__(name, health, damage, SuperAbility.RESURRECTION)

    def apply_super_power(self, boss, heroes):
        for i in heroes:
            if i.health == 0 and self != i:
                i.health += self.health
                self.health = 0
                print(f"{self.name} gives her life to {i.name}")
                break


round_counter = 0


def print_statistics(boss, heroes):
    print()
    print('ROUND ' + str(round_counter) + ' -------------')
    print(boss)
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print('Heroes won!!!')
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print("Boss won!!!")
    return all_heroes_dead


def play_round(boss, heroes):
    global round_counter
    round_counter += 1
    boss.choose_defence(heroes)
    boss.hit(heroes)
    for hero in heroes:
        if boss.defence != hero.super_ability and hero.health > 0 and boss.health > 0:
            hero.hit(boss)
            hero.apply_super_power(boss, heroes)
    print_statistics(boss, heroes)
    print()


def start_game():
    boss = Boss('Rashan', 1900, 50)
    warrior = Warrior('Konor', 280, 10)
    doc = Medic('Hous', 250, 5, 15)
    berserk = Berserk('Hiccup', 260, 15)
    magic = Magic('Invoker', 270, 20)
    assistant = Medic('Morty', 290, 5, 5)
    hacker = Hacker('Ulanbek', 250, 15)
    samurai = Samurai('Aftandil', 300, 30)
    witcher = Witcher('Aidai', 300)
    heroes = [warrior, doc, berserk, magic, assistant, hacker, samurai, witcher]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        play_round(boss, heroes)


start_game()