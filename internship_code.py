import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="SAILEE99",
  database="mydatabase"
)

print(mydb)

mycursor = mydb.cursor()

##mycursor.execute("CREATE DATABASE mydatabase")

mycursor.execute("CREATE TABLE Movies (name VARCHAR(255), lead_actor VARCHAR(255), lead_actress VARCHAR(255), year_of_release INT, director VARCHAR(255))")

sql = "INSERT INTO Movies (name, lead_actor, lead_actress, year_of_release, director) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("Inception", "Leonardo DiCaprio", "Elliot Page", 2010, "Christopher Nolan"),
    ("Jumanji", "Robin Williams", "Kirsten Dunst", 1995, "Joe Johnston"),
   ("A Quiet Place", "John Krasinski", "Emily Blunt", 2018, "John Krasinski")
]
mycursor.executemany(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM Movies")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

mycursor.execute("SELECT name FROM Movies WHERE lead_actor='Robin Williams'")

myresult2 = mycursor.fetchall()

for x in myresult2:
  print(x)




