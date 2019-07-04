import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Ignore",
    database = "testdb"
)
# print(mydb)

mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM Students WHERE age = 20")

# sql = "UPDATE students SET age = 13 WHERE name = 'Bob'"

#execute first 5 values
# mycursor.execute("SELECT * FROM students LIMIT 5")
# myresult = mycursor.fetchall()

#Ordering Queries + Results
sql = "SELECT * FROM students ORDER BY age"
mycursor.execute(sql)
myresult = mycursor.fetchall()

for result in myresult:
    print(result)
# mycursor.execute(sql)
# mydb.commit()
# sql = "SELECT * FROM students ORDER BY name DESC"

#Deleting Tables/Entries
# sql = "DELETE FROM students WHERE age=13"
# sql = "DROP TABLE IF EXISTS students"


#Wildcard Name Query
# mycursor.execute("SELECT * FROM Students WHERE name LIKE 'Lil%'")
# myresult = mycursor.fetchall()
# for row in myresult:
#     print(row)


#Inserting students
# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# # student1 = ("Rachel", 22)
# students = [ ("Bob", 22),
#              ("Amanda", 21),
#              ("Ray", 21),
#              ("LilLillian", 20),
#              ("Michelle", 20),]
#
#
# # mycursor.execute(sqlFormula, student1)
# mycursor.executemany(sqlFormula, students)
#
# mydb.commit()
#makes changes


# for tb in mycursor:
#     print(tb)



