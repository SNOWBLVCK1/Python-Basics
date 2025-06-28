#Loop control statement

fruits = ["apple","banana","cherry", "date"]

for fruit in fruits:
    if fruit == "cherry":
        break #Exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue #skips cherry and moves to the literation
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass #placeholder , no action is needed for cherry
    print(fruit)
    