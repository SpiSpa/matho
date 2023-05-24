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

A = {master_list[0], master_list[1], master_list[2], master_list[3], master_list[4], master_list[5], master_list[6], master_list[7], master_list[8], master_list[9], master_list[10], master_list[11], master_list[12]} 

def makeCard():
    for count in range(25):
        #print("count:", count)
        xRandom = random.randint(0,4)  #x value of a randomized location
        yRandom = random.randint(0,4)    #y value of randimized location
        #print("First Random", xRandom, yRandom)

        if randomizedCard[xRandom][yRandom] == "":
            randomizedCard[xRandom][yRandom] = master_list[count]   #check that the spot is empty
        
        else:
            #print("Location Already Filled")
            xRandom = random.randint(0,4)  # if the randomized location is already taken, try a new randomized location
            yRandom = random.randint(0,4)    #second hash
            #print("Second random", xRandom, yRandom)

            if randomizedCard[xRandom][yRandom] == "":
                randomizedCard[xRandom][yRandom] = master_list[count]
            #else:
                #print("Location already filled")
            
                while randomizedCard[xRandom][yRandom] != "":  # if the second randomized location is also taken, find another spot that is open
                    xcount = 0
                    yRandom = (yRandom + 7) % 5
                    #print("y-random", yRandom)
                    while randomizedCard[xRandom][yRandom] != "" and xcount !=4:
                        xRandom = (xRandom + 7) % 5
                        xcount += 1
                        #print("x-random:", xRandom, "xcount:", xcount)
                    
                randomizedCard[xRandom][yRandom] = master_list[count]

    for i in range(5):
        print(randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4])

def checkCard():
    checkVariable = False
    for i in range(5):
        B = {randomizedCard[i][0], randomizedCard[i][1],randomizedCard[i][2],randomizedCard[i][3],randomizedCard[i][4]}  # all the rows in matho
        C = {randomizedCard[0][i], randomizedCard[1][i],randomizedCard[2][i],randomizedCard[3][i],randomizedCard[4][i]}  # all the columns
        if B.issubset(A) or C.issubset(A) == True:  #checks to see if there's a matho scored in the rows or columns in the first twelve questions
            checkVariable = True
            #print("Row or Column Solution Found. checkVariable =", checkVariable)
        #else:
            #print("Card meets requirements. checkVariable=", checkVariable)
    D = {randomizedCard[0][0], randomizedCard[1][1], randomizedCard[2][2], randomizedCard[3][3], randomizedCard[4][4]}  # diagonal from upper left to lower right
    E = {randomizedCard[0][4], randomizedCard[1][3], randomizedCard[2][2], randomizedCard[3][1], randomizedCard[4][0]}  # diagonal from lower left to upper right
    if D.issubset(A) or E.issubset(A) == True:
        checkVariable = True
        #print("Diagonal Solution found. checkVariable =", checkVariable)
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
