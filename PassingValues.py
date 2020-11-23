# Uh Comment?

from random import shuffle


def compare(x: int, y: int):
    if x < y:
        print(f"{x} is less than {y}")
    elif y < x:
        print(f"{y} is less than {x}")
    else:
        print(f"{x} is equal to {y}")


for x in range(3):
    int1 = int(input("What is the first integer?\n"))
    int2 = int(input("What is the second integer?\n"))
    compare(int1, int2)


names: list = list()


def eliminate(eliminate: int):
    shuffle(names)
    for __ in range(eliminate):
        names.pop()
    return names


for y in range(6):
    name: str = input("Input a name.\n")
    names.append(name)

voteOff: int = int(input("How many people would you like to vote off?\n"))
answer = eliminate(voteOff)

seperator: str = ", "

print(f"{len(names)} survived. Those people are {seperator.join(names)}")
