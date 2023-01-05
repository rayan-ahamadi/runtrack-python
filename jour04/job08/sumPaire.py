def valeurPaire(value):
    if str(value)[-1] == "0" or str(value)[-1] == "2" or str(value)[-1] == "4" or str(value)[-1] == "6" or str(value)[-1] == "8":
        return value
    else: 
        return print(value," n'est pas paire")

L = [8,24,27,48,2,16,9,7,84,91]
Lpaire = []
i = 0
while(i<len(L)):
    if valeurPaire(L[i]) == L[i] :
        Lpaire.append(L[i])
        i+=1
    else: 
        i+=1
    
print(Lpaire)    
print("La somme des nombres paires de cette liste :", sum(Lpaire))
