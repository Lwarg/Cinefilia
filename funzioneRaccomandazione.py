import pandas as pd
import numpy as np

from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

utente = 'insert user'
database = 'insert path'


# creazione automatica del dataset
file_utenti = open(database + "/users.txt", 'r')
dataset = []
for dati_utente in file_utenti:
    id_utente = dati_utente.split(",")[0]
    nome_utente = dati_utente.strip().split(",")[1]
    if nome_utente == utente:
        id_utente_loggato = id_utente
    file_film = open(database + "/elencoFilmdi" + nome_utente + ".txt", 'r')
    for dati_film in file_film:
        id_film = dati_film.split(",")[0]
        voto_film = dati_film.strip().split(",")[1]
        nuova_istanza = [id_utente, id_film, int(voto_film)]
        dataset.append(nuova_istanza)
    file_film.close()
file_utenti.close()

df = pd.DataFrame(dataset, columns=['User', 'Item', 'Rating'])
df.dropna(inplace=True)

# Creazione matrice USER-ITEM
matriceUI = df.pivot_table(index=['User'], columns=['Item'], values='Rating').fillna(0)
# converto la pivot table in matrice sparsa
matriceUI = sparse.lil_matrix(matriceUI)

# Creazione matrice ITEM-ITEM similarity
m_m_similarity = cosine_similarity(matriceUI.T, dense_output = False)

d = {'ID':list(df['Item']), 'Title':list(df['Item'])}
item_title_df = pd.DataFrame(d, columns=['ID','Title'])

# inizializzo alcune variabili che mi servono
userID = int(id_utente_loggato) - 1001
user_rating_list = []
not_rated = []
for i in range(25):
    user_rating_list.append(matriceUI[userID, i])
    if matriceUI[userID, i] == 0.0:
        not_rated.append(i)

# faccio la predizione dei ratings  
suggested = []
rating_pred = []
numero_totale_film = m_m_similarity.shape[0]
for col in range(numero_totale_film):
    if matriceUI[userID, col] == 0:
        # aggiungo l'item alla lista suggeriti
        suggested.append(item_title_df['ID'].iloc[col])
        
        # predico che voto l'user darebbe all'item
        item_similarity_list = []
        denominatore = 0
        for i in range(numero_totale_film):
            item_similarity_list.append(m_m_similarity[col, i])
            if i not in not_rated:
                denominatore += m_m_similarity[col, i]
        numeratore = np.dot(np.array(item_similarity_list), np.array(user_rating_list))
        if denominatore != 0:
            rating_pred.append(int(numeratore/denominatore))
        else:
            rating_pred.append('NaN')


print('Items suggested to',utente,':',suggested)
print('Predicted ratings given by user',userID+1,':',rating_pred)
