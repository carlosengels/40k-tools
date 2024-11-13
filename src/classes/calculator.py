import random

def rollDice():
    roll = random.randint(1, 6)
    return roll

def calculateWoundRoll(strength, toughness):
    if strength == toughness:
        return 4
    # If S is double or more than T
    if strength  >= toughness * 2:
        return 2
    # If S is half or less T
    if strength * 2 <= toughness:
        return 6
    #If strength is greater than toughness
    if strength > toughness:
        return 3
    #If strength is lower than toughness
    if strength < toughness:
        return 5

def calculateDamage(shots, strength, ballisticSkill, toughness, save):
    # calculate how many shots have hit
    hits = 0
    x = 0
    while x < shots:
        roll = rollDice()
        if roll >= ballisticSkill:
            hits += 1
        x += 1
    print("Out of " + str(shots) + " shots, " + str(hits) + " hit.")
    # calculate how many hits wound
    wounds = 0
    y = 0
    while y < hits:
        roll = rollDice()
        if roll >= calculateWoundRoll(strength, toughness):
            wounds += 1
        y += 1
    print("Out of " + str(hits) + " hits, " + str(wounds) + " wound.")
    # calculate how many wounds are saved
    failedSaves = 0
    z = 0
    while z < wounds:
        roll = rollDice()
        if roll < save:
            failedSaves += 1
        z += 1
    print("Out of " + str(wounds) + " wounds, " + str(failedSaves) + " go(es) through.")
    
    # calculate total damage
    damage = 0
    q = 0
    while q < failedSaves:
        roll = rollDice()
        print(str(roll) + " damage!")
        damage += roll
        q +=1

    print("Total Damage:" +  str(damage))
    return damage