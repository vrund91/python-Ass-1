'''Write a Python program that will demonstrate the use of Bitwise Operators.'''

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))

print("1.x & y")
print(f"Bitwise {x} & {y} of two value: " ,x & y)
print("\n")

print("2.x | y")
print(f"Bitwise {x} | {y} of two value: " ,x | y)
print("\n")

print("3.~x ")
print(f"Bitwise ~{x}  of two value: " ,~x)
print("\n")

print("4.x ^ y")
print(f"Bitwise {x} ^ {y} of two value: " ,x ^ y)
print("\n")

print("5.x >> y")
print(f"Bitwise {x} >> {y} of two value: " ,x >> y)
print("\n")

print("5.x << y")
print(f"Bitwise {x} << {y} of two value: " ,x << y)
print("\n")