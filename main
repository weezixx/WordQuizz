import random

class mot:

  liste = []

  def __init__(self,nl,fr):
    self.nl = nl
    self.fr = fr
    self.score = 0 

    mot.liste.append(self)

def enregistrement():

  fichier = open("data.txt","w")

  for i in voc:
    fichier.write(' '.join(i))

  fichier.close()

mdf = []
  
fichier = open("data.txt","r")

voc = [i.split(" ") for i in fichier]



for i in range(3):
  
  nbr = random.randint(0,2)

  mot = voc[nbr][1]
  
  score = int(voc[nbr][2])

  tentatives = int(voc[nbr][3])

  if mot not in mdf:

    print("score avant :",score)
    
    mdf.append(mot)

    print(mot)

    if input() == voc[nbr][0]:
      
      print("well done !!! ")   
      
      score += 5

      tentatives += 1

      voc[nbr][2] = str(score) + "\n"

      voc[nbr][3] = str(tentatives) + "\n"
      
      print("score après : ",score)


print(mdf)




fichier.close()


enregistrement()

