from __future__ import annotations
from typing import List


class Combatant(object):
    def __init__(self) -> None:
        self.name = ""
        self.__maxHealth: int = 0
        self.__health: int = 0
        self.__strength: int = 0
        self.__defense: int = 0
        self.__ranged: int = 0
        self.__magic: int = 0

    def caclulatePower(self) -> int:
        pass

    def attackEnemy(self, enemy: Combatant) -> None:
        enemy.takeDamage(self.caclulatePower())

    def takeDamage(self, damage: int) -> None:
        real_damage = damage - self.__defense
        self.__health -= real_damage

    def resetValues(self):
        self.__health = self.__maxHealth

    def getMaxHealth(self) -> int:
        return self.__maxHealth

    def getHealth(self) -> int:
        return self.__health

    def setHealth(self, hp: int) -> None:
        pass

    def getStrength(self) -> int:
        pass

    def getDefencese(self) -> int:
        pass

    def getRanged(self) -> int:
        pass

    def getMagic(self) -> int:
        pass

    def details(self) -> str:
        return f"{}{}{}"

class Mage(Combatant):
    def __init__(self):
        super().__init__()
        self.mana = self.getMagic()
        self.regenRate = self.getMagic()//4
    def resetValues(self):
        super().resetValues()
        
class Fields(object):
    Fields_type = ["Toxic Wasteland", "Healing Meadows", "Castle Walls"]

    def __init__(self, name: str) -> None:
        self.__name: str = name

    def changeField(self) -> None:
        self.__name = __import__("random").choice(self.Fields_type)

    def fieldEffect(self, fighter1: Combatant, fighter2: Combatant) -> None:
        pass

    def getName(self) -> str:
        pass


class Arena(object):
    def __init__(self, name: str, fields: Fields) -> None:
        self.name: str = name
        self.combatants: List[Combatant] = []
        self.fields: Fields = fields

    def addCombatant(self, fighter: Combatant) -> None:
        self.combatants.append(fighter) if fighter not in self.combatants else print("The fighter is existed!")

    def removeCombatant(self, fighter: Combatant) -> None:
        self.combatants.remove(fighter) if fighter in self.combatants else print("The fighter is not existed!")

    def listCombatants(self) -> None:
        pass

    def restoreCombatants(self) -> None:
        pass

    def checkValidCombatant(self, fighter: Combatant) -> bool:
        return fighter.getHealth() != 0

    def duel(self, fighter1: Combatant, fighter2: Combatant) -> None:
        if not (self.checkValidCombatant(fighter1) and self.checkValidCombatant(fighter2)): return
