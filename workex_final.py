
import mysql.connector
# create table student_data(admission_no char(4) primary key, cash_in_hand float not null default 5000, hdfc float default 0, uco float default 0, zomato float default 0, hindustan_uni float default 0, cipla float default 0, tata float default 0);
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Buddyoo7",
    database="workexdb"
)

prices = {'hdfc':1232,'uco':11,'zomato':61,'hindustan_uni':2500,'cipla':920,'tata':450}


mc = db.cursor()

while True:
    ch=int(input('1.buy, 2. sell\n--> '))
    if ch==1:
        adno=input('admin no: ')
        company = input('company name(hdfc,uco,zomato,hindustan_uni,cipla,tata)\n--> ')
        amount = int(input("number of shares: "))
        mc.execute(f'select cash_in_hand,{company} from student_data where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            mc.execute(f"insert into student_data (admission_no,cash_in_hand,{company}) values ({adno},{5000-(prices[company]*amount)},{prices[company]*amount})")

        else:
            cash=fetch[0][0]
            comp=fetch[0][1]
            mc.execute(f"update student_data set cash_in_hand={cash-prices[company]*amount},{company}={comp+prices[company]*amount} where admission_no={adno}")

    elif ch==2:
        adno=input('admin no: ')
        company = input('company name(hdfc,uco,zomato,hindustan_uni,cipla,tata)\n--> ')
        amount = int(input("number of shares: "))
        mc.execute(f'select cash_in_hand,{company} from student_data where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            print('bro does not exist')
        else:
            cash=fetch[0][0]
            comp = fetch[0][1]
            mc.execute(f"update student_data set cash_in_hand={cash+prices[company]*amount},{company}={comp-prices[company]*amount} where admission_no={adno}")
    else:
        print('quit')


    db.commit()
    mc.execute(f'select * from student_data where admission_no={adno}')
    print(mc.fetchall())
