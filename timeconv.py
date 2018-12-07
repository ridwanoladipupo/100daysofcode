# Arithmetic & Expression
# Demonstrating with a Python program for time conversion.
# Note: this program gets an input from the users based on the number of seconds
# However, it computes and reports the time based on the Hours, Minutes and Seconds


#Get the numbers of seconds

seconds = eval(input("Please, enter the number of seconds:"))

# Firstly, compute the number of hours in the given number of seconds
hours = seconds // 3600

# Remaining seconds after the hour are accounted for
seconds = seconds % 3600

# Secondly, compute the number of minutes in the given number of seconds
minutes = seconds // 60

# Remaining seconds after the minutes are accounted for
seconds = seconds % 60

#Print the result

print(hours, "hrs", ":", minutes, ":", "min", ":", seconds, "sec")

