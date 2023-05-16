#Matho Card Generator

import random

xCoord = 0
yCoord = 0
master_list = []

print(master_list)

for entry in range(25):
    newInput = int(input("Enter a new number"))
    master_list.append(newInput)

print(master_list)

randomizedCard = [["", "", "", "", ""],[ "", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""]]

print(randomizedCard)

count = 0

for count in range(25):
    print("count:", count)
    xRandom = random.randint(0,4)  #first hash
    yRandom = random.randint(0,4)    #first hash
    print("First Hash", xRandom, yRandom)

    if randomizedCard[xRandom][yRandom] == "":
        randomizedCard[xRandom][yRandom] = master_list[count]   #check that the spot is empty
        
    else:
        print("Collision!")
        xRandom = random.randint(0,4)  #second hash
        yRandom = random.randint(0,4)    #second hash
        print("Second hash", xRandom, yRandom)

        if randomizedCard[xRandom][yRandom] == "":
            randomizedCard[xRandom][yRandom] = master_list[count]
        else:
            print("Collision")
            
            while randomizedCard[xRandom][yRandom] != "":
                xcount = 0
                yRandom = (yRandom + 7) % 5
                print("y-random", yRandom)
                while randomizedCard[xRandom][yRandom] != "" and xcount !=4:
                    xRandom = (xRandom + 7) % 5
                    xcount += 1
                    print("x-random:", xRandom, "xcount:", xcount)
                    
            randomizedCard[xRandom][yRandom] = master_list[count]
            
print("test")            
print(randomizedCard)
