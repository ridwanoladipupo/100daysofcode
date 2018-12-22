#Fibonacci series


nterms = 5

firstno = 0
secondno = 1
count = 0

if (nterms <= 0):
    print("Enter a +ve integer")

elif (nterms == 1):
    print("Fibonacci sequence upto", nterms, ":", firstno)

else:
    print("Fibonacci sequence upto", nterms, ":")
    while count < nterms:
        print(firstno, end =' , ')
        nth = firstno + secondno
        firstno = secondno
        secondno = nth
        count +=1


