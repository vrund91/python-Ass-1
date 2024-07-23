'''Write a Python program which have string str = “Hello World”,count how many times "l"
 is repeated in str using count()function.'''

str1="Hello world"
sub="l"
print(f"Number of '{sub}' in '{str1}':",str1.count(sub))
print(f"Number of '{sub}' in '{str1}'(start to end):",str1.count(sub,0,))