'''Write a Python program to calculate the sum of 5 subject and find the percentage.'''
sub1 = float(input("Enter a first subject marks:"))
sub2 = float(input("Enter a second subject marks:"))
sub3 = float(input("Enter a Third subject marks:"))
sub4 = float(input("Enter a four subject marks:"))
sub5 = float(input("Enter a five subject marks:"))

sum = sub1 + sub2 + sub3 + sub4 + sub5
avg = sum / 5

print("sub1= ",sub1)
print("sub2= ",sub2)
print("sub3= ",sub3)
print("sub4= ",sub4)
print("sub5= ",sub5)

print("The sum of five subject is:",sum)
print("The average is: ",avg)