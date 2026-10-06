"""""
Fname = input("Enter your first name: ")
Lname = input("Enter your last name: ")
age = int(input("Enter your age: "))
print(type(age))
print(type(Fname))

print(f'Hello {Fname} {Lname}')

FirstName="Antonio"
LastName="Tovar"

print(FirstName + " " + LastName)
print(FirstName," ", LastName)
print(f'Hello {FirstName} {LastName}')


print("Antonio", "Tovar",)

print("Antonio", "Tovar", sep="::")
"""""
"""""
def addone(x):
    return x + 5
print(addone(5))
"""""
"""""
def addone():
    userinput = int(input("Enter a number: "))
    print(userinput + 1)

addone()
"""""
"""""
counter = 5
counter = counter+1
counter += 1
counter *=2
counter = counter * 2
counter **= 2
counter /= 2
"""""
"""""
counter=5
# multi assignment
a,c,b =4,3,2
"""""
"""""
def myfunction(num):
    addition= num+num
    multiplication= num*num
    division= num/num
    return addition, multiplication, division
add,multi,div=myfunction(5)
print(add,multi,div)
"""""
"""""
import random
import string
a,b,c,d=23, "Antonio", False, [24,12,36]
print(a,b,c,d)
"""""
print(3/2*5)