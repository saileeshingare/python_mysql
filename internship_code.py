import mysql.connector

# Creating a connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SAILEE99",
  database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()

## Creating a database
##mycursor.execute("CREATE DATABASE mydatabase")

## Creating a table 
mycursor.execute("CREATE TABLE Movies (name VARCHAR(255), lead_actor VARCHAR(255), lead_actress VARCHAR(255), year_of_release INT, director VARCHAR(255))")

## Inserting records into a table 
sql = "INSERT INTO Movies (name, lead_actor, lead_actress, year_of_release, director) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("Inception", "Leonardo DiCaprio", "Elliot Page", 2010, "Christopher Nolan"),
    ("Jumanji", "Robin Williams", "Kirsten Dunst", 1995, "Joe Johnston"),
   ("A Quiet Place", "John Krasinski", "Emily Blunt", 2018, "John Krasinski")
]
mycursor.executemany(sql, val)
mydb.commit()

## Selecting all records from a table 
mycursor.execute("SELECT * FROM Movies")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

## Selecting records from a table using WHERE clause 
mycursor.execute("SELECT name FROM Movies WHERE lead_actor='Robin Williams'")
myresult2 = mycursor.fetchall()
for x in myresult2:
  print(x)




