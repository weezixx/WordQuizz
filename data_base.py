import sqlite3

connexion = sqlite3.connect("bdd.db")

curseur = connexion.cursor()

curseur.execute('''CREATE TABLE IF NOT EXISTS words(

    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    NL TEXT,
    FR TEXT,
    SUCCEED INTEGER,
    TRIALS INTEGER
    
)''')

donnees = [("tot4","otot",1,2),("tata","atat",3,4)]

curseur.executemany("INSERT INTO words (NL, FR, SUCCEED, TRIALS) VALUES (?, ?, ?, ?)", donnees)

connexion.commit()

curseur.execute("SELECT * FROM words")

results = curseur.fetchall()

for result in results:
    print(result)

connexion.close()

#Si ça bug il faut supprimer le fichier et relancer le script