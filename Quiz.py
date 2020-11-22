output: str = input("Is grass green?\n")

validAnswers: list = ["t", "true", "f", "false"]

try:
    index: int = validAnswers.index(output.lower())
    answer: str = validAnswers[index]

    if (answer == "t" or answer == "true"):
        print("That is correct")
    else:
        print("That is incorrect")
except:
    print("Invalid Answer")
