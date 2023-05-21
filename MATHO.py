#Matho Card Generator

import random

xCoord = 0
yCoord = 0

master_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(master_list)

randomizedCard = [["", "", "", "", ""],[ "", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""]]

print(randomizedCard)

count = 0

#set of first 12 entries

A = {master_list[0], master_list[1], master_list[2], master_list[3], master_list[4], master_list[5], master_list[6], master_list[7], master_list[8], master_list[9], master_list[10], master_list[11], master_list[12], master_list[13], master_list[14], master_list[15], master_list[16]} 

def makeCard():
    for count in range(25):
        print("count:", count)
        xRandom = random.randint(0,4)  #x value of a randomized location
        yRandom = random.randint(0,4)    #y value of randimized location
        print("First Random", xRandom, yRandom)

        if randomizedCard[xRandom][yRandom] == "":
            randomizedCard[xRandom][yRandom] = master_list[count]   #check that the spot is empty
        
        else:
            print("Location Already Filled")
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

def checkCard():
    checkVariable = False
    for i in range(5):
        B = {randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4]}
        if B.issubset(A) == True:
            checkVariable = True
            print("Row Solution Found. checkVariable =", checkVariable)
        else:
            print("Card meets requirements. checkVariable=", checkVariable)
    return checkVariable

makeCard()

#print for check 
for i in range(5):
    print(randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4])

while checkCard() == True:
    print("checkCard true.  Remaking Card")
    randomizedCard = [["", "", "", "", ""],[ "", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""],["", "", "", "", ""]]
    makeCard() 
    checkCard()

for i in range(5):
    print(randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4])
