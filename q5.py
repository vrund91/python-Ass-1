'''Create a Python program that will have one list with values = [Navratri,Diwali,
  Holi,Rakshabandhan,Bakri Id, Muharram]. Perform following operations:
• Print whole list
• Print only first element of list
• Prints elements starting from 2nd till 3rd
• Prints elements starting from 2ndelement till last
• Print whole list 4 times using appropriate operator.'''

festival=['Navratri','Diwali','Holi','Rakshabandhan','Bakri-id','Muharram']

print("whole list:",festival)
print("only first element of list:",festival[0])
print("starting from 2nd till 3rd:",festival[1:3])
print("starting from 2ndelement till last:",festival[1:])
print("whole list 4 times using appropriate operator:",festival * 4)