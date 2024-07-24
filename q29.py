'''Write a Python program which asks the user to input a string. Perform the following 
operations:
  Slicing operation
  Concatenate by using + and , operator'''

str1 = input("Enter a string:")

print("1.Slicing of string")
print("2.Concatenation using +")
print("3.Concatenation using ,")

c = int(input("Enter a choice:"))

if(c==1):
  r1 = int(input("Enter range1 for slicing:"))
  r2 = int(input("Enter range2 for slicing::"))
  print("Sliced string is:",str1[r1:r2])
 
elif(c==2):
    str2 = input("Enter string to append:")
    concatstr = str1 + str2
    print("Concatenated string is:",concatstr)

elif(c==3):
    str3 = input("Enter string to append:")
    print("Concatenated string is:",str1,str3)
    
else:
    print("Invalid choice")
