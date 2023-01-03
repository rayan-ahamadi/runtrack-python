from collections import Counter

#Fonction qui permet de trouver l'élément le plus fréquent d'une liste 
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def typeTriangle(a,b,c): 

    #Calcul pour prouver un rectangle équilatéral ou isocèle
    liste = [a,b,c]
    elementFrequent = most_frequent(liste)
    nbElementFrequent = liste.count(elementFrequent)

    #calcul pour prouver un triangle rectangle
    listeCarré=[a,b,c]
    valeurGrande = max(listeCarré)
    listeCarré.remove(valeurGrande)
    carréLong=valeurGrande*valeurGrande
    somme1= listeCarré[0] * listeCarré[0]
    somme2=listeCarré[1] * listeCarré[1]
    sommeCoteCourt = somme1 + somme2


    if nbElementFrequent == 3:
        print("Ce triangle est équilatéral")
    elif nbElementFrequent == 2: 
        print("Ce triangle est isocèle")
    elif nbElementFrequent == 2 and sommeCoteCourt == carréLong : 
        print("C'est un triangle rectangle isocèle")  
    elif sommeCoteCourt == carréLong: 
        print("Ce triangle est rectangle")
    else:
        #n'est ni rectangle,équilatéral ou isocèle
        print("C'est un triangle quelconque")
     
    
    


def triangle(a,b,c): 
    liste = [a,b,c]
    valeurGrande = max(liste)
    liste.remove(valeurGrande)
    sommePlusPetits = sum(liste)
    
    if sommePlusPetits < valeurGrande: 
        print("c'est IMPOSSIBLE de créer un triangle")
        unTriangle = False
    else : 
        print("il est POSSIBLE de faire un triangle")
        typeTriangle(a,b,c)


triangle(4,5,5)