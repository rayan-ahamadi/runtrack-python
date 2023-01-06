def hautEtBas(n):
    liste = []
    i=0 
    while(i <= n+5):
        if i == 0 or i == n+5:
            liste.append("+")
            i+=1
        else: 
            liste.append("-")
            i+=1
    return print("".join(liste))


def diagonale(n):
    liste = []
    i=0
    while(i <= n+1):
        if i < n+1:
            liste.append("#")
            i+=1
        else: 
            liste.append(" ")
            i+=1
    j=0
    hautEtBas(n)
    while(j <= n+1):
        print("|","".join(liste),"|")
        blankIndex = liste.index(" ")
        precedentIndex = blankIndex - 1
        val1= liste[blankIndex]
        val2= liste[precedentIndex]
        liste[precedentIndex] = val1
        liste[blankIndex] = val2
        j+=1
    hautEtBas(n)
  
diagonale(8)