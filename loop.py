#For Loop:Is a way to repeat code for each item in a list ,sting or range of num.

#Print Numbers 1 to 10

for x in range(1,11):
    print(x)

#Sum Numbers 1 to 100

total = 0

for n in range(1,101):
    total += n
print(total)

#Multiplication Table

for X in range(1,11):
    for Y in range(1,11):
        print(f"{X} x {Y} ={X*Y}", end="\t")
print()

#Count Even Numbers

for i in range(0,51,2):
    print(i)

#Reverse Counting

for i in reversed(range(1,11)):
    print(i)

#While Loop: Excute some Code WHILE some condition are true.

#Guess The Numbers Game

EnterNum = int(input("Enter The Number: "))

while EnterNum != 5:
    print("Wrong! Try Again")

    EnterNum = int(input("Enter The Number: "))

print("Right! Cograts")

#Factorial Of a Number

Number = 5
Factorial =1
i = 1

while i <= Number:
    Factorial *= i
    i += 1

print(f"Factorial of {Number} is {Factorial}")