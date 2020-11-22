name: str = input("What is your name?\n")

try:
    integer1: int = int(input(f"Hello {name}, please enter an integer.\n"))
    integer2: int = int(input(f"{name}, please enter another integer.\n"))

    print(f"Dividing {integer1} by {integer2} will return a whole number") if integer1 % integer2 == 0 else print(
        f"Dividing {integer1} by {integer2} will not return a whole number")

except:
    print("Something went wrong while converting inputs to intergers.")
