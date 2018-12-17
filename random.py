#Importing classes from module
#Demonstrating the use of random

from random import randrange

firstplayer = 0
secondplayer = 0


print("1st Player Throw")
for i in range (5):
    rand = randrange(6) + 1
    print("", rand)
    firstplayer = firstplayer + rand

print("Sum throw = ", firstplayer)

print("2nd Player Throw")
for i in range (5):
    rand = randrange(6) + 1
    print("", rand)
    secondplayer = secondplayer + rand

print("Sum throw = ", secondplayer)
    
if (firstplayer > secondplayer):
    print("The winner is Player 1!!")
elif (firstplayer < secondplayer):
    print("The winner is Player 2!!")
else:
    print("Draw, please rethrow!!")
