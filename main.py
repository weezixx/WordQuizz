import random

import sqlite3

def enregistrement(voc):
    fichier = open("data.txt", "w")

    for i in voc:
        fichier.write(' '.join(i))

    fichier.close()


def quizz():
    # list to avoid redundancy in Quizz (2 times the same word)
    mdf = []

    fichier = open("data.txt", "r")

    voc = [i.split(" ") for i in fichier]

    print(voc)

    for i in range(10):

        nbr = random.randint(0, 9)

        mot = voc[nbr][1]

        #score = int(voc[nbr][2])
        score = int(voc[nbr][-2])

        #tentatives = int(voc[nbr][3])
        tentatives = int(voc[nbr][-1])

        if mot not in mdf:

            print("score avant :", score)

            mdf.append(mot)

            print(mot)

            if input() == voc[nbr][0]:
                print("well done !!! ")

                score += 5

                tentatives += 1

                voc[nbr][2] = str(score)

                voc[nbr][3] = str(tentatives) + "\n"

                print("score après : ", score)

                enregistrement(voc)

                fichier.close()


# def add():

#  fichier = open("data.txt","w")

while True:

    q = input("Alors on fait quoi ? ")

    if q == "add":

        fichier = open("data.txt", "a")

        fr_nl = input("va y donne \n")

        # ajouts score + tentative
        fr_nl += " 0 0 \n"

        fichier.write(fr_nl)

    elif q == "quizz":
        quizz()