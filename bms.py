import os
import msvcrt
class atm:
    account_no=0
    name = ''
    pin=0
    balance=0.0
    mobile=''
    
    def __init__(self,a,n,p,b,m):
        self.account_no=a
        self.name=n
        self.pin=p
        self.balance=b
        self.mobile=m
    def getaccount(self):
        return self.account_no
    def getname(self):
        return self.name
    def getpin(self):
        return self.pin
    def getbalance(self):
        return self.balance
    def getmobile(self):
        return self.mobile
    def withdraw(self,amount):
        if(amount>0 and amount<self.balance):
            self.balance-=amount;
            print("Please Collect Your Cash")
            print(f"Available Balance : {self.balance} ")
            char = msvcrt.getch()
        else:
            print("Insufficient Balance!!")
            char = msvcrt.getch()
        

def sw(choice):
    if choice==1:
        print(f"Your bank balance is : {user1.getbalance()}")
        char = msvcrt.getch()
    elif choice==2:
        am = int(input("Enter an amount to withdraw : "))
        user1.withdraw(am)
    elif choice==3:
        print(f"*** User Details are :- ")
        print(f"-> Account no: {user1.getaccount()}")
        print(f"-> Name :      {user1.getname()}")
        print(f"-> Balance :  {user1.getbalance()}")
        print(f"-> Mobile No. : {user1.getmobile()}")
        char = msvcrt.getch()
    elif choice==4:
        print("4. Update Mobile no.")
        char = msvcrt.getch()
    elif choice==5:
        exit(0)
        
    
user1 = atm(1234567, "Tim", 1111, 45000.90, "9087654321")
#user1.__init__(1234567, "Tim", 1111, 45000.90, "9087654321")
on = True
while on:
    os.system('cls')
    print("*****Welcome to ATM****")
    accNum= int(input("Enter your account number : "))
    enterPin=int(input("Enter PIN : "))
    if((accNum==user1.getaccount())and(enterPin==user1.getpin())):
        while 1:
            os.system('cls')
            print("**** Welcome to ATM *****")
            print("Select Options ")
            print("1. Check Balance")
            print("2. Cash withdraw")
            print("3. Show User Details")
            print("4. Update Mobile no.")
            print("5. Exit")
            choice= int(input("Enter your Choice: "))
            sw(choice)
            
    else:   
        print("User Details are Invalid !!! ")
        on=False