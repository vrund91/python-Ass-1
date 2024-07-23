'''Write a Python program that will demonstrate the use of Sting Functions'''

str1="hello, World! This is a sample string for demonstrating string functions"

print("first character capitalize the string:",str1.capitalize())

print("The counts number of substring in string strt to end:",str1.count("str",0,))

substr1="functions"
print("check index using endswith string:",str1.endswith(substr1))

substr1="functions"
print("return index begining & end:",str1.find(substr1))

substr2="ty2024"
print("check string is alphanumeric:",substr2.isalnum())

substr3="1234"
print("check string is Digit:",substr3.isdigit())

print("check string is lowercase:",substr1.islower())

substr4="HELLO"
print("check string is uppercase:",substr4.isupper())

print("Return length of object:",len(str1))

print("convert into lowercase:",substr4.lower())

print("convert into uppercase:",str1.upper())

print("swap character upper to lower & lower to upper:",str1.swapcase())