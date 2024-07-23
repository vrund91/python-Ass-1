'''Write a Python program to calculate the area of rectangle and square'''

length=float(input("Enter a area of length:"))
width=float(input("Enter a area of width:"))

side=float(input("Enter a area of square:"))

print("Menu:")
print("1.Area of rectangle")
print("2.Area of square")
print("3.Invalid choice")

choice=int(input("Enter a your choice:"))

if  choice == 1:
    area=length*width
    print('Area of rectangle is:',area)
elif choice == 2:
    square=side*side
    print("Area of square is:",square)
else:
    print("Invalid choice")