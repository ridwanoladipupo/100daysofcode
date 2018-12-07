# Conditional execution
# Demonstrating the conditional execution and selection control stucture based on If, If-Else-If,Else-If with a python program that captures students grade and computes his/her grade
# Note, in Nigerian grading system, the scores and the equivalent grades are as follows:
# 70 - 100 : A
# 60 - 69 : B
# 50 - 59 : C
# 45 - 49 : D
# 40 - 44 : E
# 0 - 39 : F

# Capturing student score

score = int(input("Enter your score:"))

if (score >= 0 and score <= 100):
    if (score >= 70 and score <= 100):
        print("Your Grade is A")
    elif (score >= 60 and score <= 69):
        print("Your Grade is B")
    elif (score >= 50 and score <= 59):
        print("Your Grade is C")
    elif (score >= 45 and score <= 49):
        print("Your Grade is D")
    elif (score >= 40 and score <= 44):
        print("Your Grade is E")
    else:
        print("Your Grade is F")
else:
    print("Please, input the correct score")
