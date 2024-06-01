import random

userName = input("What is your name?: ")
numberOfGuess = 12
guessLeft = numberOfGuess
listOfWords = ["Morning","Day","Night"]
secretWord = random.choice(listOfWords)
#secretWord = "Morning"
hiddenWord = "*"*len(secretWord)
secretWordFound = False
guessCorrect = False

print("Guess the word: ",hiddenWord)
while(guessLeft>0):
    userGuess = input("Guess a Alphabet: ")
    for i, char in enumerate(secretWord):
        if userGuess==char:
            hiddenWordList = list(hiddenWord)
            hiddenWordList[i] = userGuess
            hiddenWord = "".join(hiddenWordList)
            guessCorrect = True

    if hiddenWord.find("*")==-1:
        print("Congratulation ",userName,", You have found the secret word! ",hiddenWord)
        secretWordFound = True
        break

    if guessCorrect:
        print("Good Guess! getting closer to the word!: ",hiddenWord)
    else:
        print("Wrong Guess! Don't give up! ",guessLeft," more tries!: ",hiddenWord)   
    
    guessCorrect = False
    guessLeft-=1

if(secretWordFound==False):
    print("The secret word is: ",secretWord," , Better luck next time")
    


