'''Write a Python program which will have Main Menu for selecting Elective Subjects as
follows:
Main Menu:
1. Joomla
2. Ruby onRails
3. Drupal
4. Android
5. iOS
Display proper message for every choice. Use elif to create a menu:'''


print("Menu:")
print("1.joomla")
print("2.Ruby OnRails")
print("3.Drupal")
print("4.Android")
print("5.ios")

choice=(input("Enter a your choice:"))

if choice == '1':
    print("You have selected joomla.")
elif choice == '2':
    print("You have selected Ruby OnRails.")
elif choice == '3':
    print("You have selected Drupal.")
elif choice == '4':
    print("You have selected Android.")
elif choice == '5':
    print("You have selected ios.")