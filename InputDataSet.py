import Book
import Library

def readInput(file):
    B = {}
    L = {}
    bookID = 0
    f = open(file, "r")
    if not f: print("File not found"); exit(0)
    input = list(map(int, f.readline().split()))
    numberOfBooks = input[0]
    numberOfLibraries = input[1]
    numberOfDays = input[2]
    input = list(map(int, f.readline().split()))
    for i in range (0, numberOfBooks):
        B[i] = input[i]
    for j in range (0, numberOfLibraries):
        input = list(map(int, f.readline().split()))    #first line
        numberOfBooks = input[0]
        L[j] = Library.Library(j)
        L[j].time = input[1]
        L[j].maxToScan = input[2]
        input = list(map(int, f.readline().split()))    #second line
        for k in range(0, numberOfBooks):
            L[j].books[k] = B[input[k]]
    f.close()

readInput("Text_files/a_example.txt")
print("22")
