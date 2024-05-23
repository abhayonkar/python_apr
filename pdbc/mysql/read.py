import mysql.connector


try:
    dbcon = mysql.connector.connect(
        host="localhost",
        user="abhay",
        password="6541",
        database="users")
    
    cur = dbcon.cursor()
    sql_st = "select * from employee"
    cur.execute(sql_st)
    employe = cur.fetchall()

    for emp in employe:
        print(emp)

except mysql.connector.Error as err:
    print(err)

finally:
    cur.close()
    dbcon.close()