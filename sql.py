import sqlite3

## Connect to sqlite
connection=sqlite3.connect("student.db")

## Create a cursor object to insert record,create table,retrieve
cursor=connection.cursor()

## Create the table
# Dropping table first so you can run this script multiple times without errors
cursor.execute("DROP TABLE IF EXISTS STUDENT")

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

## Insert records (Expanded to 30 rows)
students_data = [
    ('Mokshada', 'AIML', 'A', 90),
    ('Krish', 'Data Science', 'B', 85),
    ('Advika', 'AIML', 'A', 86),
    ('Ruchika', 'Data Science', 'A', 56),
    ('Harsh', 'AIML', 'A', 35),
    ('Aarav', 'Data Science', 'B', 78),
    ('Ananya', 'AIML', 'B', 92),
    ('Ishaan', 'ECE', 'A', 88),
    ('Saanvi', 'ECE', 'B', 74),
    ('Vivaan', 'Data Science', 'A', 65),
    ('Diya', 'AIML', 'C', 81),
    ('Arjun', 'CS', 'A', 89),
    ('Myra', 'CS', 'B', 94),
    ('Kabir', 'ECE', 'A', 45),
    ('Kiara', 'Data Science', 'C', 72),
    ('Rohan', 'CS', 'C', 60),
    ('Zoya', 'AIML', 'B', 87),
    ('Reyansh', 'ECE', 'B', 38),
    ('Sara', 'CS', 'A', 91),
    ('Aryan', 'Data Science', 'B', 55),
    ('Navya', 'AIML', 'A', 77),
    ('Dev', 'ECE', 'C', 69),
    ('Isha', 'CS', 'B', 83),
    ('Shaurya', 'Data Science', 'A', 95),
    ('Tanvi', 'AIML', 'C', 42),
    ('Karthik', 'ECE', 'A', 76),
    ('Pari', 'CS', 'C', 80),
    ('Aditya', 'Data Science', 'B', 68),
    ('Sia', 'AIML', 'A', 84),
    ('Vihaan', 'ECE', 'B', 59)
]

for student in students_data:
    cursor.execute('''Insert Into STUDENT values(?,?,?,?)''', student)

## Display all the records
print("The inserted records are:")

data=cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()

print("\nDatabase created and populated successfully with 30 records.")