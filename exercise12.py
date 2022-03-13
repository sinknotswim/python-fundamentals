#10-6

print("Give me two numbers, and I'll add them! 10-6")

number1 = input("First number: ")
number2 = input("Second number: ")

try:
    answer = int(number1) + int(number2)
    print(answer)
except:
    print("An Exception Occured")

#10-7

print("Give me two numbers, and I'll add them! 10-7, and b to stop.")

while True:
    try:
        number1 = input("First number: ")
        number1 = int(number1)
        number2 = input("And Another Number: ")
        number2 = int(number2)
        if number1 or number2 == "b":
            break
    except ValueError:
        print("Sorry, that's not a valid number input. Try again, please.")
    else:
        answer = number1 + number2
        print(answer)

#10-8

names = ["cats.txt", "dogs.txt"]

for name in names:
    print("Finding file...")
    try:
        with open(name) as filestuff:
            stuff = filestuff.read()
            print(stuff)
    except FileNotFoundError:
        print("File not found!")

#10-9

names = ["cats.txt", "dogs.txt"]

for name in names:
    print("Finding file...")
    try:
        with open(name) as filestuff:
            stuff = filestuff.read()
            print(stuff)
    except FileNotFoundError:
        pass