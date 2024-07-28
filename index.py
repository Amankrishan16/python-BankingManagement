import random 
import mysql.connector 
 
db = mysql.connector.connect(host='localhost', 
username='root', password='shivam2002', database='datacamp') 
cursor = db.cursor() 
ctr = 0 
bank = 1 
while bank == 1: 
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
    print('Press 1 for Online Banking') 
    print('Press 2 for Registering a new bank account') 
    print('Press 3 for Deleting your account') 
    print('Press 4 for Customer Help Services') 
    print('Press 5 for exit') 
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
    choice = int(input("Option :- ")) 
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
    if choice == 1: 
        def welcome_message(): 
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
            print('WELCOME TO BANK OF INDIA') 
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
 
 
        def login(): 
            while True: 
                us = input("Enter your username :- ") 
                p = int(input("Enter your password :-")) 
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                value = (us, p) 
                query = """select * from customers where 
username=%s and password=%s """ 
                cursor.execute(query, value) 
                data_login = cursor.fetchall() 
                if len(data_login) != 0: 
                    globals()['ctr'] = 1 
                    break 
                else: 
                    print('LOGIN UNSUCCSESSFUL') 
                    print("USERNAME OR PASSWORD IS WRONG") 
                    
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
 
            return data_login 
 
 
        def interface(): 
            welcome_message() 
            b = login() 
            if globals()['ctr'] == 1: 
                i = b[0][0] 
                name = b[0][2] 
                print("LOGIN SUCCESSFUL") 
                print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                c = 1 
                while c == 1: 
                    print('Press 1 for depositing money') 
                    print('Press 2 for withdrawing money') 
                    print('Press 3 for doing kyc') 
                    print('Press 4 for checking balance') 
                    print('Press 5 for logging out') 
                    
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                    ch = int(input("Enter your option :- ")) 
                    if ch == 1: 
                        money_deposit = int(input('Amount to 
be deposited :- ')) 
                        
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                        cursor.execute('update customers set 
balance=balance+%s where id=%s', (money_deposit, i)) 
                        db.commit() 
                        q = 'select balance from customers 
where id=%s and username=%s' 
                        cursor.execute(q, (i, name)) 
                        a = cursor.fetchall() 
                        a = a[0] 
                        for x in a: 
                            print("Updated Balance :- ", x) 
                            
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                    elif ch == 2: 
                        money_withdrawn = int(input('Amount to 
be withdrawn :- ')) 
                        
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                        cursor.execute('update customers set 
balance=balance-%s where id=%s', (money_withdrawn, i)) 
                        db.commit() 
                        q = 'select balance from customers 
where id=%s and username=%s' 
                        cursor.execute(q, (i, name)) 
                        a = cursor.fetchall() 
                        a = a[0] 
                        for x in a: 
                            print("Updated Balance :- ", x) 
                            
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                    elif ch == 3: 
                        q = 'select kyc from customers where 
id=%s and username=%s' 
                        cursor.execute(q, (i, name)) 
                        a = cursor.fetchall() 
                        a = a[0] 
                        for x in a: 
                            condition = x 
                        if condition == 'false': 
                            print('For KYC you need to provide 
details from one of these government id') 
                            print('Press 1 for Aadhar Card') 
                            print('Press 2 for Voter Id Card') 
                            print('Press 3 for Pan Card') 
                            print('Press 4 for Driving 
License') 
                            
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                            cho = int(input("Enter your choice 
:- ")) 
                            
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                            if cho == 1: 
                                ad = int(input("Aadhar Number 
:- ")) 
                                cursor.execute('update 
customers set kyc="true" where id=%s and username=%s', (i, 
name)) 
                                db.commit() 
                                print("KYC Done") 
                            elif cho == 2: 
                                vi = int(input("Voter Id 
Number :- ")) 
                                cursor.execute('update 
customers set kyc="true" where id=%s and username=%s', (i, 
name)) 
                                db.commit() 
                                print("KYC Done") 
                            elif cho == 3: 
                                pc = int(input("Pan Card 
Number :- ")) 
                                cursor.execute('update 
customers set kyc="true" where id=%s and username=%s', (i, 
name)) 
                                db.commit() 
                                print("KYC Done") 
                            elif ch == 4: 
                                dl = int(input("Driving 
License Number :- ")) 
                                cursor.execute('update 
customers set kyc="true" where id=%s and username=%s', (i, 
name)) 
                                db.commit() 
                                print("KYC Done") 
                            else: 
                                print('Wrong Choice') 
                        else: 
                            print('KYC Already Done') 
                        
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                    elif ch == 4: 
                        q = 'select balance from customers 
where id=%s and username=%s' 
                        cursor.execute(q, (i, name)) 
                        a = cursor.fetchall() 
                        a = a[0] 
                        for x in a: 
                            print("Balance :- ", x) 
                            
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
                    elif ch == 5: 
                        c = 0 
                    else: 
                        print("Wrong Option ") 
                        
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
 
 
        interface() 
    elif choice == 2: 
        print('Fill these details to register your account ') 
        idea = random.randint(6, 100) 
        name = input("Enter your name :- ") 
        username = input('Enter your username :- ') 
        pas = int(input('Enter your password :- ')) 
        balance = float(input('Enter your balance :- ')) 
        age = int(input('Enter your age :- ')) 
        gender = input('Enter your gender (M/F) :- ') 
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
        kyc = 'false' 
        query = 'insert into customers 
values(%s,%s,%s,%s,%s,%s,%s,%s)' 
        value = (idea, name, username, pas, balance, age, 
gender, kyc) 
        cursor.execute(query, value) 
        db.commit() 
    elif choice == 3: 
        us = input("Enter your username :- ") 
        p = int(input("Enter your password :-")) 
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
        value = (us, p) 
        query = "select * from customers where username=%s and 
password=%s " 
        cursor.execute(query, value) 
        data_login = cursor.fetchall() 
        cursor.execute('delete from customers where id=%s and 
username=%s', (data_login[0][0], data_login[0][2])) 
        db.commit() 
    elif choice == 4: 
        print('help') 
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>') 
    elif choice == 5: 
        bank = 0 
    else: 
        print('Wrong Option') 
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
