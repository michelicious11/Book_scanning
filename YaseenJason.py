#Opens the file
f = open( "C:\\Users\\abdel\\IdeaProjects\\Book_scanning\\Text_files/a_example.txt","r")    # Open the File in my Directory ( Yaseen's)

#Globale Variabeles
nbr_books =6
nbr_librairies =2
nbr_days =7

# (collection de tuples => les tuples representent les livres)
every_book =2

#(liste de listes de listes avec les informations des librairies)

#the inputs of library0
library_0_information =["5 Books","signup process takes 2 days", "Ships 2 books per day"]

#the inputs of library1
library_0_information =["4 Books","signup process takes 3 days", "Ships 1 book per day"]

# input = fichier texte, output = liste de listes where every list is a line from the text file.
def Read_Document(file):
    linked_list_fichier = []
    if not f: print("File not found"); exit(0)
    for line in f.readlines():
        linked_list_fichier.append(list(map(int, line.split(" "))))
    f.close()
    return linked_list_fichier

# Initialiser les variables globales nbr_books, nbr_libraries, nbr_days avec premiere ligne du text (premiere liste de la liste)
#def Set_data_scanning() :

#return

# create des tuples pour chaque livre (input = line numero 2 du document, output = collection de tuples)
#def Create_books()  :

    #return
#def Extract_library_information():            # paires de liste apres (a partir de la 3e liste et +) : chaque paire de ligne = information pour une librairie
                                              # donc creer une variable pour chaque librairie qui contient ses 2 lignes (une liste de liste) ex. librairie6 = [[xxx][xxxx]]

#return

# Pour tester la method Partie5
l = Read_Document("Input.txt")
print(l)                                    # Pour tester la method Partie5
print(l[0])                                 # Pour tester la method Partie5
print(l[0][0])                              # Pour tester la method Partie5



