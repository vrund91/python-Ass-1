'''Write a Python program that will demonstrate the use of Logical Operators'''

x=int(input("Enter a number:"))
y=int(input("Enter a number:"))

print("1. Logical AND (x > 0 and y > 0):")
result=(x > 0) and (y > 0)
print(f"({x} > 0) and ({y} > 0)->Result:{result}")

print("2. Logical OR (x > 0 or y > 0):")
result=(x > 0) or (y > 0)
print(f"({x} > 0) or ({y} > 0)->Result:{result}")

print("3. Logical NOT (not x > 0):")
result=(not x > 0)
print(f"not ({x} > 0) ->Result:{result}")

print("4. Logical NOT (not y > 0):")
result=(not y > 0)
print(f"not ({y} > 0) ->Result:{result}")

