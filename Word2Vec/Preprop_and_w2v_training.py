print("Antas")

import kagglehub

# Download latest version
path = kagglehub.dataset_download("saurabhbadole/game-of-thrones-book-dataset")

print("Path to dataset files:", path)

import gensim
from gensim.models import Word2Vec

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os

import nltk
from nltk import sent_tokenize
from gensim.utils import simple_preprocess

# Download stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

stop_words = set(stopwords.words('english'))
print("Stopwords: ")
print(stop_words)

documents = []

for filename in os.listdir(path):
  with open(os.path.join(path, filename), encoding="utf-8", errors="ignore") as f:
    text = f.read()
    sents_list = sent_tokenize(text)
    for sent in sents_list:
      documents.append(simple_preprocess(sent))

print("Sentences tokenised and simple preprocessed each sentence.")
print("Sample: len of a doc")
print(len(documents[98]))
print("---------------------------------------------------------------------------------")

#start from removing stopwods in each document(sentence).
new_documents = []
for doc in documents:
  new_doc = [word for word in doc if word not in stop_words]
  new_documents.append(new_doc)
print("Stopword Removed.")
print("Sample len of same doc:")    
print(len(new_documents[98]))
print("--------------------------------------------------------------------------------")

#Word2Vec model initialized
model = gensim.models.Word2Vec(
    window=10,
    min_count=2
)

#building vocab for custom model
model.build_vocab(new_documents)

#training the model
model.train(new_documents, total_examples=model.corpus_count, epochs=model.epochs)

#Model is now trained and ready for use with it's function

print("using functions of a Word2Vec model")
print("Most similar to places: ")
model.wv.most_similar("places")

#embeddings of the words
#by default size =100
model.wv["king"]

mo = model.wv.get_normed_vectors()
print(mo.shape)

print("Similaity b/w King and Queen through our embeddings: ")
print(model.wv.similarity("king", "queen"))