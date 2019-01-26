# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 

@author: Syed Hashim Reja
"""
#importing the required libraries
import pandas as pd
import numpy as np
import string
import nltk
from nltk.corpus import stopwords

#importing the dataset
dataset = pd.read_csv('cleaneddata.csv',header=None,index_col=0)

#looping through the dataset to remove the punctuations
data1 = []
for i in dataset[1]:
    words = ''.join(x for x in i if x not in string.punctuation)
    words = words.lower()
    words = words.split()
    data1.append(words)
    
#again looping through to remove the stopwords in english
finaldata = []
for i in data1[:]:
    repeated_words = ' '.join(x for x in i if not x in stopwords.words('english'))
    repeated_words = repeated_words.split()
    finaldata.append(repeated_words)
    
#finding the most repeating words from the finaldata
from collections import Counter
common_words = []
for i in finaldata:
    common = Counter(i)
    common_words.append(max(common.most_common()))
    
#dropping the numbers from tuple
common_words1 = []
for i in range(0,154):
    common_words1.append(common_words[i][0])
    
#creating a dataframe concatnating both common words and final data
finalresult = pd.DataFrame({'Common Words':common_words1,'Sonnets':finaldata})
#info
finalresult.info()
