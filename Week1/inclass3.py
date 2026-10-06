# Aman Osmonov
# 10/6/2026
"""""
# Problem 1
# Programs prints out "Hello World"

print("Hello World")
"""""

"""""
# Problem 2
# Program asking for the username and greets them

username=input('type your name: ')
print('Hello', username)
"""""

"""""
# Problem 3
# Programed check if the name that typed is either mine or professors, and if it is my or professor name then it greets either of us

username = input('type your name: ')
if username == "Aman" or username == "Antonio":
    print('Hello', username)
else:
    print("Sorry, I don't recognize you.")
"""""

"""""
# Problem 4
# Program computer area of circle with typed radius

r = float(input('enter the radius of the circle: '))
pi = 3.14
area = pi * r * r
print('The area of a circle with radius', r, 'is', area)
"""""

"""""
# Problem 5
# Program canculates MPG based on typed miles and gallons

miles = float(input('Enter the number of miles driven: '))
gallons = float(input('Enter the number of gallons used: '))
MPG = miles / gallons
print('Your car got', MPG, 'miles per gallon.')
"""""

"""""
# Problem 6
# Program converts F to C

f = float(input('Enter the temperature in Fahrenheit: '))
c = (f - 32) * 5 / 9
print(f, 'degrees Fahrenheit is', c, 'degrees Celsius.')
"""""
"""""
# Problem 7
# Programs asks  for the starting day number, and the length of your stay, and
# it will tell you the number of day of the week you will return on

start_day = int(input('Enter the starting day number (0 = Sunday, 6 = Saturday): '))
nights = int(input('Enter the number of nights you will stay: '))
return_day = (start_day + nights) % 7
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print('You will return on a', days[return_day])
"""""