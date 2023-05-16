#Matho Card Generator

import random

xCoord = 0
yCoord = 0
master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(master_list)

#for entry in range(25):     
 #   newInput = int(input("Enter a new number"))
  #  master_list.append(newInput)

print(master_list)

randomizedCard = [["", "", "", "", ""],[ "", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""]]

print(randomizedCard)

count = 0

for count in range(25):
    print("count:", count)
    xRandom = random.randint(0,4)  #x value of a randomized location
    yRandom = random.randint(0,4)    #y value of randimized location
    print("First Random", xRandom, yRandom)

    if randomizedCard[xRandom][yRandom] == "":
        randomizedCard[xRandom][yRandom] = master_list[count]   #check that the spot is empty
        
    else:
        print("Location Already Fo;;ed")
        xRandom = random.randint(0,4)  # if the randomized location is already taken, try a new randomized location
        yRandom = random.randint(0,4)    #second hash
        print("Second random", xRandom, yRandom)

        if randomizedCard[xRandom][yRandom] == "":
            randomizedCard[xRandom][yRandom] = master_list[count]
        else:
            print("Location already filled")
            
            while randomizedCard[xRandom][yRandom] != "":  # if the second randomized location is also taken, find another spot that is open
                xcount = 0
                yRandom = (yRandom + 7) % 5
                print("y-random", yRandom)
                while randomizedCard[xRandom][yRandom] != "" and xcount !=4:
                    xRandom = (xRandom + 7) % 5
                    xcount += 1
                    print("x-random:", xRandom, "xcount:", xcount)
                    
            randomizedCard[xRandom][yRandom] = master_list[count]
            
for i in range(5):
    print(randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4])
