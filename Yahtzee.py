from ast import In
import random

dice = [1,1,1,1,1]  # This creates a Python list of five dice 
 
for index in range(0, 5): 
  dice[index] = random.randint(1,6)


test_mode = False
test_count = 1
test = input("Would you like to enter testing mode (y/n): ")
if (test == "y"):
    test_mode = True
    game = False
    dice.clear()
    print("Enter desired numbers:")
    while(test_count<= 5):
        val = int(input( str(test_count) + ": "))
        if (val > 0 and val < 7):
            test_count += 1
            dice.append((val))
        else:
            print("Wrong input...")
else:
    game = True
print("")
 

stay = True # allows user to keep the first roll out come.
roll_count = 1
select = True
reroll = True
while(game):
    if (roll_count == 1):
        print("Roll 1-           -YAHTZEE-                    ")
        print("...............................................") 
        print("Dice Results:  ", end = "") 
        for index in range(0, 5): 
            print(str(dice[index]) + " ", end = "")
        print()
    else: 
        print("""










...............................................""")
        print("Dice Results:  ", end = "")
        for index in range(0, len(dice)):
                print(str(dice[index]) + " ", end="") 
        print()
    while (select):
        print(" ")
        print("Roll " + str(roll_count + 1) + "-           (Enter n for none)")
        select_dice = input("Which dice would you like to reroll: ")
        if (select_dice in str(dice)):
            dice.remove(int(select_dice))
            print("""










...............................................""")
            print("Remaining dice: ", end= "")
            for index in range(0, len(dice)):
                print(str(dice[index]) + " ", end="") 
            print() 
            reroll = True
            stay = False
        elif ((stay == True and select_dice == "n")):
            game= False
            select = False
        elif (select_dice == "n"):        
            roll_count += 1
            select = False
            reroll = True#
        else:
            print("Wrong input try again...")
    while (reroll):
        if (int(len(dice)!= 5)):
            dice.append(random.randint(1, 6))
        else:
            reroll = False
            print("""










...............................................""")
            print("Dice Results:  ", end = "")
            for index in range(0, len(dice)):
                print(str(dice[index]) + " ", end= "")
            print()
    if (roll_count != 3):
        select = True
    else:
        game = False
 
count = [0, 0, 0, 0, 0, 0, 0] 

for index in range(0, 5):
    count[dice[index]] += 1
print()
if(5 in count):
    print("Yahtzee!")
elif ((count[1] >= 1 and count[2] >= 1 and count[3] >= 1 and count[4] >= 1 and count[5] >= 1) \
or (count[2] >=1 and count[3] >= 1 and count[4] >= 1 and count[5] >= 1 and count[6] >= 1)):
    print("Large Straight!")
elif((count[1] >= 1 and count[2] >= 1 and count[3] >= 1 and count[4] >= 1) \
or (count[2] >= 1 and count[3] >= 1 and count[4] >= 1 and count[5] >= 1) \
or (count[3] >= 1 and count[4] >= 1 and count[5] >= 1 and count[6])):
    print("Small Straight!")
elif(4 in count):
    print("Four-of-a-kind!")
elif((2 in count) and (3 in count)):
    print("Full House!")
elif(3 in count):
    print("Three-of-a-kind!")
else:
    print("Sorry...")
print(" ")
print("Thanks for playing!")

while (test_mode):
    print("For debugging purposes your counts are: ") 
    for index in range(0, 7): 
        print("count[" + str(index) + "] = " + str(count[index]))
    print()
    test_mode = False 
