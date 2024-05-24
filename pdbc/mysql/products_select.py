import mysql.connector

try:
    dbcon = mysql.connector.connect(
        host="localhost",
        user="abhay",
        password="6541",
        database="users")

    cur = dbcon.cursor()
    b_name = input("Enter the brand name:")

    # Use a placeholder in the query
    sql_st = "SELECT * FROM products WHERE brand = %s"

    # Pass the user input as a separate argument to execute()
    cur.execute(sql_st, (b_name,))
    employe = cur.fetchall()

    for emp in employe:
        print(emp)

except mysql.connector.Error as err:
    print(err)

finally:
    cur.close()
    dbcon.close()
