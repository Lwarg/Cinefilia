import pickle

commento = "L'ultimo film della trilogia è davvero una merda"

#NLP al commento (con lo stemmer Snowball e con le stop words in italiano)
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
# column : "Review", row ith 
review_2 = re.sub('[^a-zA-Z]', ' ', commento)
# convert all cases to lower cases 
review_2 = review_2.lower() 
# split to array(default delimiter is " ") 
review_2 = review_2.split() 
# loop for stemming each word 
# in string array at ith row	 
review_2 = [stemmer_ita.stem(word) for word in review_2
            if not word in set(stopwords.words('italian'))] 
# rejoin all string array elements 
# to create back into a string 
review_2 = ' '.join(review_2) 

test = review_2
modelloFrasiVolgari = pickle.load(open("C:/Users/simac/Google Drive/appCinefilia/modelloFrasiVolgari.pickle","rb"))
# importo lista feature
features = open ("C:/Users/simac/Google Drive/appCinefilia/featureModelloFrasiVolgari.txt","r")
x_test = []
for i in features:
    if i.strip() in test:
        x_test.append(1)
    else:
        x_test.append(0)
X_test = [x_test]

# Predicting the Test set results 
y_pred = modelloFrasiVolgari.predict(X_test)
print(y_pred)


