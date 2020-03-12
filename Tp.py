import xlrd
import os.path
import csv

#Initialisation des répertoires et des fichiers utiles au projet
repBonnesLignes = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\\Tp\\tpAlgo\\tpdefinitif\\tpAlgo\\bonnesLignes"
repMauvaisesLignes = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\Tp\\tpAlgo\\tpdefinitif\\tpAlgomauvaisesLignes"
fichierXls = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\\Tp\\tpAlgo\\tpdefinitif\\tpAlgo\\coty2.csv"
newRow = []
#Test de l'existence du fichier et de sa validité
try:
 with open(fichierXls) as csvfile:
     lines = csvfile.readlines()
     pass
except IOError:
 print("Erreur! Le fichier n'a pas pu être ouvert")

for row in lines:
    newRow = row.split(';')
    # Vérification de la colonne A, si vide on prend la valeur de la colonne B
    if newRow[0] == '' and newRow[1] != '':
        newRow[0] = newRow[1]
        # newRow[0] = str(newRow[1])
        print(newRow)
    else:
        print(newRow)

    # print(newRow[0])

# for line in newRow.count()
#     print(newRow[0])
# ouverture du fichier Excel
# wb = xlrd.open_workbook(fichierXls)

#Récupération de la première feuille du classeur
# feuilles = wb.sheet_names()
# feuille = wb.sheet_by_name(feuilles[0])

#Création du csv bonnes lignes
# if os.path.isfile('bonnesLignes.csv'):
#     print ("File exist")
# else:
#     f = open('bonnesLignes.csv', 'w')
#     f.close()

#Parcours des lignes de la feuille
# for rownum in range(feuille.nrows):
#     newRow = rownum.split(';')

#test
