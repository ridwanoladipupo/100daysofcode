from time import sleep

userPin =0000 #Take note, use '0000' for the Pin
balance = 0

def main():
    balance = 0
    print ("Welcome to RIDWAN ATM Machine")
    pin = int(input("Enter Your Password"))
    if(pin == userPin):
        startMenu(balance)
    else:
        print ("Invalid Password")
    
def startMenu(balance):
    print ("1  >>Deposit         2  <<Withdraw")
    print ("3  >>Recharge        4  <<Check Balance")
    print ("5  >>PayBill         6  <<QuickTeller")
    resp = int(input("Please enter Response"))
    if(resp == 1):
        balance = deposite(balance)
    elif(resp == 2):
        withdraw(balance)
    elif(resp ==4):
        print ("Your Current Balance is:",checkBalance(balance))
    
def deposite(balance):
    amount = int(input("Enter Amount You wish to deposite"))
    balance = balance + amount
    opt = int(input("Do you want to perform Anothr Operation Enter 1 for yes and 0 for no"))
    if(opt == 1):
        startMenu(balance)
    elif(opt ==0):
        print("Thank You for using This ATM Machine")
        sleep(3)
        exit()
    return balance
                
def withdraw(balance):
    widthamount = int(input("Enter Amount to Withdraw"))
    if(widthamount<balance):
        balance = balance - widthamount
        sleep(3)
        print ("Take Your Cash")
    else:
        print ("Insufficient Fund")
        opt = int(input("Do you want to perform Anothr Operation Enter 1 for yes and 0 for no"))
    if(opt == 1):
        startMenu(balance)
    elif(opt ==0):
        print("Thank You for using This ATM Machine")
        sleep(3)
        exit()
    return balance
def checkBalance(balance):
    return balance
main()
    
    
    
