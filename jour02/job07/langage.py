def dev(langage):
    match langage: 
        case "javascript": 
            print("tu es un développeur web")
        case "python": 
            print("tu es un développeur IA")
        case "java": 
            print("tu es un développeur logiciel")
        case "reactjs": 
            print("tu es un développeur mobile")
        case _:
            print("un jour,je serais le meilleur développeur")

dev("javascript")
dev("python")
dev("java")
dev("reactjs")
dev("aucun")
