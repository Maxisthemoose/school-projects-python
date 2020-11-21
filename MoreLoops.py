# 1-100 Prompt
number: int = 0
while number < 1 or number > 100:

    try:
        number = int(input("Please enter a whole number from 1-100\n"))
        if number <= 100 and number >= 1:
            print("Thank you for the input.")
            break
        else:
            print("I said a number between 1 and 100.")
    except:
        print("That wasn't a number. Please try again.\n")


# Favorite Color
favoriteColor: str = "blue"
counter: int = 1
guess: str = ""

while guess.lower() != favoriteColor:
    if counter == 1:
        guess = input("What is my favorite color?\n")
    else:
        guess = input("That guess was incorrect. Please guess again.\n")

    counter += 1

print(f"You got it! It was {favoriteColor}! It took you {counter} guesses.")


# Number Added

numberOfNumbers: int = 0
while numberOfNumbers == 0:
    try:
        numberOfNumbers = int(input(
            "Please enter a number for the amount of numbers you would like to add together.\n"))
    except:
        print("That wasn't a number")

counter: int = 0

numberList: list = list()

while counter < numberOfNumbers:
    try:
        numberList.append(int(input(f"Enter number #{counter + 1}\n")))
        counter += 1
    except:
        print("That wasn't a number...\n")

total: int = 0
for num in numberList:
    total += num


print(f"All {len(numberList)} numbers add to {total}!")
