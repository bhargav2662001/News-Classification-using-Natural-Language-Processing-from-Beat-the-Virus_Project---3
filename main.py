import numpy as np
import matplotlib.pyplot as plt
import sea as sns
sns.set()

from sklearn.datasets import fetch_20newsgroups # here we are fetching data from sklearn.datasets

data=fetch_20newsgroups()
data.target_names

# Defining all the categories

categories=['alt.atheism',
 'comp.graphics',
 'comp.os.ms-windows.misc',
 'comp.sys.ibm.pc.hardware',
 'comp.sys.mac.hardware',
 'comp.windows.x',
 'misc.forsale',
 'rec.autos',
 'rec.motorcycles',
 'rec.sport.baseball',
 'rec.sport.hockey',
 'sci.crypt',
 'sci.electronics',
 'sci.med',
 'sci.space',
 'soc.religion.christian',
 'talk.politics.guns',
 'talk.politics.mideast',
 'talk.politics.misc',
 'talk.religion.misc']
# training the data on these categories
train = fetch_20newsgroups(subset='train', categories=categories)

# testing the data for these categories
test=fetch_20newsgroups(subset='test', categories=categories)

# print a data
print(train.data[5])
print(train.target[5])

# import necessary packages

from sklearn.feature_extraction.text import TfidfVectorizer # To convert normal tetx to TfIdfVector( which signify importance of a particular word) 

from sklearn.naive_bayes import MultinomialNB  # import Naive Bayes Classifier

from sklearn.pipeline import make_pipeline # we are using pipeline because its a huge data and we will provide data in batches

#created a model based on Multinomial NB along with pipeline
model=make_pipeline(TfidfVectorizer(),MultinomialNB()) 

# training the model with the train data
model.fit(train.data,train.target)

# predictions on test data
labels=model.predict(test.data)

# creating confusion matrix

from sklearn.metrics import confusion_matrix,accuracy_score
accuracy=accuracy_score(test.target,labels)
mat=confusion_matrix(test.target,labels)
print(mat)

# Preprocessing category on new data based on trained model
def predict_category(s, train=train, model=model):
  pred= model.predict([s])
  return train.target_names[pred[0]]

# print accuracy of model
print(accuracy)

from sklearn.svm import SVC
clf = make_pipeline(TfidfVectorizer(),SVC(gamma='auto'))
clf.fit(train.data,train.target) 
pred_svm=clf.predict(test.data)
accuracy_svm=accuracy_score(test.target,pred_svm)

print(accuracy_svm)

from sklearn.ensemble import RandomForestClassifier
clf = make_pipeline(TfidfVectorizer(),RandomForestClassifier(n_estimators=100,random_state=0)) 
clf.fit(train.data,train.target)

pred_rf=clf.predict(test.data)
accuracy_rf=accuracy_score(test.target,pred_rf)
print(accuracy_rf)

# So here NB classifier perform better

predict_category('Jesus Christ')

predict_category('Mr. Narendra Modi is prime minister of India')

predict_category('As the reach of data science expands across the globe, developed, developing or underdeveloped, all countries are looking forward to enhance their data-friendly infrastructure, capacity and workforce. Especially in United Kingdoms, the technology is at rise with increasing demand for data science professionals. A recent report revealed that around 80 percent of the UK companies planning to hire data scientists or seek data consultancy in coming years. Several companies are seeking specialist skills and expertise to help navigate the potentials of uncertain market conditions.')

predict_category('The Indian Premier League is the most celebrated T20 event around the globe. With each passing year, its popularity is increasing exponentially. Here everything is top-notch from world-class players to renowned commentators. Even the IPL cheerleaders who entertain the audience with their special acts should be given their share of the credit. Their combined efforts have played a big role in making this tournament a huge success.')
