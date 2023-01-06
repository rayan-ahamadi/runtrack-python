def draw_rectangle(width,height):
    i = 0
    j = 0
    liste = []
    listeEspace = []
    while(j <= width):
        liste.append("-")
        listeEspace.append(" ")
        j+=1

    while(i <= height):
        if i == 0 or i == height: 
            print("|", "".join(liste) ,"|")
            i+=1
        else: 
            print("|","".join(listeEspace) , "|")
            i+=1
        
draw_rectangle(50,5)
draw_rectangle(10,8)

