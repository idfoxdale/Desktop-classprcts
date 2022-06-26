#make a palindrome function that takes a string and returns a boolean
# True if the string is a palindrome, False if not
# a palindrome is a string that is the same forwards and backwards
# for example, 'racecar' is a palindrome
# 'hello' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 'racecars' is not a palindrome
# 'racecar' is a palindrome
# 
# Hint: you can use the built in function len() to get the length of a string
# Hint: you can use the built in function str() to convert a number to a string
# Hint: you can use the built in function int() to convert a string to an integer
string1 = input("Enter a string: ")
string2 = string1[::-1]
if string1 == string2:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
#make a palindrome function that takes a string and returns a boolean   
# True if the string is a palindrome, False if not
