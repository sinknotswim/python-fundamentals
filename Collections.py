#1 5-8

usernames = ['jake', 'michael', 'skylar', 'admin']

special = 'admin'

for special in usernames:
    print("Hello admin, would you like to see a staus report?")
for username in usernames:
    print("Hello, " + username.title() + " thank you for logging in.")

#5-9

usernames = []

special = 'admin'

if not usernames:
    print("We need to find users!")
else:
    for special in usernames:
        print("Hello admin, would you like to see a staus report?")
    for username in usernames:
        print("Hello, " + username.title() + " thank you for logging in.")

#2 5-10

current_users =['jake', 'michael', 'skylar', 'yang', 'jesse']

new_users = ['tanner', 'ike', 'jack', 'Jake', 'michael']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("I'm sorry, that name is taken.")
    else:
        print("User is availible.")

#3 5-11

numlists = list(range(1,10))

for numlist in numlists:
    if numlist==1:
        print("1st")
    elif numlist == 2:
        print("2nd")
    elif numlist == 3:
        print("3rd")
    else:
        print(numlist + "th")

#4 6-1

person = {
    'first_name': 'jenny',
    'last_name': 'smith',
    'age': '22',
    'city': 'wichita'
    }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])

#5 6-7

person2 = {
    'first_name': 'mack',
    'last_name': 'hanner',
    'age': '23',
    'city': 'mcpherson'
    }

person3 = {
    'first_name': 'michael',
    'last_name': 'bisges',
    'age': '21',
    'city': 'wichita'
    }

people = [person, person2, person3]

print(people)