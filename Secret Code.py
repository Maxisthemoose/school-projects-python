from random import randint

secretCode: str = ""
attempts: int = 1

for x in range(4):
    secretCode += str(randint(1, 9))

print(secretCode)

guesses: list = list()

whileLoop: bool = True
correct: list = []
while whileLoop:

    for x in range(len(correct) - 1):
        del correct[x]

    for x in range(4):
        guess: str = input(f"What is your #{x + 1} guess?\n")
        guesses.append(guess)

    for y in range(4):
        if (guesses[y] == secretCode[y]):
            correct.append(guesses[y])

    if (len(correct) >= 4):
        whileLoop = False
    else:
        print(f"You only got {len(correct)} right! Try again.\n")
        attempts += 1

print(
    f"You got it! The code was {secretCode} and it took you {attempts} tries")
