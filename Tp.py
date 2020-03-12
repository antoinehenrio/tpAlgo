import xlrd
from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl import styles
import csv

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

for row in c:
    print(row)

# ouverture du fichier Excel
# wb = xlrd.open_workbook(fichierXls)
# compteurLignes = 1
# compteurColonnes = 1
# #Récupération de la première feuille du classeur
# feuilles = wb.sheet_names()
# feuille = wb.sheet_by_name(feuilles[0])

#Parcours des lignes de la feuille
