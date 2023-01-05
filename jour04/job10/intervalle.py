def intervalleList(value,min,max):
    if value >= min and value <= max: 
        return value
    else:
       return print("pas dans l'intervalle")
    

L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
i=0
list = []
while(i < len(L)):
    if intervalleList(L[i],25,90) == L[i]:
        list.append(L[i])
        print(list)
        i+=1
    else:
        i+=1    
    
print("Le produit de cette intervalle", sum(list))