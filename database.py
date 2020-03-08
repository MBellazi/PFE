
import mysql.connector

database_name = "ffff"
tables = ["person","candidat"]

conn = mysql.connector.connect(host ="localhost",user="root",passwd="")
cursor = conn.cursor()

db_exist = False

# if database exist 
cursor.execute("SHOW DATABASES")
for db in cursor:
    if db == database_name:
        conn = mysql.connector.connect(host ="localhost",user="root",passwd="", db=database_name)
        db_exist = True

if db_exist == False :       
    cursor.execute("CREATE DATABASE " + database_name)
    conn = mysql.connector.connect(host ="localhost",user="root",passwd="",db=database_name)  

sql_create_table = "create table "+ tables[0] + "(id int(20) primary key auto_increment, firstname char(20) not null,lastname char(20) not null)"
sql_create_table2 = "create table "+ tables[1] +"(id_candidat int(20) primary key auto_increment,nom char(20) not null,prenom char(20) not null)"

# check if table exists:
cursor.execute("SHOW TABLES")
first_table_exist = False
second_table_exist = False

for table in cursor:
    if table == tables[0]:
        first_table_exist = True
    if table == tables[0]:
        first_table_exist = True
if first_table_exist == False:
    cursor.execute(sql_create_table)
if second_table_exist == False:
    cursor.execute(sql_create_table2)

conn.commit()
conn.close()