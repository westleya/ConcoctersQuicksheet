import scipy
import numpy
from enum import Enum

class ApplicationMethod(Enum):
    INGESTION = 0.75
    INJECTION = 1
    INJURY = 1
    INHALATION = 1.5
    CONTACT = 2

class TargetedSave(Enum):
    STRENGTH = 7.5
    DEXTERITY = 1.25
    WISDOM = 0.65
    INTELLIGENCE = 5
    CHARISMA = 1.12
    CONSTITUTION = 1
    NOSAVE = 20

class DamageType(Enum):
    FIRE = 1.3
    PSYCHIC = 9
    COLD = 1.5
    NECROTIC = 4.5
    MAGICALWEAPON = 5.2
    NONMAGICALWEAPON = 1.3
    PURE = 20
    POISON = 1

class SpellLevel(Enum):
    CANTRIP = 2
    FIRST = 3
    SECOND = 5
    THIRD = 8
    FOURTH = 13
    FIFTH = 21
    SIXTH = 34
    SEVENTH = 55
    EIGHTH = 89
    NINTH = 144

class MutedSense(Enum):
    DEAFENED = 3
    BLINDED = 6.5
    MUTED = 2.25
    SILENCED = 2.25
    NUMB = 1.85
    ANOSMIA = 1.07 #loss of smell
    AGEUSIA = 1.05 #loss of taste

class Disadvantage(Enum):
    COMMONSAVE = 1.4
    DEXTERITYSAVE = 1.4
    CONSTITUTIONSAVE = 1.4
    WISDOMSAVE = 1.4
    UNCOMMONSAVE = 1.15
    INTELLIGENCESAVE = 1.15
    STRENGTHSAVE = 1.15
    CHARISMASAVE = 1.15
    ALLSAVES = 3.5
    ALLATTACKS = 2.5
    MELEEATTACKS = 1.4
    RANGEDATTACKS = 1.4
    SPELLATTACKS = 1.4
    ALLCHECKS = 1.75
    #TODO


# check for out of range? Less than 8 or more than 25?
def calculat_DC_Cost(targetDC):
    return 1.17**(targetDC - 8)


def calculate_basics(specifications["basics"], multiplier):
    #TODO
    return multiplier


def Calculate_Cost(specifications):
    #TODO
    multiplier = specifications["base_price"]
    (lambda: multiplier, lambda: multiplier *= calculate_basics(specifications["basics"], multiplier))[specifications["basics"]]();

    return multiplier

