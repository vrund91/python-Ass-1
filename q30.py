''' Write a Python program which asks the user to input a string. Use endswith and startwith 
operations on input string'''

str1=(input("Enter a string:"))
print("check string index starts:",str1.startswith('v'))
print("check string index starts:",str1.startswith(str1,0,))


str2=(input("Enter a string:"))
suffix="patel"
print("check string index starts:",str2.endswith(suffix))
print("check string index starts:",str2.endswith(suffix,6,11))

