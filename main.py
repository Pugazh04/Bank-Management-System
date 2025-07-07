import mysql.connector as m 
import random 
db=m.connect(host='localhost',user='root',password='123456') 
c=db.cursor() 
c.execute("use indian_bank") 
 
print(""" 
What do you wish to do?? 
1.Create Account 
2.Deposit amount in your account 
3.View Account 
4.Exit""") 
 
res=int(input("enter your choice (1/2/3/4)")) 
if res==1: 
    new_account() 
elif res==2: 
    deposit() 
elif res==3: 
    search() 
elif res==4: 
    print("thank you visit again") 
else: 
    print("invalid choice") 
 
def new_sb(): 
    print('Savings Bank Account Opening Form') 
    sb_date=input("""Enter date of opening account in words Example: 24th November 20xx""") 
    sb_bank=input('Account to be opened at Branch : ') 
    acc_type="SB" 
    status="ACTIVE" 
  
    BO_ID=0 
    if sb_bank=="Ambattur" or "AMBATTUR" or "ambattur": 
        BO_ID=1438756902 
    elif sb_bank=="Kolathur" or "KOLATHUR" or "kolathur": 
        BO_ID=1438738746 
    elif sb_bank=="Mogappair" or "MOGAPPAIR" or "mogappair": 
        BO_ID=1438790006 
    elif sb_bank=="Villivakkam" or "VILLIVAKKAM" or "villivakkam": 
        BO_ID=1438756912 
    else: 
        print("Sorry, we don't have branches there") 
    i=str(BO_ID) 
    sb_name1=input('First Applicant Name (in full) : ') 
    sb_rel_name=input('Father/Husband/Guardian Name : ') 
    sb_add=input('Residential address : ') 
    sb_city=input('Village/City : ') 
    sb_district=input('District : ') 
    sb_state=input('State : ') 
    sb_code=input('Pincode : ') 
    sb_phone_no=input('Telephone/Landline : ') 
    sb_Mobile_no=input('Mobile No. : ') 
    sb_email=input('E-mail address : ') 
    sb_gender=input('Male/Female : ') 
    sb_dob=input('Date of Birth (dd/mm/yyyy) : ') 
    sb_occ=input('Occupation : ') 
    sb_req_card=input('Request for ATM debit card (Yes/No) : ') 
    sb_req_sms=input('SMS Alert (Yes/No) : ') 
    nom=input('Nomination Required (Yes/No) : ') 
    if nom=='Yes':
        nom_name=input('Nominee Name : ') 
        nom_dob=input('Nominee Date of Birth (dd/mm/yyyy) : ') 
        nom_age=input('Nominee Age : ') 
        nom_rel=input('Nominee Relationship with depositor (if any) : ') 
        nom_add=input('Nominee Address : ') 
    print('Documents accepted as proof of identity:') 
    print('''1. Passport 
             2. PAN card 
             3. Voter's Identity Card 
             4. Driving License''') 
    print('Documents accepted as proof of address:') 
    print('''1. Ration Card 
             2. Electricity Bill 
             3. Telephone Bill 
             4. Bank Account Statement''') 
    sb_acc_no=random.randint(10000000,99999999) 
    print('Congrats! Your account has got created successfully ') 
    print('Your Account Number : ',sb_acc_no) 
    y=str(sb_acc_no) 
    c.execute("insert into bank_dbms values (' "+sb_name1+" ',' "+sb_date+" ',' "+sb_bank+" ',' "+i+" ',' "+acc_type+" ',' "+y+" ',' "+status+" ',0,0,0)") 
    db.commit() 
               
def new_fd(): 
    print('Fixed Deposit Account Opening Form') 
    exist=input('Are you an existing customer (Yes/No) ?') 
    if exist=='Yes': 
        print('Your Details') 
        fd_bank=input('Account to be opened at Branch : ') 
 
        BO_ID=0 
        if fd_bank=="Ambattur" or "AMBATTUR" or "ambattur": 
            BO_ID=1438756902 
        elif fd_bank=="Kolathur" or "KOLATHUR" or "kolathur": 
            BO_ID=1438738746 
        elif fd_bank=="Mogappair" or "MOGAPPAIR" or "mogappair": 
            BO_ID=1438790006 
        elif fd_bank=="Villivakkam" or "VILLIVAKKAM" or "villivakkam": 
            BO_ID=1438756912 
        else: 
            print("Sorry, we don't have branches there") 
     
        fd_name=input('Applicant Name (in full) : ') 
        fd_dob=input('Date of Birth (dd/mm/yyyy) : ') 
        fd_add=input('Residential address : ') 
        fd_city=input('Village/City : ') 
        fd_district=input('District : ') 
        fd_state=input('State : ') 
        fd_code=input('Pincode : ') 
        fd_phone_no=input('Telephone/Landline : ') 
        fd_Mobile_no=input('Mobile No. : ') 
        fd_email=input('E-mail address : ') 
 
        print('Fixed Deposit Details') 
         
        fd_amt=int(input('Amount to be deposited : ')) 
        fd_tenure=int(input('Tenure : ')) 
        fd_rate_of_int=int(input('Rate of interest (p.a): ')) 
         
        print('Maturity Instructions') 
         
        print('1-->Renew Principal and interest') 
        print('2-->Renew Principal and pay interest') 
        print('3-->Do not Renew') 
        fd_renew_opt=input('Enter your renew option (1/2/3) : ') 
        if fd_renew_opt==1 or 2 or 3: 
            print('''Payment of interest on maturity by 
                     1. Transfer to savings account 
                     2.Manager's cheque to mailing address''') 
            fd_poi=int(input('Enter (1/2) : ')) 
            if fd_poi==1: 
                acc_no1=int(input('Enter your Savings Bank account no. : ')) 
                 
    if exist=='No': 
        print('Please complete the below new account opening form for a savings account') 
        new_sb() 
         
 
def new_rd(): 
    rd_bank=input('Account to be opened at Branch : ') 
    rd_date=input("""Enter date of opening account in words Example: 24th November 20xx""") 
    acc_type="RD" 
    BO_ID=0 
    if rd_bank=="Ambattur" or "AMBATTUR" or "ambattur": 
        BO_ID=1438756902 
    elif rd_bank=="Kolathur" or "KOLATHUR" or "kolathur": 
        BO_ID=1438738746 
    elif rd_bank=="Mogappair" or "MOGAPPAIR" or "mogappair": 
        BO_ID=1438790006 
    elif rd_bank=="Villivakkam" or "VILLIVAKKAM" or "villivakkam": 
        BO_ID=1438756912 
    else: 
        print("Sorry, we don't have branches there") 
    i=str(BO_ID) 
    rd_name1=input('First Applicant Name (in full) : ') 
    rd_dob=input('Date of Birth (dd/mm/yyyy) : ') 
    rd_add=input('Residential address : ') 
    rd_city=input('Village/City : ') 
    rd_district=input('District : ') 
    rd_state=input('State : ') 
    rd_code=input('Pincode : ') 
    rd_phone_no=input('Telephone/Landline : ') 
    rd_Mobile_no=input('Mobile No. : ') 
    rd_email=input('E-mail address : ') 
 
    print('Recurring Deposit Details') 
         
    rd_amt=int(input('Monthly Installment amount : ')) 
    rd_tenure=int(input('Tenure : ')) 
    rd_rate_of_int=int(input('Rate of interest (p.a): ')) 
 
    rd_acc_no=random.randint(10000000,99999999) 
    print('Congrats! Your account has got created successfully ') 
    print('Your Account Number : ',rd_acc_no) 
    y=str(rd_acc_no) 
      
    c.execute("insert into bank_dbms values (' "+rd_name1+" ',' "+rd_date+" ',' "+rd_bank+" ',' "+i+" ',' "+acc_type+" ',' "+y+" ',' "+status+" ',0,0,0)") 
    db.commit() 
 
def new_account(): 
    print('Welcome to Indian Bank') 
    acc_type= input('Which type of account you wish to choose \n 1. Savings Bank account \n 2. Fixed deposit account \n 3. Recurring deposit account') 
 
    if acc_type=='Savings Bank account': 
        new_sb() 
   elif acc_type=='Fixed deposit account': 
        new_fd() 
   elif acc_type=='Recurring deposit account': 
        new_rd() 
 
def deposit(): 
    m=int(input("""enter the type of account 
                           1.Savings Bank Account 
                           2.Recurring Deposit Account 
                           3.Fixed Deposit Account""")) 
    def sb(): 
        t=input("enter account number") 
        c.execute("select debit_balance from bank_dbms where account_number= ' " +t+ " ' ") 
        d=0 
        for i in c: 
            d=i[0] 
        c.execute("select cumulative_balance from bank_dbms where account_number=' "+t+"'") 
        k=0 
        for w in c: 
            k=w[0] 
        s=int(input("enter amount to be deposited")) 
        f=d+s 
        g=k+s 
        r=str(f) 
        q=str(g) 
        c.execute("update bank_dbms set debit_balance= ' "+r+" ' where account_number= '"+t+"'") 
        db.commit() 
        c.execute("update bank_dbms set cumulative_balance= ' "+q+" ' where account_number= '"+t+"'") 
        db.commit() 
        c.execute("select * from bank_dbms where account_number= ' "+t+" ' ") 
         
        for j in c: 
            print(j) 
     
 
   def rd(): 
        p=input("enter account number") 
        c.execute("select debit_balance from bank_dbms where account_number= ' " +p+ " ' ") 
        y=0 
        for i in c: 
            y=i[0] 
        c.execute("select cumulative_balance from bank_dbms where account_number=' "+p+"'") 
        h=0 
        for w in c: 
            h=w[0] 
        s=int(input("enter amount to be deposited")) 
        f=y+s 
        g=h+s 
        r=str(f) 
        q=str(g) 
        c.execute("update bank_dbms set debit_balance= ' "+r+" ' where account_number= '"+p+"'") 
        db.commit() 
        c.execute("update bank_dbms set cumulative_balance= ' "+q+" ' where account_number= '"+p+"'") 
        db.commit() 
        c.execute("select * from bank_dbms where account_number= ' "+p+"'") 
        for j in c: 
            print(j) 
         
 
    def fd(): 
        t=input("enter account number") 
        c.execute("select debit_balance from bank_dbms where account_number= ' " +t+ " ' ") 
        p=0 
        for i in c: 
            p=i[0] 
        c.execute("select cumulative_balance from bank_dbms where account_number=' "+t+"'") 
        e=0 
        for w in c: 
            e=w[0] 
        s=int(input("enter amount to be deposited")) 
        f=p+s 
        g=e+s 
        r=str(f) 
        q=str(g) 
        c.execute("update bank_dbms set debit_balance= ' "+r+" ' where account_number= '"+t+"'") 
        c.execute("update bank_dbms set cumulative_balance= ' "+q+" ' where account_number= '"+t+"'") 
        c.execute("select * from bank_dbms where account_number= ' "+t+"'") 
        for j in c: 
            print(j) 
    print(‘1-> Savings Bank Account\n2-> Recurring deposit Account\n3-> Fixed Deposit Account’)
    m= int(input(‘Enter your choice : ‘)              
    if m==1: 
        sb() 
    elif m==2: 
        rd() 
    elif m==3: 
        fd() 
    else: 
        print("invalid choice") 
 
def search(): 
    x=input('enter your account number') 
    c.execute("select * from bank_dbms where account_number= ' "+x+" ' ") 
    for i in c: 
        print(i) 
 
 
