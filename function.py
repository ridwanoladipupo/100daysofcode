# Function
# Demonstrating function with the challenge below
# Challenge : FACTORIAL, PERMUTATION AND COMBINATION

def computation():
    # Accepting value for for n, r
    n = int(input("Enter value for n :"))
    r = int(input("Enter value for r :"))
    
    y = n - r # n-r!
    
    nfact = 1
    rfact = 1
    yfact = 1

    
    perm = 1
    comb = 1


    for i in range (n):
        nfact = nfact * n
        n = n - 1

    for i in range (r):
        rfact = rfact * r
        r = r - 1

    for i in range (y):
        yfact = yfact * y
        y = y - 1


    # Permutation
    perm = nfact / yfact

    # Combination
    comb = (nfact / (yfact * rfact))
    
    print("n! = ", nfact)
    print("r! = ", rfact)
    print("(n - r)! = ", yfact)
    print("permutation = ", perm)
    print("combination = ", comb)

computation()
