'''Write a Python program which asks the user to input a string and perform lstrip and rstrip 
function on input string.'''

str1=(input("Enter a string:"))
print("Remove Leading  character:",str1.lstrip('@'))

str2=(input("Enter a string:"))
print("Remove Trailing character:",str2.rstrip('@'))

str3=(input("Enter a string:"))
print("Removes Both Leading and Trailing whitespace character:",str3.lstrip())