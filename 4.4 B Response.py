# Program 1
name = input()
while not name.isalpha():
    name = input()
print(name.capitalize())

# Program 2
count = 0
sentence = input()
for letter in sentence:
    if letter in "aAeEiIoOuU":
        count = count + 1
print(count)

# Program 3
letter = input()
word = "antidisestablishmentarianism"
for char in word:
    if char == letter:
        print(char)

# Program 4
letter1 = input()
letter2 = input()
while letter2 == letter1:
    letter2 = input()
alpha = "AbCdefGHiJKLmnoPqRsTUvwxyZ"
location1 = alpha.find(letter1.lower())
location2 = alpha.find(letter2.lower())
if location1 == -1:
    letter1 = letter1.upper()
else:
    letter1 = letter1.lower()
if location2 == -1:
    letter2 = letter2.upper()
else:
    letter2 = letter2.lower()
alpha = alpha.replace(letter1, letter2)
print(alpha)


# #1
# This program will only accept an input that is alphabetic characters, no alpha-numeric characters.
# Once the input is only aclphabetic characters, it will output the same string back, but with the first letter
# capitalized.

# #2
# This program will count the number of vowels in the input.

# #3
# This program will accept a single char, then it will print each time that
# char appears in the word "antidisestablishmentarianism"

# #4
# This program will accept 2 DIFFERENT chars, then it will check for where that first
# char appears in the string "alpha", regardless of case, then it will replace that char
# with the second input char.
