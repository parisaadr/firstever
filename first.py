import math

print("hello world")

print("      ^")
print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")

print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didn't like being 70.")

character_name = "John"
character_age = "29"
# if i dont put the " for the number is going to have a problem. i can use str function instead.
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

character_name = "John"
character_age = "29"
print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
character_name = "Jack"
character_age = "28"
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

print("ninja turtles")
print("ninja\nturtles")
print("ninja\"turtles")
print("ninja\turtles")
print("Ninja\Turtles")

phrase = "Ninja Turtles"
print(phrase + " are mutated.")

phrase = "Ninja Turtles"
print(phrase.isupper())

phrase = "Ninja Turtles"
print(phrase.upper().isupper())

phrase = "Ninja Turtles"
print(len(phrase))

phrase = "Ninja Turtles"
print(phrase[0])

phrase = "Ninja Turtles"
print(phrase.index("N"))

phrase = "Ninia Turtles"
print(phrase.index("i"))
# how can i make it print both i's?

phrase = "Ninja Turtles"
print(phrase.index("tles"))

phrase = "Ninja Turtles"
print(phrase.index("N"))

phrase = "Ninja Turtles"
print(phrase.replace("Turtles", "Parisa"))

phrase = "Ninja Turtles"
print(phrase.find('Tur'))
# why doesnt it give 7? it starts from ZERO

phrase = "Ninja Turtles"
print(phrase.center(20))

print(2,4.6378,-8.74829)
print(3 * 865.93)
print(4 * 5 + 6)
print(4 + 5 * 6)
print(776 % 3)

my_num = 11
print(my_num)

my_num = -11
print (abs(my_num))

my_num = 11
print(pow(my_num , 4))

my_num = 11
print(max(my_num , 6.3))

print(round(4.8))
print(round(4.1))
print(math.floor(4.8))
print(math.ceil(4.1))
print(math.sqrt(4.8))

# or we could do:
from math import *
print(round(4.8))
print(round(4.1))
print(floor(4.8))
print(ceil(4.1))
print(sqrt(4.8))

#GETIING INPUT FROM USERS
# surname = input("Enter your name: ")
# print("Hello  " + surname + "!")

# surname = input("Enter your name: ")
# age = input("and your age: ")
# print("Hello  " + surname + "!")
# print("Wow " + age + "! You're so young!")

#BASIC CALCULATOR (THE WRONG ONE NO.1)
# num1 = input("Enter a number: ")
# num2 = input("and another number: ")
# result = (num1 + num2)
# print(result)

#BASIC CALCULATOR (THE WRONG ONE NO.2)
# num1 = input("Enter a number: ")
# num2 = input("and another number: ")
# result = int(num1) + int(num2)
# print(result)

#BASIC CALCULATOR (THE WRONG ONE NO.3)
# num1 = input("Enter a number: ")
# num2 = input("and another number: ")
# result = float(num1 + num2)
# print(result)

#BASIC CALCULATOR (THE CORRECT ONE)
# num1 = input("Enter a number: ")
# num2 = input("and another number: ")
# result = float(num1) + float(num2)
# print(result)

#MAD LIBS GAME
# noun = input("Enter a noun: ")
# nounn = input("Enter another noun: ")
# verb = input("Enter a verb: ")
# adj = input("Enter an adjective: ")
# print(noun + " is my rock")
# print("I take him for a " + nounn)
# print("He " + verb + " in the light")
# print("He's " + adj + ", he doesn't bite")

#LISTS
friends = ["Carter", "Calvin", "Edward"]
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
print(friends[1:4])
# print(friends[:-2]) # how can i make it work this way?
friends[2] = "Diego"
print(friends[2])
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
lucky_numbers = [20, 14, 11, 23, 64]
print(friends)

friends.extend(lucky_numbers)
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.append("Diego")
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.insert(2, "Paolo")
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.remove("Carter")
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.reverse()
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.clear()
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.pop()
print(friends)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
print(friends.index("Edwin"))
# print(friends.index("Joan"))

friends = ["Carter", "Calvin", "Edward", "Edwin", "William", "Edwin"]
print(friends.count("Edwin"))

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
friends.sort()
print(friends)
lucky_numbers = [20, 14, 11, 23, 64]
lucky_numbers.sort()
print(lucky_numbers)

coordinates = (11, 14)
print(coordinates[0])
# coordinates[1] = 20  we cant change tuples.

testlist = [(11, 14), (20, 23), (64, 81)]
print(testlist)
testlist[0] = (8, 11)
print(testlist)
testlist[0] = 8
print(testlist)
# print(testlist.index(20)) 20 as an element doesnt exsit.

#FUNCTIONS AND RETURN STATEMENT
def sayhi():
    print("Hello user")
sayhi()

def sayhi():
    print("Hello user")
print("top")
sayhi()
print("bottom")

def sayhi(name, age ):
    print("Hello " + name + "Wow " + age + "! You're so young!")
sayhi("Carter ", "29")
sayhi("Jack ", "28")

def cube(num):
    num*num*num
cube(3)

def cube(num):
    return num*num*num
print(cube(3))

#IF STATEMENT
ishungry = True
if ishungry:
    print("well go eat!!!")
# this wouldnt work if we changed the value to false

iscloudy = False
if iscloudy:
    print("please take your umbrella")
else:
    print("please take your sunglasses")

ismeat = False
ispasta = False
if ismeat:
    print("you should get steak")
elif ispasta:
    print("you should get spaghetti and meatballs")
else:
    print("you should get a salad")

ishungry = False
ismeat = False
ispasta = False
if ishungry and ismeat:
    print("well you should go out and have some steak!")
elif ishungry and ispasta:
    print("well you should go out and have some spaghetti and meatballs!")
elif ishungry:
    print("well you should go out and have a salad")
else:
    print("just stay home then.")

ishungry = True
iscloudy = False
ismeat = False
ispasta = False
if not(ishungry) or iscloudy:
    print("let's just stay home")
elif ismeat:
    print("well you should go out and have some steak. don't forget to take your sunglasses!")
elif ispasta:
    print("well you should go out and have some spaghetti and meatballs. don't forget to take your sunglasses!")
else:
    print("well you should go out and have a salad. don't forget to take your sunglasses!")

#COMPARISON AND IF STATEMENT
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(432, 264, 2243))

#LESS BASIC CALCULATOR
# num1 = float(input("enter a number: "))
# op = input("enter operator: ")
# num2 = float(input("enter another number: "))
# if op == "+":
#    print(num1 + num2)
# elif op == "-":
#    print(num1 - num2)
# elif op == "/":
#    print(num1 / num2)
# elif op == "*":
#    print(num1 * num2)
# else:
#    print("invalid operator")

#DICTIONARIES
monthconv = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}
print(monthconv["Nov"])
print(monthconv.get("Dec"))
print(monthconv.get("sep"))

#WHILE LOOP
i = 1
while i <= 10:
    print(i)
    i += 1
print("done with loop")

#BASIC GUESSING GAME
guessword = "Ninja Turtles"
guess = ""
# while guess != guessword:
#    guess = input("take a guess: ")

print("yay! you won!")

#LESS BASIC GUESSING GAME
guessword = "Ninja Turtles"
guess = ""
guesscount = 0
guesslimit = 3
outofguess = False
# while guess != guessword and not(outofguess):
#    if guesscount < guesslimit:
#      guess = input("take a guess: ")
#      guesscount += 1
#    else:
#        outofguess = True

if outofguess:
    print("sorry, you lost!")
else:
    print("yay! you won!")

#FOR LOOPS
for letter in "Ninja Turtles":
    print(letter)

friends = ["Carter", "Calvin", "Edward", "Edwin", "William"]
for friend in friends:
    print(friend)

for number in range(11):
    print(number)

for number in range(len(friends)):
    print(friends[number])

for number in range(5):
    if number == 0:
        print("First interation")
    else:
        print("Not first")

#EXPONENT AND FOR LOOPS
def raisetopower(basenum, powernum):
    result = 1
    for number in range(powernum):
        result = result * basenum
    return result
print(raisetopower(2,11))

#2D LISTS
numgrid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(numgrid[0][0])

#NESTED LOOPS
for row in numgrid:
    print(row)

for row in numgrid:
    for col in row:
        print(col)

#BASIC TRANSLATOR
# in ninja turtles language they say 't' instead of the vowels
'''
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in 'aeuio':
            if letter.islower():
                translation = translation + "t"
            else:
                translation = translation + "T"
        else:
            translation = translation + letter
    return translation
print(translate(input("Talk in Ninja Turtles: ")))
'''
#TRY/EXCEPT BLOCK
'''
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid Input")
'''
#IMPORTING, CLASSES, OBJECTS & OBJECT FUNCTIONS
from Class import student
student1 = student("Carter", "Data Science", 3.5, False)
student2 = student("Calvin","Fashion", 3.3, False)
print(student1.name)
print(student2.major)
print(student2.on_honor_roll())

#MULTIPLE CHOICE QUIZ
# answer these questions about shrek2

from quizquestions import question
question_prompts = [
    "\nWho said, 'The position of annoying talking animal has already been filled.'?\n(a) Shrek\n(b) Fiona\n(c) The King\n(d) Donkey\nYour answer: ",
    "\nWhen the messenger from Far Far Away arrives at the swamp, what is the name of \nthe trumpetist who goes on playing after everybody was supposed to stop?\n(a) Angus\n(b) Reggie\n(c) Pete\n(d) Fred\nYour answer: ",
    "\nWhat was the secret that Fairy Godmother used to control the King?\n(a) He had a criminal past.\n(b) He was an ogre too.\n(c) He was a frog.\n(d) He was not the real king.\nYour answer: "
]

Questions = [
    question(question_prompts[0], "d"),
    question(question_prompts[1], "b"),
    question(question_prompts[2], "c"),
]
'''
def run_test(questions):
    score = 0
    for Question in Questions:
        reply = input(Question.prompt)
        if reply == (Question.answer):
            score += 1
    print("You got " + str(score) + " out of " + str(len(Questions)) + " questions correct!")
run_test(Questions)
'''













