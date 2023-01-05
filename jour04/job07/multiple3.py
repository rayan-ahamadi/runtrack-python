def multiple3(i): 
    iChar = str(i)
    array = []
    for caracter in iChar:
        array.append(int(caracter))
    result = sum(array)
    return(result)

def Ismultiple3(value):
    calcul = multiple3(value)
    if calcul == 3 or calcul == 6 or calcul == 9:
        return True
    elif len(str(calcul)) > 1 and multiple3(calcul) :
        return True
    else: 
        return False
        
        

    
l = [8,24,48,2,16]
i=0
countMultiple3=0
while(i < len(l)):
    if Ismultiple3(l[i]) == True:
        print(l[i])
        countMultiple3 = countMultiple3 + 1 
    i= i + 1

print("il y a ",countMultiple3," nombre multiple de 3 dans cette liste")



