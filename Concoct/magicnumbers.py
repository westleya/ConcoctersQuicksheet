from enum import Enum

class Basics(Enum):
    AVGPCMOVESPEED = 30
    DEFAULTMOVEMENTPERSQUARE = 5
    LUCKYNUMBER = 13

class DifficultyClass(Enum):
    DCBASE = 1.17
    DCMIN = 8
    DCMAX = 25

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

class RemoveSenses(Enum):
    DEAFENED = 3
    BLINDED = 6.5
    MUTED = 2.25
    SILENCED = 2.25
    NUMB = 1.85
    ANOSMIA = 1.07 # Loss of smell
    AGEUSIA = 1.05 # Loss of taste

class DisadvantageOnSaves(Enum):
    COMMONSAVE = 1.4
    DEXTERITYSAVE = 1.4
    CONSTITUTIONSAVE = 1.4
    WISDOMSAVE = 1.4
    UNCOMMONSAVE = 1.15
    INTELLIGENCESAVE = 1.15
    STRENGTHSAVE = 1.15
    CHARISMASAVE = 1.15
    ALLSAVES = 3.5
    #TODO

class DisadvantageOnAttacks(Enum):
    ALLATTACKS = 2.5
    MELEEATTACKS = 1.4
    RANGEDATTACKS = 1.4
    SPELLATTACKS = 1.4
    #TODO

class DisadvantageOnChecks(Enum):
    ALLCHECKS = 1.75
    #TODO

class Motion(Enum):
    PARALYZED = 8
    PETRIFIED = 9
    RESTRAINED = 6
    STUNNED = 7.5
    INCAPACITATED = 7
    LOSEACTION = 2.5
    LOSEBONUS = 2
    LOSEREACTION = 1.5
    CHANGEPLANES = 10
    GROUNDED = 3.5
    MULTIATTACKBASE = 1.3
    MOVESPEEDBASE = 1.07
    UNCONSCIOUSBASE = 1.1 # Also Sleep. This is unusual as Sleep has no save

class Mental(Enum):
    CHARMED = 4
    HALLUCINATING = 7.25
    CONFUSION = 6
    FEAR = 5.5
    SELFHARM = 20
    MEMORYLOSSBASE = 1.5 # This is dependent on the amount of memory lost
    LOSESPECIFICMEMORY = 10
    FORGETEVERYTHING = 20
    INFLUENCEEMOTION = 1.4 # I’m assuming that this’ll be adjudicated as disadvantage on related checks for the affected person or advantage for those manipulating.

class Degrade(Enum):
    DAMAGEBASE = 1.08
    HPREDUCTIONBASE = 1.09
    POISONED = 4.5 # Also alcohol or sickened
    PRONE = 5
    SUFFOCATING = 75
    #TODO

class Time(Enum):
    MAXROUNDS = 10
    MAXMINUTES = 60
    MAXHOURS = 24
    MAXDAYS = 7
    MAXWEEKS = 4
    MAXMONTHS = 12
    MAXYEARS = 100

class ConditionDuration(Enum):
    ONHIT = 1
    NEXTBLANK = 1.25
    ENDCURRENTTURN = 1.35
    BEGINTARGETSTURN = 1.45
    ENDTARGETSTURN = 1.55
    BEGINUSERSNEXTTURN = 1.65
    DURATIONBASE = 1.75
    PERMANENT = 20
    OCCURRENCESBASE = 1.25
    UNTILSAVEBASE = 20
    UNTILCUREDBASE = 20
    UNTILRESOLVES= 0.9

class UsefulnessDuration(Enum):
    ONCE = 1
    USEFULNESSBASE = 2
    PERMANENT = 100
    NUMBEROFUSESBASE = 1.6
    ROUNDSBASE = 1.5
    MINUTESBASE = 0.5
    HOURSBASE = 0.45
    DAYSBASE = 0.4
    WEEKSBASE = 0.35
    MONTHSBASE = 0.3
    YEARSBASE = 0.25

class ConcoctionOperations(Enum):
    DELAYBASE = 0.99
    CRITFAILEFFECT = 1.15
    PUNISHINGBASE = 1.6 # The effect worsens for failing additional saves