'''Write a Python program to swap of two numbers.'''

x=int(input("Enter a first value:"))
y=int(input("Enter a second value:"))

print("Before swapping value:")
print("x =",x)
print("y =",y)

temp = x
x = y
y = temp

print("After swapping value:")
print("x =",x)
print("y =",y)