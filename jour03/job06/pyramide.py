def pyramide():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i=0
    longueur = 1
    while(i < len(alphabet)):
        if i == 0:
            print(alphabet[i])
            i = i + 1 
        elif i > 0:
            print(alphabet[i:i+longueur+1])
            longueur = longueur + 1 
            i = i+longueur
        



pyramide()


