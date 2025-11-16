import random

def Hangman(word):
    max_guesses=6
    wrong_guesses=0
    guessed=len(word)*["_"]
    guessed_letters=[]

    print("Welcome to the Hangman !!")
    print("Lets! start the game...")
    print("\nword:", " ".join(guessed))

    while wrong_guesses < max_guesses and "_" in guessed:
        print("wrong guesses: ",wrong_guesses,"/",max_guesses)
        print("guessed letters: ", guessed_letters)

        guess = input("guess a letter:")
        guess=guess.lower()

        if len(guess) !=1 or not guess.isalpha()  :
            print("enter a single character alphabet only ")
            continue

        if guess in guessed_letters :
            print("The Letter is Already Guessed . Try Other options!! ")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("\nLetter is present in the word!! ")
            for i in range(len(word)):
                if word[i]==guess:
                    guessed[i]=guess

        else:
            print("\nIt's a Wrong guess")
            wrong_guesses+=1

    print("\n-------------------------------")
    if "_" not in guessed:
        print("Congrats !! You guessed the word :",word)
    else:
        print("Game over !! The word choosen is : ",word)




words=["codealpha","internship","offer","google","books"]
word=random.choice(words)
Hangman(word)
