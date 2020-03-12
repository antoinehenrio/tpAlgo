import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl import styles
import csv

def estUnique(valeur, numColonne, reader, index):
    flag = False
    i = 0
    j = 0
    counter = 0
    chaineTemp = ""
    compteurLignes = 1
    for row in reader:
        ligne = row[0].split(";")
        if len(ligne) < 8:
            for j in range(1,9 - len(ligne)):
                ligne.append(" ")
        if len(ligne) > 8:
            del(ligne[len(ligne) - 1])
        if ligne[numColonne - 1] == valeur and compteurLignes != index:
            print("Ligne : {} Valeur : {} Num Colonne : {}".format(ligne[numColonne -1],valeur,numColonne))
            flag = True
        compteurLignes = compteurLignes + 1
        print(ligne)
    if flag == True:
        return True
    else:
        return False

#Initialisation des répertoires et des fichiers utiles au projet
repBonnesLignes = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\bonnesLignes"
repMauvaisesLignes = "D:\Desktop\Cours\CESI\Algorithmie\mauvaisesLignes"
fichierBonnesLignes = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\bonnesLignes\\bonnesLignes.csv"
fichierMauvaisesLignes = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\mauvaisesLignes\\mauvaisesLignes.csv"
fichierXls = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\coty.csv"

#Test de l'existence du fichier et de sa validité
c = csv.reader(open(fichierXls, "r"))

#Création du fichier contenant les lignes valides
try:
    with open(fichierBonnesLignes,"w"): pass
except IOError:
    print("Erreur dans l'ouverture du fichier")

#Création du fichier contenant les lignes erronnées
try:
 with open(fichierMauvaisesLignes,"w"): pass
except IOError:
 print("Erreur dans l'ouverture du fichier csv")

if estUnique("82464565",1,c,21) == True:
    print("Cela existe")
else:
    print("Cela n'existe pas")
# for row in c:
#     print(row)
