from datetime import datetime
def isnot_expired(expire_date_str):
    date_format = "%m/%y"
    expire_date = datetime.strptime(expire_date_str, date_format)
    current_date = datetime.now().replace(day=1)
    if current_date > expire_date:
        return False
    else:
        return True
    
id1=1234567891234567
id2=1234512345123456
bank ={
    id1:{
        "card holder name":"Mina Adel Botros 2211",
        "balance":20000,
        "expire date":"05/26"
        },
    id2:{
        "card holder name":"Ahmed Mohamed Ahmed 2211",
        "balance":300000,
        "expire date":"05/27"
        }    
    }
PAN=int(input("please enter your ID : "))
c1=0
while(PAN not in bank.keys()):
    c1+=1
    if c1==3:
        break
    print("not valid please try again")    
    PAN=int(input("please enter your ID : "))
if c1!=3:
    key=PAN
    name=input("please enter your card holder name : ")
    card_name1=name.title()
    card_name=card_name1.strip()
    if card_name==bank[key]["card holder name"]:
        expdate1=input("please enter the expire date of the card : ")
        expdate2=expdate1.zfill(5)
        if expdate2==bank[key]["expire date"] and isnot_expired(expdate2) :
            operation=input("please choose a number for an operation : \n1-deposite \n2-check balance \n3-transaction \n: ")
            if operation =="deposite" or operation=="1":
                print("your balancce before deposition is ",bank[key]["balance"])
                dep_amount=int(input("please enter the amount you want to deposite : "))
                bank[key]["balance"]+=dep_amount
                print("successful pocess your balance after deposition is", bank[id1]["balance"])
            elif operation=="check balance" or operation== "2":
                print(bank[key]["balance"])
            elif operation=="transaction" or operation=="3":
                print("your balancce before transaction is ",bank[key]["balance"])
                tran_amount=int(input("please enter an amount that is less than or equal ten thousand and less than or equal your balance to withdraw  :"))
                if tran_amount<=10000 and bank[key]["balance"]>=tran_amount :
                    bank[key]["balance"]-=tran_amount
                    print("successful pocess your balance after transaction is", bank[key]["balance"])
                elif tran_amount>10000:
                    print("failed procees the amount of money must be less than ten thousand ")
                elif bank[key]["balance"]>=tran_amount:
                    print("failed process you don't have this much amount of money in your balance")
            else:
                print("failed process please check tht you enter the correct operation number or letters")
        elif isnot_expired(expdate2) == False:
            print("your card has expired") 
        else:
            print("failed process please check that you enter the correct expire date ")
    else:
        print("failed process please check that you enter the correct card name holder")
else:
    print("failed process please check that you enter the correct account id number and try again later")
                              