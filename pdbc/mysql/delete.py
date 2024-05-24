import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',user='abhay',password='6541',database='users')
    cursor=dbcon.cursor() 
    sql_st='delete from user_list'
    cursor.execute(sql_st)
    dbcon.commit()
    print("all rows deleted")

   

except mysql.connector.Error as err:
    print(err) 

finally:
    cursor.close()
    dbcon.close()