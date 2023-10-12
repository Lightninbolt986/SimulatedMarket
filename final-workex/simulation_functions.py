import mysql.connector
def insert(adno,company,amount,prices):
    try:
        db=mysql.connector.connect(host='localhost', user='root', password='', database='')
        mc= db.cursor()
        mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
        fetch= mc.fetchall()
        mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            mc.execute(f"insert into students (admission_no,cash_in_hand,{company}) values ({adno},{5000-(prices[company]*amount)},{amount})")

        else:
            cash=fetch[0][0]
            comp=fetch[0][1]
            mc.execute(f"update students set cash_in_hand={cash-prices[company]*amount},{company}={comp+amount} where admission_no={adno}")
        db.commit()
        db.close()
    except Exception as e:
        db.close()

        return e




def delete(adno,company,amount,prices):
    try:
        db=mysql.connector.connect(host='localhost', user='root', password='', database='')
        mc= db.cursor()
        mc.execute(f'select cash_in_hand,{company} from students where admission_no={adno}')
        fetch= mc.fetchall()

        if fetch==[]:
            return 'bro does not exist'
        else:
            cash=fetch[0][0]
            comp = fetch[0][1]
            mc.execute(f"update students set cash_in_hand={cash+prices[company]*amount},{company}={comp-amount} where admission_no={adno}")
        db.commit()
        db.close()
    except Exception as e:
        db.close()
        print(e)
        return e
