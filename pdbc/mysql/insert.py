import mysql.connector

dbcon = mysql.connector.connect(

  host="localhost",
  user="abhay",
  password="6541",
  database="users"
)

cur = dbcon.cursor()

sql_st = '''
    insert into employee values(101, "rahul", 4567)
'''

cur.execute(sql_st)
dbcon.commit()

print("data inserted successfully")