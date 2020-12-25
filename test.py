import sqlite3

connexion = sqlite3.connect("bdd.db")

curseur = connexion.cursor()

#SELECT * FROM words ORDER BY RANDOM() LIMIT 1

curseur.execute("SELECT * FROM words WHERE trials = 0 ORDER BY RANDOM()  LIMIT 1")
#curseur.execute("UPDATE words SET trials = 0 WHERE id = 5425 ")

# rows = curseur.execute("SELECT * FROM words ")
#
rows = curseur.fetchall()

for row in rows:

     ligne = row[0]

     reponse = input('quelle est la traduction de : '+ row[2])

     reponse = reponse + "\n"

     if reponse == row[1]:
          print("gooooooooooood")

     else:
          print("raté la réponse était : " + row[1])

#      curseur.execute("UPDATE words SET trials = 1 WHERE id = ? ",(ligne,))
#
# curseur.execute("SELECT * FROM words WHERE id = ?", (ligne,))
#
# rows = curseur.fetchall()
#
# print(rows)