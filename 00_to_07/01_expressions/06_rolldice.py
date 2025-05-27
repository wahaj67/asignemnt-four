import random 

ROLL_SIDES = 6
def simulate_roll_dice():

 die1 = random.randint(1,ROLL_SIDES)
 die2 = random.randint(1,ROLL_SIDES)

 total = die1 + die2

 print("Total of two dice: ",total)
if __name__ == "__main__":
    simulate_roll_dice()
    