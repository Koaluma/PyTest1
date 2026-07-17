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
    
#Lesson 6: functions (resusable code)

def reduce(a,b):
    return a-b
print(reduce(178,12387))

def is_even(a):
    if  a % 2 == 0:
        return True
    else:
        return False
print(is_even(5)) 

def apply_discount(price, percent):
    return price * (100 - percent) / 100

print(f"final price: {apply_discount(200, 10)}")


#Tests

def celsius_to_farenheit(c):
    return (c*(9/5))+32

print (celsius_to_farenheit(20))



def count_evens(numbers):
    evens = 0
    for num in numbers:
        if num % 2 == 0:
            evens += 1
    return evens

print(count_evens([1,2,3,4,5,6]))


def grade(score):
        if score >= 90:
            return "A"
        elif score  >= 80:
            return "B"
        elif score >=70:
            return "C"
        else:
            return "F"
        
scores = [95,72, 88, 51]
for s in scores:
    print(f"{s} -> {grade(s)}")
    
def is_passing(score):
    return score >= 70

def count_passing(scores):
    count = 0
    for score in scores:
        if is_passing(score) == True:
            count += 1
    return count
print(count_passing([95,72,88,51]))