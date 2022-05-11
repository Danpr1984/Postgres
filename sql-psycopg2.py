import psycopg2

connection = psycopg2.connect(database="chinook")

cursor = connection.cursor()

#cursor.execute('SELECT * FROM "Artist"')

cursor.execute('SELECT * FROM "Artist"')

#cursor.execute('SELECT * FROM "N" WHERE "Name" = %s', ["Kiss"])

#cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [55])

results = cursor.fetchall()

#results = cursor.fetchone()

connection.close()

for result in results:
    print(result)