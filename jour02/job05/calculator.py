def calcule(num1,operator,num2):
    if operator == "+":
        return(print(num1 + num2))
    elif operator == "-":
        return(print(num1 - num2))
    elif operator == "*":
        return(print(num1 * num2))
    elif operator == "/":
        return(print(num1 / num2))
    elif operator == "%":
        return(print(num1 % num2))
    else: 
        return(print("erreur : mauvais opérateur"))

calcule(5,"+",5)
calcule(5,"-",5)
calcule(5,"*",5)
calcule(5,"/",5)
calcule(5,"%",5)
calcule(5,"?",5)