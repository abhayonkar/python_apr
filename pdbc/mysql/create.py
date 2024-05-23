import mysql.connector

dbcon = mysql.connector.connect(

  host="localhost",
  user="abhay",
  password="6541",
  database="users"
)

cur = dbcon.cursor()

sql_st = '''
    create table employee(
    eid int,
    ename varchar(32),
    esal int
    );
'''

cur.execute(sql_st)

print("created successfully")