# Book_scanning
Problem statement for the Online Qualication Round of Hash Code 2020

# Table des matieres

- [Book_scanning](#book-scanning)
  * [Table des matieres](#table-des-matieres)
  * [Introduction](#introduction)
  * [Description du probleme](#description-du-probleme)
    + [Books](#books)
    + [Time](#time)
    + [Scanning](#scanning)
  * [Langage de programmation](#langage-de-programmation)
  * [Demarrage](#demarrage)
  * [Contributions](#contributions)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Introduction
---
Books allow us to discover fantasy worlds and beer understand the world we live in.
They enable us to learn about everything from photography to compilers… and of
course a good book is a great way to relax!
Google Books is a project that embraces the value books bring to our daily lives. It
aspires to bring the world's books online and make them accessible to everyone. In the
last 15 years, Google Books has collected digital copies of 40 million books in more
than 400 languages , paly by scanning books from libraries and publishers all around
the world.

In this competition problem, we will explore the challenges of seing up a scanning
process for millions of books stored in libraries around the world and having them
scanned at a scanning facility.

**URL** : <https://storage.googleapis.com/coding-competitions.appspot.com/HC/2020/hashcode_2020_online_qualification_round.pdf>

## Description du probleme
---

### Books
There are B dierent books with IDs from 0 to B–1. Many libraries can have a copy of
the same book, but we only need to scan each book once. Each book is described by
one parameter: the score that is awarded when the book is scanned.
Libraries
There are L dierent libraries with IDs from 0 to L–1. Each library is described by the
following parameters:
● the set of books in the library,
● the time in days that it takes to sign the library up for scanning,
● the number of books that can be scanned each day from the library once the
library is signed up.

### Time
There are D days from day 0 to day D–1. The rst library signup can sta on day 0. D–1
is the last day during which books can be shipped to the scanning facility.

Library signup
Each library has to go through a signup process before books from that library can be
shipped. Only one library at a time can be going through this process (because it
involves lots of planning and on-site visits at the library by logistics expes): the signup
process for a library can sta only when no other signup processes are running. The
libraries can be signed up in any order.
Books in a library can be scanned as soon as the signup process for that library
completes (that is, on the rst day immediately aer the signup process, see the gure
below). Books can be scanned in parallel from multiple libraries.

For example, if:
● the signup process for library 0 (that is, the library with ID 0) takes 2 days, and
● the signup process for library 1 takes 3 days, and
● library 1 is signed up before library 0
then
● the signup process of library 1 starts on day 0, and finishes on day 2 (3 days in
total)
● the first books from library 1 can be scanned staing on day 3 (the next day
after the signup process finishes)
● the signup of library 0 starts on day 3 (the next day aer the signup process
of library 0 is done) and nishes on day 4 (2 days in total)
● the first books from library 0 can be scanned starting on day 5 (the next day
after the signup process finishes)

### Scanning
All books are scanned in the scanning facility. The entire process of sending the books,
scanning them, and returning them to the library happens in one day (note that each
library has a maximum number of books that can be scanned from this library per day).
The scanning facility is big and can scan any number of books per day.
For example, if library 0 has 5 books, can ship 2 books per day, and completes the
signup process on day 1, then:
● 2 books can be scanned on day 2
● 2 books can be scanned on day 3
● the one remaining book can be scanned on day 4


## Langage de programmation 
---
Python 3.8


## Demarrage
---

1. Telecharger Python 3.8
2. Creer sa propre branche dans github 


## Contributions
---

Livres
  -	Tableau/liste de (0 --> n – 1) livres avec des ID différents ( 
  -	Les livres devrait être scanné uniquement une fois (même si il apparaissent dans plusieurs librairies) 
      o	Chaque livre est décrit par 1 paramètre (valeur qu’elle reçoit lorsque scanné)

Proposition : 
(variable globale) set B; 
(variable globale) int idLivre;
Class livre () {
    int id = this.idLivre
}

Librairies
  -	Tableau/liste de (0 --> n – 1) librairies avec des ID différents 
      o	Défini par l’ensemble de livres contenu dans la librairie (liste/tableau de livres)
      o	Défini par le temps en jours que sa prend pour l’inscription de la librairie
      o	Défini par le nombre de livres qui peuvent être scanné par jour lorsque la librairie inscrit (max)
Proposition : 
(variable globale) int idLibrairie;
