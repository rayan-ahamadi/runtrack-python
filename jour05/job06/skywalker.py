def arrondirNote(n):
    print("Les notes sans arrondir:", n)
    i=0
    listeArrondi=[]
    while(i < len(n)) :
      if str(n[i]+2)[-1] == "0" or str(n[i]+2)[-1] == "5":
            listeArrondi.append(n[i] + 2)
            i+=1
      else:
        listeArrondi.append(n[i])
        i+=1      
    return listeArrondi

note= [10,23,88,90]

print("Liste de notes arrondies :", arrondirNote(note))