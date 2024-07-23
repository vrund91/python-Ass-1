'''Create a Python program that will have one string variable =“Welcome to Python”.
Perform following operations:
• Print whole string
• Print only first character of string
• Print 3rdcharacter to -1 character of string using slicing operator
• Print string from 4thcharacter to the end of string using slicing operator
• Print whole string 5 times using appropriate operator'''

str1="Welcome to Python"
#Print the whole string
print("Print whole string:",str1)

#Print only the first character of the string
print("only first character:",str1[0])

#Print characters from 3rd to -1 (second-to-last)
print("3rdcharacter to -1 character of string:",str1[2:-1])

#Print characters from 4th character to the end
print("4th char to end char of string:",str1[3:])

#Print the whole string 5 times
print("whole string 5 times: " , str1 * 5)


