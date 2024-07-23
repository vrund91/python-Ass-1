''' Write a Python program that will demonstrate the use of Identity Operators.'''
x=[1,2,3]
y=x
print(x is y)
print(x is not y)

z=[1,2,3]
print(z is x)
print(z is not x)