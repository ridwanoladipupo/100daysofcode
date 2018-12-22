import time

accountOwner = "Ridwan OLADIPUPO"
userPin = 1234
balance = 0

def main():
    print ("Welcome to Zenith Bank ATM")
    pin = int(input("ENTER YOUR PIN"))
    print("")
    if (pin == userPin):
        time.sleep(2)
        initiateProcess()
    else:
        print("Sorry, the PIN is not Correct")
        main()
  
    
def initiateProcess():
    print ("1 >> Deposit")
    print ("2 >> Withdraw")
    print ("3 >> Check Balance")
    print ("4 >> Pay Bill")
    print ("5 >> Recharge")
    print ("6 >> Exit")

    optionv = int(input("Pls Select the Code"))

    if(optionv == 1):
        deposit()
    elif(optionv == 2):
        withdraw()
    elif(optionv == 3):
        checkBalance()
    elif(optionv == 4):
        payBill()
    elif(optionv == 5):
        Recharge()
    elif(optionv == 6):
        exitapp()
    else:
        initiateProcess()
    

def deposit(balance):
    amounttodeposit = int(input("Enter Amount to Deposit"))
    balance = balance + amounttodeposit
    print("Pls Wait...")
    time.sleep(2)
    print ("Your Deposit of ",amounttodeposit, " has been Processed,Your New Balance = ",balance)


def withdraw(balance):
      amounttowithdraw = int(input("Enter Amount to Withdraw"))
      print("Pls Wait...")
      time.sleep(2)
      if amounttowithdraw < balance:
           print ("Pls take your Cash of ",amounttowithdraw)
      else:
            print("Sorry, your Balance is not Sufficient, Kindly Deposit Funds into your Account")
            deposit()


def checkBalance(balance):
    print("Pls Wait...")
    time.sleep(2)
    print ("Your Balance is ",balance)

def payBill(balance):
    print("Print Select the Service/Vendor you want to Pay")
    print("")
    print ("1 >> Air Nigeria")
    print ("2 >> DSTV")
    print ("3 >> JAMB")
    print ("4 >> AAUA")

    optionv = int(input("Pls Select the Code for the Service/Vendor you want to pay :"))

    if optionv == 1:
        amounttoPay = int(input("Enter Amount to Pay to Air Nigeria"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoPay < balance:
                print ("You have Paid the Sum of ",amounttoPay," to Air Nigeria")
            else:
                print("Sorry, your Balance is not Sufficient")

    if optionv == 2:
        amounttoPay = int(input("Enter Amount to Pay to DSTV"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoPay < balance:
                print ("You have Paid the Sum of ",amounttoPay," to DSTV")
            else:
                print("Sorry, your Balance is not Sufficient")


   if optionv == 3:
        amounttoPay = int(input("Enter Amount to Pay to JAMB"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoPay < balance:
                print ("You have Paid the Sum of ",amounttoPay," to JAMB")
            else:
                print("Sorry, your Balance is not Sufficient")

   if optionv == 4:
        amounttoPay = int(input("Enter Amount to Pay to AAUA"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoPay < balance:
                print ("You have Paid the Sum of ",amounttoPay," to AAUA")
            else:
                print("Sorry, your Balance is not Sufficient")
                
def Recharge(balance):
    print("Print Select the Network Provider")
    print("")
    print ("1 >> AIRTEL")
    print ("2 >> 9MOBILE")
    print ("3 >> GLO")
    print ("4 >> MTN")
    print("")
    
    optionv = int(input("Pls Select the Code for the Network Provider"))

    if optionv == 1 :
        amounttoBuy = int(input("Enter Amount"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoBuy < balance:
                print ("You have Purchase the Sum of ",amounttoBuy," Airtime")
            else:
                print("Sorry, your Balance is not Sufficient")

    if optionv == 2:
        amounttoBuy = int(input("Enter Amount"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoBuy < balance :
                print ("You have Purchase the Sum of ",amounttoBuy," Airtime")
            else:
                print("Sorry, your Balance is not Sufficient")


   if optionv == 3:
        amounttoBuy = int(input("Enter Amount"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoBuy < balance:
                print ("You have Purchase the Sum of ",amounttoBuy," Airtime")
            else:
                print("Sorry, your Balance is not Sufficient")

   if optionv == 4 :
        amounttoBuy = int(input("Enter Amount"))
        print("Pls Wait...")
        time.sleep(2)
            if amounttoBuy < balance:
                print ("You have Purchase the Sum of ",amounttoBuy," Airtime")
            else:
                print("Sorry, your Balance is not Sufficient")


def exitapp():
    main()
        
                 

    
    
