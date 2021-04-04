# Importing Libraries 
import numpy as np 
import pandas as pd

# Import dataset 
dataset = pd.read_csv('C:/Users/simac/Google Drive/appCinefilia/train_frasiVolgari.txt', delimiter = '|')

#Stampo il numero delle righe del dataset
numrows=dataset.shape[0]

# NLP
#Puliamo il dataset con lo stemmer Snowball e con le stop words in italiano

# library to clean data 
import re 
# Natural Language Tool Kit 
import nltk 
nltk.download('stopwords') 
# to remove stopword 
from nltk.corpus import stopwords 
# for Stemming in Italiano con Snowball
from nltk.stem import SnowballStemmer 
stemmer_ita = SnowballStemmer('italian')
# Initialize empty array 
# to append clean text 
corpus = [] 
# 66(reviews) rows to clean 
for i in range(0, numrows): 
	# column : "Review", row ith 
	review = re.sub('[^a-zA-Z]', ' ', dataset['Frasi'][i])
	# convert all cases to lower cases 
	review = review.lower() 
	# split to array(default delimiter is " ") 
	review = review.split() 
	# loop for stemming each word 
	# in string array at ith row	 
	review = [stemmer_ita.stem(word) for word in review 
				if not word in set(stopwords.words('italian'))] 
	# rejoin all string array elements 
	# to create back into a string 
	review = ' '.join(review) 
	# append each string to create 
	# array of clean text 
	corpus.append(review)

# Utilizziamo il modello Bag of Words
from sklearn.feature_extraction.text import CountVectorizer 
# To extract max 1500 feature. 
# "max_features" is attribute to 
# experiment with to get better results 
cv = CountVectorizer(max_features = 1500) 
# X contains corpus (dependent variable) 
X = cv.fit_transform(corpus).toarray() 
# y contains answers if review 
# is positive or negative 
y = dataset.iloc[:, 1].values

# Calcolo il modello:
# Fitting Random Forest Classification 
# to the Training set 
from sklearn.ensemble import RandomForestClassifier 
# n_estimators can be said as number of 
# trees, experiment with n_estimators 
# to get better results 
model = RandomForestClassifier(n_estimators = 501, 
							criterion = 'entropy') 			
model.fit(X,y)

# Salvo il file del modello
import pickle
modelloFrasiVolgari = open ("C:/Users/simac/Google Drive/appCinefilia/modelloFrasiVolgari.pickle","wb")
pickle.dump(model,modelloFrasiVolgari)
modelloFrasiVolgari.close()