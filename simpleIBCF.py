import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error

df = pd.read_csv("provaDatasetRaccomandazione.csv", sep=",")
df.dropna(inplace=True)

# Creazione matrice USER-ITEM
matriceUI = df.pivot_table(index=['User'], columns=['Item'], values='Rating').fillna(0)
# converto la pivot table in matrice sparsa
matriceUI = sparse.lil_matrix(matriceUI)

# Creazione matrice ITEM-ITEM similarity
m_m_similarity = cosine_similarity(matriceUI.T, dense_output = False)

d = {'ID':list(range(1,26)), 'Title':list(range(1,26))}
item_title_df = pd.DataFrame(d, columns=['ID','Title'])

# specifico l'user per cui voglio fare la raccomandazione\n",
userID = 5

# inizializzo alcune variabili che mi servono
userID -= 1
user_rating_list = []
not_rated = []
for i in range(25):
    user_rating_list.append(matriceUI[userID, i])
    if matriceUI[userID, i] == 0.0:
        not_rated.append(i)

# faccio la predizione dei ratings  
suggested = []
rating_pred = []
for col in range(25):
    if matriceUI[userID, col] == 0:
        # aggiungo l'item alla lista suggeriti
        suggested.append(item_title_df['ID'].iloc[col])
        
        # predico che voto l'user darebbe all'item
        item_similarity_list = []
        denominatore = 0
        for i in range(25):
            item_similarity_list.append(m_m_similarity[col, i])
            if i not in not_rated:
                denominatore += m_m_similarity[col, i]
        numeratore = np.dot(np.array(item_similarity_list), np.array(user_rating_list))
        if denominatore != 0:
            rating_pred.append(int(numeratore/denominatore))
        else:
            rating_pred.append('NaN')


print('Items suggested to user',userID+1,':',suggested)
print('Predicted ratings given by user',userID+1,':',rating_pred)
