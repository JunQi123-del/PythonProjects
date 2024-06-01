import random

playerStartFirst = input("Does the player wants to start first? (Y/N): ")
listOfNumbers = []

def playersTurn():
    numOfNumbers = int(input("Please indicate how many numbers to enter 1 to 3: "))
    while numOfNumbers > 3 or numOfNumbers<0:
            numOfNumbers = int(input("please indicate how many numbers to enter in the correct range 1 to 3: "))
    print("Please enter your word guess(s) below: ")
    for i in range(numOfNumbers):
        userNumber = int(input())
        while (userNumber in listOfNumbers):
            print("The number ",userNumber," is already in the list, please enter another number: ")
            userNumber = int(input())
        listOfNumbers.append(userNumber)
    listOfNumbers.sort()
    print(listOfNumbers)

    if checkConsecutiveNumber(listOfNumbers):
        print("Player win!")
            
def checkConsecutiveNumber(number):
     return number==list(range(1,20+1))

def computersTurn():
    computerNumber = random.choice(range(1,3+1))
    for i in range(computerNumber):
         computerNumber = random.choice(range(1,20+1))
         while(computerNumber in listOfNumbers):
             computerNumber = random.choice(range(1,20+1))
         listOfNumbers.append(computerNumber)
    listOfNumbers.sort()
    print(listOfNumbers)

    if checkConsecutiveNumber(listOfNumbers):
        print("computer win, you lose!")



         
def checkListforNumber():
    if 21 in listOfNumbers:
        return True
    else:
        return False

#starting code

print("Starting: ")

if(playerStartFirst=="Y"):
    while(True):
        playersTurn()
        if(checkConsecutiveNumber(listOfNumbers)):
            break
        else:
            computersTurn()
            if(checkConsecutiveNumber(listOfNumbers)):
                break
else:
     while(True):
        computersTurn()
        if(checkConsecutiveNumber(listOfNumbers)):
            break
        else:
         playersTurn()
        if(checkConsecutiveNumber(listOfNumbers)):
            break

