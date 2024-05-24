import mysql.connector
import requests

resp=requests.get('https://dummyjson.com/products')
user_list=resp.json()

data=[]
for user in user_list['products']:
    data.append((user['id'], user['title'], user['price'], user['brand']))

try:
    con=mysql.connector.connect(host='localhost',user='abhay',password='6541',database='users')
    cursor=con.cursor()
    sql_st='''
            insert into products values(%s,%s,%s,%s);
           '''
    #data = [(102,'sonia',65000),(103,'priyanka',75000)]
    cursor.executemany(sql_st,data)
    con.commit()
    print("Data inserted successfully")
except mysql.connector.Error as err:
    print(err)
finally:
    con.close()
    cursor.close()