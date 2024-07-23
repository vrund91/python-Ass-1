''' Write a Python program that will perform following conversions using appropriate 
method:
 1. string to integer
 2. integer to float
 3. tuple to list
 4. string to list
 5. list to tuple'''

x=(input("Enter a string:"))
y=(input("Enter a string:"))

print("Before convert string:",x,y)

print("1.")
print("convert into string to integer:",int(x)+int(y))
print("\n")

print("2.")
print("convert into int to float:",float(int(x))+float(int(y)))
print("\n")

print("3.")
my_tuple=(1,"RED",5)
print("value of tupple:",my_tuple)
print("convert into tupple to list:",list[my_tuple])
print("\n")

print("4.")
print("convert string to list:",list[x,y])
print("\n")

print("5.")
list1=[1,"hello"]
tuple_list=tuple(list1)
print("convert list to tupple:",tuple_list)