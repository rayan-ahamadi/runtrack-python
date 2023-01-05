# Fonction qui permet de prouver un multiple de 3 en trouvant le résultat de la somme des nombres de la variable i
# la fonction retourne au final un integer 
def multiple3(i): 
    iChar = str(i)
    array = []
    for caracter in iChar:
        array.append(int(caracter))
    result = sum(array)
    return(result)


def fizbuzz():
    i = 0
    while(i <= 100):
        if i == 15: 
            print("fizzbuzz")
            i = i + 1 
        elif multiple3(i) == 3 or multiple3(i) == 6 or multiple3(i) == 9: 
            print("Fizz")
            i= i + 1
        elif str(i)[-1] == "5" or str(i)[-1] == "0":
            print("buzz")
            i = i + 1
        else: 
            print(i)
            i = i + 1 

fizbuzz()