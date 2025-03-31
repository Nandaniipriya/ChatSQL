import sqlite3
## connect to sqlite
connection=sqlite3.connect("student.db")
## create a cursor object to insert record, create table
cursor=connection.cursor()

## create a table
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)
## insert records into the table
cursor.execute("insert into STUDENT values('John','Data Science','A',90)")
cursor.execute("insert into STUDENT values('Jane','Data Science','B',85)")
cursor.execute("insert into STUDENT values('Doe','Data Analyst','C',88)")
cursor.execute("insert into STUDENT values('Alice','DEVOPS','A',92)")
cursor.execute("insert into STUDENT values('Bob','DEVOPS','B',80)")

## DISPLAY RECORDS
print("The inserted records are")
data=cursor.execute("select * from STUDENT")
for row in data:
    print(row)
    
## COMMIT THE CHANGES IN THE DATABASE
connection.commit()
## CLOSE THE CONNECTION
connection.close()