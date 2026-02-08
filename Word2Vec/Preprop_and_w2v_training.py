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

from nltk.corpus import stopwords

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
print("Sample: ")
print(documents[0])
print("---------------------------------------------------------------------------------")

#start from removing stopwods in each document(sentence).