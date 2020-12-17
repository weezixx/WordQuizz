import sqlite3
import time
start_time = time.time()


connexion = sqlite3.connect("bdd.db")

curseur = connexion.cursor()

curseur.execute('''CREATE TABLE IF NOT EXISTS words(

    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    NL TEXT,
    FR TEXT,
    SUCCEED INTEGER,
    TRIALS INTEGER
    
)''')

nl = open("neerlandais.txt","r")
en = open("anglais.txt","r")


donnee = []

for i,j in zip(nl,en):
    donnee.append(i)

    curseur.execute("INSERT INTO words (NL, FR, SUCCEED, TRIALS) VALUES (?, ?, 0, 0)", (i,j,))

    connexion.commit()

    curseur.execute("SELECT * FROM words")

# results = curseur.fetchall()
#
# for result in results:
#     print(result)

connexion.close()

print("--- %s seconds ---" % (time.time() - start_time))

#Si ça bug il faut supprimer le fichier et relancer le script