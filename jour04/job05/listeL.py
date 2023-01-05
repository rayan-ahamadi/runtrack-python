def replaceL3(list):
    sum = list[2] + list[4]
    list[3] = sum

def listL():
    L = [1,2,3,4,5]
    print(L[1])
    replaceL3(L)
    print(L[-1])
    return print(L)

listL()