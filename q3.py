'''Create a Python program that will have 3 variables which stores integer, float and
complex value. Display its value and also demonstrate its datatype class using type().'''

first_val=int(input("Enter a Integer number:"))
second_val=float(input("Enter a Float value:"))
third_val=complex(input("Enter a complex number:"))

# Display values of variables
print("Integer value:",first_val)
print("Float value:",second_val)
print("complex value:",third_val)

#Demonstrate data types
print("Integer value:",type(first_val))
print("Float value:",type(second_val))
print("complex value:",type(third_val))