def nbMetreParcouru(nbMarche,hauteurMarche):
    unAller = hauteurMarche * nbMarche
    unJour = unAller * 5 
    dansLaSemaine = unJour * 5
    return print("Pour",nbMarche,"marches de",hauteurMarche,"cm,Le gardien parcours ",dansLaSemaine / 100,"m par semaine. ")


nbMetreParcouru(80,70)

