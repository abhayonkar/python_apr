import mysql.connector
try:
    dbcon = mysql.connector.connect(
        host="localhost",
        user="abhay",
        password="6541",
        database="users")
    
    cur = dbcon.cursor()
    sql_st = ''' insert into employee(eid,ename,esal) values(%s, %s, %s)'''
    data = [(102,'sonia', 5823),(103,'priya',6723)]

    cur.executemany(sql_st,data)

    dbcon.commit()

    print("success")

except mysql.connector.Error as err:
    print(err)

finally:
    cur.close()
    dbcon.close()