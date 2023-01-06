

def chiffrementCesar(message,rang):
    messageAscii = []
    i=0
    while i < len(message):
        messageAscii.append(ord(message[i]))
        i+=1 
    messageEncrypted = []
    j = 0 
    while j < len(messageAscii): 
        messageEncrypted.append(chr(messageAscii[j]+rang))
        j +=1
    
    return print(message,"-->","".join(messageEncrypted))

chiffrementCesar("LaPlateforme",3)