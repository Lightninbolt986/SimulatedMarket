import mysql.connector

db = mysql.connector.connect( # details daal dena yahan par
    host="",
    user="",
    password="",
    database=""
)

prices = {'hdfc':1232,'uco':11,'zomato':61,'hindustan_uni':2500,'cipla':920,'tata':450}


mc = db.cursor()

while True:
    ch=int(input('1.buy, 2. sell\n--> '))
    if ch==1:
        adno=input('admin no: ')
        company = input('company name(hdfc,uco,zomato,hindustan_uni,cipla,tata)\n--> ')
        amount = int(input("number of shares: "))
        mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            mc.execute(f"insert into students (admission_no,cash_in_hand,{company}) values ({adno},{5000-(prices[company]*amount)},{prices[company]*amount})")

        else:
            cash=fetch[0][0]
            comp=fetch[0][1]
            mc.execute(f"update students set cash_in_hand={cash-prices[company]*amount},{company}={comp+prices[company]*amount} where admission_no={adno}")

    elif ch==2:
        adno=input('admin no: ')
        company = input('company name(hdfc,uco,zomato,hindustan_uni,cipla,tata)\n--> ')
        amount = int(input("number of shares: "))
        mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            print('bro does not exist')
        else:
            cash=fetch[0][0]
            comp = fetch[0][1]
            mc.execute(f"update students set cash_in_hand={cash+prices[company]*amount},{company}={comp-prices[company]*amount} where admission_no={adno}")
    else:
        print('quit')


    db.commit()
    mc.execute(f'select * from students where admission_no={adno}')
    print(mc.fetchall())
