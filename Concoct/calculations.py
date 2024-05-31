import math
import magicnumbers

#
#  QUESTION: Do we want to pass by reference or by value?
#            I've read that Python passes by assignment,
#            Which is similar to reference, but I haven't
#            been able to get that to work yet.
#

# check for out of range? Less than 8 or more than 25?
def calculate_DC_Cost(DoseDC):
    return magicnumbers.DifficultyClass.DCBASE ** (DoseDC - magicnumbers.Basics.DCMIN)

def calculate_Damage(averageDamage):
    return magicnumbers.DifficultyClass.DAMAGEBASE ** averageDamage

def calculate_HP_Reduction(HPReduction):
    return magicnumbers.DifficultyClass.HPREDUCTIONBASE ** HPReduction

def calculate_Sleep(HPAffected):
    return magicnumbers.Motion.UNCONSCIOUSBASE ** HPAffected

def calculate_Movement_Reduction(MoveReduction, MovementPerSquare):
    return magicnumbers.Motion.MOVESPEEDBASE ** (MoveReduction / MovementPerSquare)

def calculate_Ranged_Concoction(Range, MovementPerSquare):
    return calculate_Movement_Reduction(Range, MovementPerSquare)

def calculate_Multi_Attack_Reduction(NumberOfAttacksLost):
    return magicnumbers.Motion.MULTIATTACKBASE ** NumberOfAttacksLost

def calculate_Memory_Rounds(Duration):
    return magicnumbers.Mental.MEMORYLOSSBASE + math.log2(Duration)

def calculate_Memory_Minutes(Duration):
    return calculate_Memory_Rounds(magicnumbers.Time.MAXROUNDS) + math.log(Duration, 3)

def calculate_Memory_Hours(Duration):
    return calculate_Memory_Minutes(magicnumbers.Time.MAXMINUTES) + math.log(Duration, 4)

def calculate_Memory_Days(Duration):
    return calculate_Memory_Hours(magicnumbers.Time.MAXHOURS) + math.log(Duration, 5)

def calculate_Memory_Weeks(Duration):
    return calculate_Memory_Days(magicnumbers.Time.MAXDAYS) + math.log(Duration, 6)

def calculate_Memory_Months(Duration):
    return calculate_Memory_Weeks(magicnumbers.Time.MAXWEEKS) + math.log(Duration, 7)

def calculate_Memory_Years(Duration):
    return calculate_Memory_Months(magicnumbers.Time.MAXMONTHS) + math.log(Duration, 8)

def calculate_Memory_Loss(Duration, TimeType):

    match TimeType:
        case "rounds":
            return calculate_Memory_Rounds(Duration)
        case "minutes":
            return calculate_Memory_Minutes(Duration)
        case "hours":
            return calculate_Memory_Hours(Duration)
        case "days":
            return calculate_Memory_Days(Duration)
        case "weeks":
            return calculate_Memory_Weeks(Duration)
        case "months":
            return calculate_Memory_Months(Duration)
        case "years":
            return calculate_Memory_Years(Duration) 
        case _:
             return 1  

#TODO: calculate TimeFrameMultiple
def calculate_Onset_Delay(TimeFrameMultiple):
    return magicnumbers.ConcoctionOperations.DELAYBASE**TimeFrameMultiple

def calculate_Save_Attempts(DoseDC, Attempts):
    return DoseDC / (magicnumbers.DifficultyClass.DCMAX*math.sqrt(Attempts))

def calculate_Diminishing_Returns(DoseDC, Stages):
    return math.sqrt(DoseDC / (magicnumbers.DifficultyClass.DCMAX*Stages))

def calculate_Increasing_Intensity(DoseDC, Stages):
    return Stages*math.sqrt(DoseDC/magicnumbers.DifficultyClass.DCMAX)

def calculate_Periodic_Effect(AverageUpTime, AverageDownTime):
    return AverageUpTime / AverageDownTime

def calculate_Punishing_Failures(DoseDC, NumberOfSaves):
    return (magicnumbers.ConcoctionOperations.PUNISHINGBASE**NumberOfSaves) * (DoseDC / magicnumbers.DifficultyClass.DCMAX)

def calculate_Joint_Conditions(FirstConditionMultiplier, SecondConditionMultiplier):
    return FirstConditionMultiplier*SecondConditionMultiplier

def calculate_Separate_Conditions(FirstConditionMultiplier, SecondConditionMultiplier):
    return FirstConditionMultiplier + SecondConditionMultiplier

def calculate_Reduced_Effect(NormalEffectMultiplier, OnSaveEffectMultiplier):
    return (NormalEffectMultiplier + OnSaveEffectMultiplier) / 2 # Just averaging them

def calculate_2D_Area(Area):
    return math.log(Area,4)

def calculate_3D_Area(Volume):
    return math.log(Volume,4)

def calculate_Exhaustion_5E(Stages):

    result = 1

    if(1 <= Stages):
        result *= magicnumbers.DisadvantageOnChecks.ALLCHECKS

    if(2 <= Stages):
        #speed halved - for most races
        result *= calculate_Movement_Reduction(magicnumbers.Basics.AVGPCMOVESPEED, magicnumbers.Basics.DEFAULTMOVEMENTPERSQUARE)

    if(3 <= Stages):
        result *= magicnumbers.DisadvantageOnAttacks.ALLATTACKS * magicnumbers.DisadvantageOnSaves.ALLSAVES

    if(4 <= Stages):
        result *= calculate_HP_Reduction(magicnumbers.Basics.LUCKYNUMBER)

    if(5 <= Stages):
        result *= calculate_Movement_Reduction(magicnumbers.Basics.AVGPCMOVESPEED, magicnumbers.Basics.DEFAULTMOVEMENTPERSQUARE)

    if(6 <= Stages):
        result *= 2 
    
    return result

# This is currently the exponential method.
# The factorial method scales more drastically towards the tail end, assuming
# Later stages are more impactful. Factorial method: 15^x/((14!)/(14-x)!)
def calculate_Exhaustion_1DD(Stages):
    return magicnumbers.Degrade.EXHAUSTION1DDBASE ** Stages  

def calculate_Common_Save(NumberOfDecrements):
    return magicnumbers.AbilityScores.COMMONSAVE * NumberOfDecrements

def calculate_Uncommon_Save(NumberOfDecremenets):
    return magicnumbers.AbilityScores.UNCOMMONSAVE * NumberOfDecremenets

# I believe this calculation would work for increases to AC as well.
def calculate_Armor_Class(NumberOfDecrements):

    result = 1
    for i in range(1,NumberOfDecrements + 1):
        result += 4/(1+i)

    return result

# It might be worthwhile to pull the exponent math on this one out to its own function
# as it shows up more than once. Basically, it describes the range that DoseDC can be as
# a decimal value between 0 and 1. For your DoseDC to be impactful, even at its minimum, we
# have to start at 1. (Hence DCMIN - 1) So, the range becomes DCMAX - (DCMIN -1) where, if
# your DoseDC == DCMAX, the exponent becomes one and your BASE value is fully realized.
def calculate_Contagion(DoseDC):
    return magicnumbers.Degrade.CONTAGIOUSBASE ** ((DoseDC - (magicnumbers.DifficultyClass.DCMIN - 1)) /
                                                    (magicnumbers.DifficultyClass.DCMAX - (magicnumbers.DifficultyClass.DCMIN - 1)))

def calculate_Basics(Specifications["basics"], Multiplier):
    #TODO
    return Multiplier


