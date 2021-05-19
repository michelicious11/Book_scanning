import Book
import Library


def librarySignup(B, L, numberOfDays):
    time = {}

    index = 0
    score = {}
    while len(time) <= numberOfDays:
        for i in range(0, index):
            booksToShip = L[i].maxToScan - len(L[i].books)
            if booksToShip > 0:
                for j in range(0, L[i].maxToScan-1):
                    if L[j] not in score:
                        score[j] = L[i].books[j]
                        L.pop(L[i].books[j])
                else:
                    break
                    #score[j] = L[i]
            #if L[index].time - len(time) <= 0:1

        L[index].time = L[index].time - 1
        time[len(time)] = index
        if L[index].time <= 0 and index < len(L) - 1:
            index += 1

    #print(time)
    #print(score)





#6 2 7          There are 6 books, 2 libraries, and 7 days for scanning.
#1 2 3 6 5 4    The scores of the books are 1, 2, 3, 6, 5, 4 (in order).
#5 2 2          Library 0 has 5 books, the signup process takes 2 days, and the library can ship 2 books per day.
#0 1 2 3 4      The books in library 0 are: book 0, book 1, book 2, book 3, and book 4.
#4 3 1          Library 1 has 4 books, the signup process takes 3 days, and the library can ship 1 book per day.
#3 2 5 0        The books in library 1 are: book 3, book 2, book 5 and book 0.
#for i in range (0, len(L[0].time)):
#        time[i] = None




