from __future__ import annotations
from typing import List
from abc import abstractmethod


class Combatant(object):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int) -> None:
        self.name, self.__health, self.__strength, self.__defense, self.__ranged, self.__magic, self.__maxHealth = name, health, strength, defense, ranged, magic, health

    @abstractmethod
    def calculatePower(self) -> int:
        pass

    def attackEnemy(self, enemy: Combatant) -> None:
        damage = self.calculatePower()
        print("{} attacks for {} damage!".format(self.name, damage))
        enemy.takeDamage(damage)

    def takeDamage(self, damage: int) -> None:
        real_damage = damage - self.__defense
        self.__health -= real_damage
        print("{}'s defence level blocked {} damage".format(self.name, self.__defense))
        if self.__health > 0:
            print("{} took {} damage and has {} health remaining ".format(self.name, real_damage, self.__health))
        else:
            print("{} has been knocked out!".format(self.name))

    def resetValues(self):
        self.__health = self.__maxHealth

    def getMaxHealth(self) -> int:
        return self.__maxHealth

    def getHealth(self) -> int:
        return self.__health

    def setHealth(self, hp: int):
        pass

    health = property(fget=getHealth, fset=setHealth)

    def getStrength(self) -> int:
        return self.__strength

    def getDefencese(self) -> int:
        return self.__defense

    def getRanged(self) -> int:
        return self.__ranged

    def getMagic(self) -> int:
        return self.__magic

    def details(self) -> str:
        pass
        # return f"{}{}{}"


class Mage(Combatant):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged)
        self._mana = self.getMagic()
        self._regenRate = self.getMagic() // 4

    def resetValues(self):
        super().resetValues()
        self._mana = self.getMagic()

    def calculatePower(self) -> int:
        return self.castSpell()

    @abstractmethod
    def castSpell(self):
        pass


class PyroMage(Mage):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged)
        self.__flameBoost: int = 1

    def castSpell(self):

        # (Strength level * flameBoost ) + bonus damage
        if self._mana >= 40:
            self.castSuperHeat()
            return self.getStrength() * self.__flameBoost
        elif 10 <= self._mana < 40:
            return (self.getStrength() * self.__flameBoost) + (self.castFireBlast())
        else:
            return self.getStrength() * self.__flameBoost

    def castFireBlast(self) -> int:
        print("{} casts Fire Blast!".format(self.name))
        self._mana -= 10
        self._mana += self._regenRate
        return 10


    def castSuperHeat(self):
        # mini the mana and add flameBoost
        self._mana += self._regenRate
        print("{} casts SuperHeat! ".format(self.name))
        self._mana -= 40
        self.__flameBoost += 1



class FrostMage(Mage):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged)
        self.__iceBlock: bool = False

    def takeDamage(self, damage: int) -> None:
        self._mana += self._regenRate
        if self.__iceBlock:
            print("{} ice block absorbed all the damage!\nIce block has faded ".format(self.name))
            self.__iceBlock = False
        else:
            super().takeDamage(damage)

    def castSpell(self) -> int:
        # (Magic level / 4) + bonus
        if self._mana >= 50:
            self.iceBlock()
            return self.getMagic() // 4
        elif 10 <= self._mana < 50:
            return (self.getMagic() // 4)  + self.iceBarrage()

    def iceBarrage(self) -> int:
        self._mana -= 10
        return 30

    def iceBlock(self):
        print("{} casts Ice Block! ".format(self.name))
        self._mana -= 50
        self.__iceBlock = True


class Ranger(Combatant):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged)
        self.__arrow: int = 3

    def calculatePower(self) -> int:
        if self.__arrow > 0:
            print("进入")
            self.__arrow -= 1
            return self.getRanged()

        else:
            return self.getStrength()

    def resetValues(self) -> None:
        super().resetValues()
        self.__arrow = 3


class Warrior(Combatant):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int,
                 armourValue: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged)
        self.__armourValue: int = armourValue

    def takeDamage(self, damage: int) -> None:
        if self.__armourValue > 0:
            if damage > self.__armourValue:
                damage -= self.__armourValue
                self.__armourValue = 0
                print("{}'s armour blocked {} damage\nArmour shattered!".format(self.name, self.__armourValue))
                super().takeDamage(damage)
            else:
                self.__armourValue -= damage
                print("{}'s armour blocked {} damage".format(self.name, damage))

    def calculatePower(self) -> int:
        pass

    def resetValues(self) -> None:
        pass


class Dharok(Warrior):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int,
                 armourValue: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged, armourValue)

    def calculatePower(self) -> int:
        pass


class Guthans(Warrior):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int,
                 armourValue: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged, armourValue)

    def calculatePower(self) -> int:
        pass


class Karil(Warrior):
    def __init__(self, name: str, health: int, strength: int, defense: int, magic: int, ranged: int,
                 armourValue: int) -> None:
        super().__init__(name, health, strength, defense, magic, ranged, armourValue)

    def calculatePower(self) -> int:
        print("The power of Karil activates adding {} damage!".format(self.getRanged()))
        return self.getStrength() + self.getRanged()


class Fields(object):

    def __init__(self) -> None:
        self.__name = None
        self.changeField()

    def changeField(self) -> None:
        name = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]

        self.__name = __import__("random").choice(["Toxic Wasteland", "Healing Meadows", "Castle Walls"])

    def fieldEffect(self, fighter1: Combatant, fighter2: Combatant) -> None:
        pass

    def getName(self) -> str:
        return self.__name


class Arena(object):
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.combatants: List[Combatant] = []
        self.fields: Fields = Fields()

    def addCombatant(self, fighter: Combatant) -> None:
        self.combatants.append(fighter) if fighter not in self.combatants else print("The fighter is existed!")

    def removeCombatant(self, fighter: Combatant) -> None:
        self.combatants.remove(fighter) if fighter in self.combatants else print("The fighter is not existed!")

    def listCombatants(self) -> None:
        for combatant in self.combatants:
            print(
                "{0} is a {1} and has a following stats:\nHealth{2}:\nStrength:{3}\nDefence{4}:{5}\nMagic:{4}\nRanged:{5}".format(
                    combatant.name, combatant.__class__.__name__
                    , combatant.health, combatant.getStrength(), combatant.getDefencese(), combatant.getMagic(),
                    combatant.getRanged()))

    def restoreCombatants(self) -> None:
        pass

    def checkValidCombatant(self, fighter: Combatant) -> bool:
        return fighter.getHealth() > 0

    def duel(self, fighter1: Combatant, fighter2: Combatant) -> None:
        if not (self.checkValidCombatant(fighter1) and self.checkValidCombatant(fighter2)):
            print("not valid")
            return
        print("----- Battle has taken place in {} on the {} between {} and {} -----".format(self.name,
                                                                                            self.fields.getName(),
                                                                                            fighter1.name,
                                                                                            fighter2.name))
        count = 1

        while 1:
            if count == 11:
                break
            if not (self.checkValidCombatant(fighter1) and self.checkValidCombatant(fighter2)):
                print("---------- END BATTLE ----------")
                break
            print("\nRound {}\n".format(count))
            fighter1.attackEnemy(fighter2)
            fighter2.attackEnemy(fighter1)
            count += 1


# jeff = Karil("Jeff", 99, 50, 40, 1, 10, 5)
# tim = Ranger("Tim", 99, 10, 10, 1, 50)
# falador = Arena("Falador")
# falador.addCombatant(tim)
# falador.addCombatant(jeff)
# falador.listCombatants()
# duel between ranger and karil
# falador.duel(tim, jeff)
jaina = FrostMage("Jaina", 99, 10, 20, 94, 10)
zezima = PyroMage("Zezima", 99, 15, 20, 70, 1)
wilderness = Arena("Wilderness")
wilderness.addCombatant(jaina)
wilderness.addCombatant(zezima)
# duel between a pyro and frost mage... double ko?!?!?
wilderness.duel(jaina, zezima)