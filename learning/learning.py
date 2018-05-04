import random

print("\nHello World!")

name = "Brandon Alfred"

print("\nHello everyone, my name is " + name)

name = 21

print("\n")
print(name)  # variable types can be changed dynamically
print("\n")

# this is a comment

'''
this is how you make a comment blocks
'''

# Lists (basically arrays)
grocery_list = ["cherry's", "cereal", "cheese", "bacon"]
other_list = ["this", "is", "the", "other", "list"]

print(grocery_list)
print(other_list)

combined_list = [grocery_list, other_list]

print(combined_list)

grocery_list.append("onions")
print(grocery_list)

print(len(grocery_list))

# Dictionaries

super_villians = {'Fiddler': 'Isaac Bowin',
                  'Captian Cold': 'Leonard Snart',
                  'Pied Piper': 'Thomas Peterson'}

# using different methods
print(super_villians['Captian Cold'])
print(super_villians.get("Fiddler"))

# Conditionals
print("\n")

age = 18

if age > 16:
    print("You're old enough to drive")
elif age > 21:
    print("You're old enough to drink")
elif age < 21:
    print("You're not old enough to drive")
else:
    print("sorry :(")

print("\n")

if (age > 1) and (age > 16):
    print("You're not a kid, and you're old enough to drive")
else:
    print("sorry :(")

# to print a for loop in one line
for x in range(0, 10):
    print(x, " ", end="")

print("\n")

# new line will be done automatically
for x in range(0, 10):
    print(x, " ")

print("\n")

for i in super_villians:
    print(i)

print("\n")

print(super_villians)

print("\n")

for i in grocery_list:
    print(i)

print("\n")

random_num = random.randrange(0, 20)

while(random_num != 10):
    print(random_num)
    random_num = random.randrange(0, 20)