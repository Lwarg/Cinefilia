# Cinefilia
Un'app per gestire la tua cinefilia

----------
API di riferimento: http://www.omdbapi.com/

CONTENUTO REPOSITORY:
- InserireNuoviFilm.py : codice che prende in input il titolo di un film e lo aggiunge in un database
- elencoFilm.txt : file sostitutivo al database fintanto che non ne viene realizzato uno più adatto 
- VisualizzaListaFilm.py : codice che stampa elencoFilm.txt dall'ultimo al primo
- VisualizzaInfoMieiFilm.py : codice per selezionare un film da elencoFilm.txt e restituire la scheda tecnica
- CercaInfoNuovoFilm.py : codice per selezionare un film da elencoFilm.txt e restituire la scheda tecnica
- creazioneDatabase.py : codice per connettersi al database e per creare le tabelle Utente e Film (da utilizzare solo una volta)
- registrazioneUtente.py: codice che permette all'utente di registrarsi nel database inserendo username e password
- statistiche.py: codice che genera le statistiche a partire da un elenco di film
- GUI*.py : codice generazione gui per singole funzioni (andranno unite in un'unica GUI)
