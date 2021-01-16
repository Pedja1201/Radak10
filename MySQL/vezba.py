import mysql.connector

#TODOO: Napravi konekciju!!!
db = mysql.connector.connect(
    host="ProbaPython",
    user="root",
    password="pedja10",
    database="Python",
    port=3306
)

print("Hey, I think I'm connected")

cur = db.cursor()
for i in range(100):
    cur.execute("INSERT INTO employees (ID, NAME) VALUES (%s, %s)", (i +10, f'Pedja{i}' ))

cur.execute("SELECT ID,NAME FROM employees")

rows = cur.fetchall()

for r in rows:
    print(f" ID = {r[0]} NAME = {r[1]}")


cur.close()

db.close()




