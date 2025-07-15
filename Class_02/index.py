import random

print("----------- Number Guessing Game -----------")

computerNumber = random.randint(1, 20)
lives = 3

while lives > 0:
    userGuessNo = int(input("Enter Your Guess between 1 - 20: "))

    if userGuessNo == computerNumber:
        print("Congratulations You've Guessed")
        break
    else:
        lives -= 1

        if userGuessNo > computerNumber:
            print("Please Guess Low Number")
        else:
            print("Please Guess High Number")

        if lives > 0:
            print(f"You've {lives} lives remaining")
        else:
            print("All Lives has been Finished")
            print(f"computer number is: {computerNumber}")
