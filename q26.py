'''Write a Python program which will have Main Menu for performing following operations
 based on selection:
 Main Menu:
 Airthmetic Operation
 Identity Operator Operation
 Logical Operation
 Member Operator Operation
 Display proper message for every choice. Use elif to create a menu:'''

print("1. Arithmetic Operation")
print("2. Identity Operator Operation")
print("3. Logical Operation")
print("4. Membership Operator Operation")
print("5. Exit")

choice = int(input("Enter your choice: "))

if choice == 1:
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        arithmetic_choice = int(input("Enter your choice: "))

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if arithmetic_choice == 1:
            result = num1 + num2
            print("Result:", result)
        elif arithmetic_choice == 2:
            result = num1 - num2
            print("Result:", result)
        elif arithmetic_choice == 3:
            result = num1 * num2
            print("Result:", result)
        elif arithmetic_choice == 4:
            if num2 == 0:
                print("Error! Division by zero.")
            else:
                result = num1 / num2
                print("Result:", result)
        else:
            print("Invalid choice")

elif choice == 2:
       var1='Hello'
       var2='Hello'
       var3='World'
       var4=123
       var5=123
       print(var1 is var2)
       print(var3 is var1)
       print(var4 is var5)
       print(var3 is not var2)

elif choice == 3:
        print("1. AND")
        print("2. OR")
        print("3. NOT")

        logical_choice = int(input("Enter your choice: "))

        if logical_choice == 1:
            bool1 = bool(input("Enter first boolean: "))
            bool2 = bool(input("Enter second boolean: "))
            result = bool1 and bool2
            print("Result:", result)

        elif logical_choice == 2:
            bool1 = bool(input("Enter first boolean : "))
            bool2 = bool(input("Enter second boolean : "))
            result = bool1 or bool2
            print("Result:", result)

        elif logical_choice == 3:
            bool1 = bool(input("Enter a boolean: "))
            result = not bool1
            print("Result:", result)

        else:
            print("Invalid choice")

elif choice == 4:
        range_user=["varun","ravi","amrit","nitin"]
        name=input("Enter your name:")

        if name in range_user:
             print(name in range_user,"Access granted")
        else:
             print(name in range_user,"Access denied")

elif choice == 5:
        print("Exit")

else:
     print("Invalid choice")
