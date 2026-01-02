#Fuction(def) Is a block of code that does a specific task.(can reuse it whenever need)

#Parameter is a variable written inside the fuction(def) definition.

#Argument is the actual value you pass to a fuction(def) when calling it.

#Example1

def greet():
    print("Linus Torvalds")

greet()
#Example2
def greet(name):
    print(name)

greet("Linus Torvals")

#greet is a parameter.
#Linus Torvalds is a argument.

#Practice
# Sum 2 Numbers

def sum(x, y):
    print(x + y)

sum(5, 10)

#Subtract

def subtract(x, y, z):
    print(x - y - z)

subtract(5, 1, 2)

#Calculate AVG

def avg(M, P, ENG):
    sum= M + P + ENG
    print(sum / 3)

avg(90, 80 ,70)

#Find Max Number

def max_num(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# print(max_num(4, 7, 6))

#Check Even/Odd

def Check(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(Check(10))
print(Check(5))

#Celsius to Fahrenhiet

def celsius(temp):
    Fahrenhiet = (temp * 9/5) + 32
    return Fahrenhiet

print(celsius(30), "C")

# Square Area Calulate

def Square(length):
    Area = length * length # or lenght**2
    return Area

print(Square(50), "M2")

#Grade Calulator

def marks(M, P, C, B, ENG):
    Sum = M + P + C + B + ENG
    if Sum >= 450:
        return "Grade A"
    elif Sum <= 449:
        return "Grade B"
    elif Sum <= 380:
        return " Grade C"
    elif Sum <= 330:
        return " Grade D"
    else:
        return "Fail"
    return Sum

print(marks(90, 90, 90, 90, 90))
