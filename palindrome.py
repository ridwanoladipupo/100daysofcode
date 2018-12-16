#Challenge: To check if a string is a palindrome or not


string = 'aIbohPhoBiA'

string = string.casefold()

reverse_string = reversed(string)

if (list(string) == list(reverse_string)):
    print(string + " is a palindrome")

else:
    print(string + " is not a palindrome")
