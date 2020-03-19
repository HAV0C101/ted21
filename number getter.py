#12022020 List
#cory Keastpither

#imports
import sys

#Vars

numbers = []
UserInput =""
#main loop
print("""
This is a Super Awsome number crunch 
thingymajig which lets you input numbers 
then averages them
""")

while len(numbers) < 10:
    while UserInput.lower() != "x":
        UserInput = input("Number you wish to add(Use x to Quit the Program): ")     
        if UserInput.lower() == "x":
            break        
        numbers.append(int(UserInput))
        length = len(numbers)
    if UserInput.lower() == "x":
        print("Quiting....")
        break

    
#crunch numbers
count = 0
total = 0
while count < len(numbers):
    total += numbers[count]
    count += 1
average = total/len(numbers)

print("You Inputed a total of %d numbers with your list being %s and on average it was %d" % (
length, numbers, average))


