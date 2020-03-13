import xlrd
import os.path
import csv

#Initialisation des répertoires et des fichiers utiles au projet
repBonnesLignes = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\\Tp\\tpAlgo\\tpdefinitif\\tpAlgo\\bonnesLignes"
repMauvaisesLignes = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\Tp\\tpAlgo\\tpdefinitif\\tpAlgomauvaisesLignes"
fichierXls = "C:\\Users\\Antoine\\Documents\\CESI\\Cours\\Algo\\Tp\\tpAlgo\\tpdefinitif\\tpAlgo\\coty2.csv"
newRow = []
ligneInserer = []
cpt = 0
cleC = 0

my_list = []
# my_list.append('geeks')
# print(my_list)

#Test de l'existence du fichier et de sa validité
try:
 with open(fichierXls) as csvfile:
     lines = csvfile.readlines()
     pass
except IOError:
 print("Erreur! Le fichier n'a pas pu être ouvert")

for row in lines:
    newRow = row.split(';')
    # Colonne 1
    # Vérification de la colonne A, si vide on prend la valeur de la colonne B
    if newRow[0] == '' and newRow[1] != '':
        ligneInserer.append(newRow[1])
    else:
        ligneInserer.append(newRow[0])

    # Colonne 2
    ligneInserer.append(newRow[2] + ' ' + newRow[3] + 'ML')

    # Colonne 3
    ligneInserer.append(newRow[3])

    # Colonne 4
    ligneInserer.append(newRow[4])

    #Colonne 5
    # Verif EAN-13
    if len(newRow[7].strip()) != 13:
        for item in newRow[7].strip():
            cleC = cleC + int(item)
        cleC = cleC%10
        newRow[7] = newRow[7].strip() + str(10 - cleC)
        if(len(newRow[7]) == 13):
            ligneInserer.append(newRow[7])
        else:
            ligneInserer.append('')
    else:
        ligneInserer.append(newRow[7].strip())

    #Colonne 6
    ligneInserer.append(newRow[5])

    print(ligneInserer)
    ligneInserer = []
