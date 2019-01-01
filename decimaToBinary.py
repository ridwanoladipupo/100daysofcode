# Python function to convert from Binary -> Decimal

def decToBinary(n):
    k = []

    while (n>0):
        a = int(float(n%2))
        k.append(a)
        n = (n-a)/2

    k.append(0)

    string = ""
    for j in k[:: -1]:
        string = string + str(j)
    print("The binary no. is", string)
    
n = int(input("Enter value of n :"))

decToBinary(n)


