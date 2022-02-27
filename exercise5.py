
#1
music = 'folk'
print("Is music=='folk'? I predict True.")
print(music=='folk')

music = 'rock'
print("Is music=='rock'? I predict True.")
print(music=='rock')

music = 'hip hop'
print("Is music=='hip hop'? I predict True.")
print(music=='hip hop')

music = 'rap'
print("Is music=='rap'? I predict True.")
print(music=='rap')

music = 'blues'
print("Is music=='blues'? I predict True.")
print(music=='blues')

music = 'blues'
print("Is music=='blue'? I predict False.")
print(music=='blue')

music = 'rap'
print("Is music=='wrap'? I predict False.")
print(music=='wrap')

music = 'hip hop'
print("Is music=='hips'? I predict False.")
print(music=='hips')

music = 'rock'
print("Is music=='stone'? I predict False.")
print(music=='stone')

music = 'folk'
print("Is music=='falk'? I predict False.")
print(music=='falk')

#2

#strings equality

def sent_t():
    sentence = "Kit-Kat's are chocolate."
    print(sentence)
    q = "Kit-Kat's are chocolate."
    print(q)

    if q==sentence:
        print("Equal")

sent_t()

def sent_f():
    sentence = "Kit-Kat's are chocolate."
    print(sentence)
    q = "Hershey's are chocolate."
    print(q)

    if q!=sentence:
        print("Not Equal")

sent_f()

#.lower

def low_t():
    car = "BMW"
    print(car)
    print(car.lower())

    if car.lower() == "bmw":
        print("Equal")

low_t()

def low_f():
    car = "BMW"
    print(car)
    print(car.lower())

    if car.lower() != "audi":
        print("Not Equal")

low_f()

#number inequality

answer = 21
if answer == 21:
    print("True")

answer = 21
if answer != 18:
    print("False")

# and/or

number_1 = 12
number_2 = 1
if number_1 >= 11 and number_2 >= 0:
    print("True")
else:
    print("False")

number_1 = 12
number_2 = 1
if number_1 >= 11 or number_2 >= 0:
    print("True")
else:
    print("False")

#list

grocery = ['milk', 'eggs', 'bread']
if 'milk' in grocery:
    print("True")
else:
    print("False")

grocery = ['milk', 'eggs', 'bread']
if 'dog food' in grocery:
    print("True")
else:
    print("False")

#3

def maths(a, b):
    print("This is a: " + str(a))
    print("This is b:" + str(b))
    c=a+b
    d=a-b
    e=a*b
    f=a/b
    print("A+B: " + str(c))
    print("A-B: " + str(d))
    print("A*B: " + str(e))
    print("A/B: " + str(f))

maths(1, 2)

#4 mod, minus, exponent, plus

def maths_2(a):
    b = 2
    a%=b
    print(a)
    a-=b
    print(a)
    a^=b
    print(a)
    a+=b
    print (a)

maths_2(2)