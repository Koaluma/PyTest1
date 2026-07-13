#Lesson 1: Printing and variables

name = "Eduardo"
last_name = "Saldivar"
age = 30
print(f"im {name} {last_name} and im {age} years old")

#Lesson 2: Math and updating variables

price = 10
discount = 5
total = price - discount
print(total)

egg_boxes = 3
eggs_per_box = 12
total_eggs = eggs_per_box * egg_boxes
print(f"We have a total of {total_eggs} eggs")

#Lesson 3: Conditionals

cost_per_person = 35
total_persons =  5
if total_persons > 4:
    print(f"The total cost is:{(cost_per_person*total_persons)*0.95}")
else:
    print(f"The total cost is: {cost_per_person*total_persons}")

patient = "?"

if patient is "dog":
    print("This patient is a dog")
elif patient is "cat":
    print("This patient is a cat")
else:
    print("Unknown patient")


#Lesson 4: loops

for i in range(5):
    print (i)

print("5 multiplied from 1 to 10")
for i in range(1,11):
    print(f"5*{i}={i*5}")

for i in range(10,0,-1):
    print(i)

#Lesson 5: lists

fruits = ["apple", "cherry", "banana"]
meats = ["beef","pork","chicken"]
print(fruits[0])


numbers = [67, 69, 15, 6]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print(biggest)
    
