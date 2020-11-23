names: list = ["Peter", "Bruce", "Steve", "Tony",
               "Natasha", "Clint", "Wanda", "Hope", "Danny", "Carol"]
numbers: list = [100, 50, 10, 1, 2, 7, 11, 17, 53, -8, -4, -9, -72, -64, -80]

print("Every other name")
# Every other name
namesCounter: int = 0
while namesCounter < len(names):
    if (namesCounter % 2 == 0):
        print(names[namesCounter])
    namesCounter += 1

print("\n\nPositive Numbers")

# Positive Numbers
for num in numbers:
    if num > 0:
        print(num)


print("\n\nSum Of Nums")

# Sum Of Nums
total: int = 0
for num in numbers:
    total += num
print(total)


print("\n\nOdd Numbers")

# Odd Numbers
for num in numbers:
    if not (num % 2 == 0):
        print(num)


print("\n\nNames after Thor")

# Names after Thor
for name in names:
    if name[0] > "T":
        print(name)


print("\n\nMax In Num List")

# Max In Num List
curValue: int = 0
for num in numbers:
    if num > curValue:
        curValue = num
print(curValue)
