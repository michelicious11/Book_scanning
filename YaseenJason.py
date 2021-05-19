
f = open( "C:\\Users\\abdel\\IdeaProjects\\Book_scanning\\Text_files/a_example.txt","r")    # Open the File in my Directory ( Yaseen's)

nbr_books =5
nbr_librairies =3
nbr_days =2
every_book =2                                                        # (collection de tuples => les tuples representent les livres)
library_information =0                                                 #(liste de listes de listes avec les informations des librairies)

def Read_Document(file):                # input = fichier texte, output = liste de listes where every list is a line from the text file.
    linked_list_fichier = []

    if not f: print("File not found"); exit(0)
    for line in f.readlines():
        linked_list_fichier.append(list(map(int, line.split(" "))))
    f.close()
    return linked_list_fichier

def Set_data_scanning()                         # Initialiser les variables globales nbr_books, nbr_libraries, nbr_days avec premiere ligne du text (premiere liste de la liste)

return

def Create_books()                              # create des tuples pour chaque livre (input = line numero 2 du document, output = collection de tuples)

    return

def Extract_library_information()               # paires de liste apres (a partir de la 3e liste et +) : chaque paire de ligne = information pour une librairie
                                                # donc creer une variable pour chaque librairie qui contient ses 2 lignes (une liste de liste) ex. librairie6 = [[xxx][xxxx]]

return

l = Read_Document("Input.txt")                    # Pour tester la method Partie5
print(l)                                    # Pour tester la method Partie5
print(l[0])                                 # Pour tester la method Partie5
print(l[0][0])                              # Pour tester la method Partie5



