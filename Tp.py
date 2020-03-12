import xlrd

#Initialisation des répertoires et des fichiers utiles au projet
repBonnesLignes = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\bonnesLignes"
repMauvaisesLignes = "D:\Desktop\Cours\CESI\Algorithmie\mauvaisesLignes"
fichierXls = "D:\\Desktop\\Cours\\CESI\\Algorithmie\\coty.xls"

#Test de l'existence du fichier et de sa validité
try:
 with open(fichierXls): pass
except IOError:
 print("Erreur! Le fichier n'a pas pu être ouvert")

# ouverture du fichier Excel
wb = xlrd.open_workbook(fichierXls)

#Récupération de la première feuille du classeur
feuilles = wb.sheet_names()
feuille = wb.sheet_by_name(feuilles[0])

#Parcours des lignes de la feuille
for rownum in range(feuille.nrows):
    print(feuille.row_values(rownum))
