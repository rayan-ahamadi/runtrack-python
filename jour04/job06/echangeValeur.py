def echange(list): 
    first = list[0]
    last = list [-1]
    list[0] = last
    list[-1] = first
    return list




liste = [1,5,9]
print(echange(liste))