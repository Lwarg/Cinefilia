def listaSeguaci():
    #global Utente
    #global database
    Utente = "Simone"
    numeroAmici = 0
    fileUtenti = open('C:/Users/simac/Google Drive/appCinefilia/users.txt','r')
    for user in fileUtenti:
        if Utente != user.strip():
            fileUtenti2 = open('C:/Users/simac/Google Drive/appCinefilia/amicidi'+user.strip()+'.txt','r')
            for amici in fileUtenti2:
                if amici.strip() == Utente:
                    numeroAmici += 1
    print(numeroAmici)