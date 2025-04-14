import sqlite3

##Connect to sqlite
connection=sqlite3.connect("student.db")

##Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

##create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""


cursor.execute(table_info)

##Insert some more records

cursor.execute('''Insert Into STUDENT values('Mokshada','AIML','A',90)''')
cursor.execute('''Insert Into STUDENT values('Krish','Data Science','B',85)''')
cursor.execute('''Insert Into STUDENT values('Advika','AIML','A',86)''')
cursor.execute('''Insert Into STUDENT values('Ruchika','Data Science','A',56)''')
cursor.execute('''Insert Into STUDENT values('Harsh','AIML','A',35)''')

## Display all the records
print("The inserted records are")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

##Close the connection

connection.commit()
connection.close()