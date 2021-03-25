def listaSeguaci():
    global Utente
    global database
    numeroAmici = 0
    fileUtenti = open(''+database+'/users.txt','r')
    for user in fileUtenti:
        if Utente != user.strip():
            fileUtenti2 = open(''+database+'/amicidi'+user.strip()+'.txt','r')
            for amici in fileUtenti2:
                if amici.strip() == Utente:
                    numeroAmici += 1
    print(numeroAmici)