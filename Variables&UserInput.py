# Using varName: type, similarly to TypeScript will strong type the variable.
name: str = input("What is your name?\n")
print(f"Hello {name}")  # Responds Hello to the name
try:
    # Convert the input to an int, if it isn't a convertable string, respond with
    age: int = int(input("How old are you?\n"))
    print(f"{name}, you will be {age + 10} in 10 years.")
except:
    print("Hey. Thats not a number silly.")  # This
