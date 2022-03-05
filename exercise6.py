#1 5-3

alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("You just earned 5 points!")

alien_color1a = ['green', 'yellow', 'red']

if 'blue' in alien_color1a:
    print("You earned no points!")

#2 5-4

alien_color2 = 'green'

if 'green' in alien_color2:
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

alien_color2b = 'red'

if 'green' in alien_color2b:
    print("You just earned 5 points!")
else:
    print("You just earned 10 points!")

#3 5-5

alien_color3a = 'green'

if 'green' in alien_color3a:
    print("You just earned 5 points!")
elif 'yellow' in alien_color3a:
    print("You just earned 10 points!")
elif 'red' in alien_color3a:
    print("You just earned 15 points!")

alien_color3b = 'red'

if 'green' in alien_color3b:
    print("You just earned 5 points!")
elif 'yellow' in alien_color3b:
    print("You just earned 10 points!")
elif 'red' in alien_color3b:
    print("You just earned 15 points!")

alien_color3c = 'yellow'

if 'green' in alien_color3c:
    print("You just earned 5 points!")
elif 'yellow' in alien_color3c:
    print("You just earned 10 points!")
elif 'red' in alien_color3c:
    print("You just earned 15 points!")

#4 5-6

age = 22

if age < 2:
    print("You are a baby.")
elif age > 2 and age < 4:
    print("You are a toddler.")
elif age > 4 and age < 13:
    print("You are a kid.")
elif age > 13 and age < 20:
    print("You are a teenager.")
elif age > 20 and age < 65:
    print("You are an adult.")
elif age > 65:
    print("You are an elder.")

#5 bool

def scary(too):
    print(bool(too))

scary("0")

#it's true because it's 0. If it was anything else it would be false.