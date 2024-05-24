import mysql.connector
import requests

resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

print(type(user_list))
data=[]
for user in user_list:
    data.append((user['id'],user['name'],user['email'],user['address']['city'],user['phone']))


try:
    con=mysql.connector.connect(host='localhost',user='abhay',password='6541',database='users')
    cursor=con.cursor()
    sql_st='''
            insert into user_list values(%s,%s,%s,%s,%s);
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