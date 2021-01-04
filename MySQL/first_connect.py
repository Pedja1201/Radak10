import mysql.connector
#dobavljanje konekcije
connection = mysql.connector.connect(user='root', password='pedja10', host='localhost', port='3306', database='MyDataBase')

csor = connection.cursor()

insert_statement = "INSERT INTO zaposleni (ime, prezime) VALUES (%s, %s)"
insert_data = ('Pedja', 'Radak')
insert_several = [('Pedja', 'Radak'), ('Nikola', 'Nikolic'), ('Pavle', 'Palic')]

csor.execute(insert_statement, insert_data)
#csor.executemany(insert_statement, insert_several)

query = "SELECT ime, prezime FROM zaposleni WHERE zaposleni.satnica*zaposleni.radni_sati BETWEEN %s AND %s;"
min_plata = 500
max_plata = 2000

csor.execute(query, (min_plata, max_plata))


#for(ime, prezime) in csor:
    #print(f"{ime}, {prezime}")
#ILI
#for result in csor.fetchall():
    #print(result)
#ILI
row = csor.fetchone()
while row is not None:
    print(row)
    row = csor.fetchone()

#primer sa procedurom
csor.callproc("ZaposleniPoImenu", ["Nikola"])
for res in csor.stored_results():
    print(res.fetchall())


connection.commit()
#zatvaramo kursor, da ga raskačimo od konekcije
csor.close()
#zatvaramo konekciju - trebalo bi da se smesti u try/finally
connection.close()