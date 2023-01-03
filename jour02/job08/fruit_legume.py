def alimentSaison(type,saison):
    if type == "fruits" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "été":
        print("Poire, fraise, cassis")
    elif type == "légumes" and saison == "hiver":
        print("carotte, topinambour, endive")
    elif type == "légumes" and saison == "été":
        print("artichaut, aubergine,navet")
    else:
        print("erreur : mauvaise valeur")

alimentSaison("fruits","hiver")
alimentSaison("fruits","été")
alimentSaison("légumes","hiver")
alimentSaison("légumes","été")
alimentSaison("pomme","printemps")