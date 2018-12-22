# Conditional execution
# Demonstrating the Iterative control structure with a python program that allows users to specify loop range, -
# detects the loop elements based on [EVEN AND ODD] and display to the screen the odd integers and even integers.

# Loop specifier

looprange = int(input("Indicate the loop range:"))

# Looping

for i in range (looprange):
    if (i%2 == 0):
        print ("Even integer :", i)
    elif (i%2 == 1):
        print ("Odd integer:", i)


