import pandas as pd
import numpy as np
import re
import spacy
import nltk

from nltk.tokenize.toktok import ToktokTokenizer
tokenizer=ToktokTokenizer()

nlp=spacy.load('en_core',parse=True,tag=True,entity=True)
stopword_list=set(nltk.corpus.stopwords.words('english'))
stopword_list.add('write')
stopword_list.add('query')
stopword_list.add('sql') 

Drugs=pd.read_excel("C:\\Users\\sagar\\Downloads\\EmpSqlQueries.xlsx",header=None,names=['Query'])
print(Drugs.head())

def remove_special_char(text):
    pattern=r'[^a-zA-z0-9\s]'
    text=re.sub(pattern,'',text)
    return text

remove_special_char("Hello my name is $@gaR")

def lemmatization(text):
    text=nlp(text)
    text=' '.join([word.lemma_ if word.lemma_!='-PRON-' else word.text for word in text])
    return text

lemmatization("My System Crashed Yesterday and Today is Hackathon")

def remove_Stopword(text):
    tokens=tokenizer.tokenize(text)
    tokens=[token.strip() for token in tokens ]
    filtered_tokens=[token.lower() for token in tokens if token.lower() not in stopword_list]
    filtered_tokens=' '.join(filtered_tokens)
    return filtered_tokens

remove_Stopword("Hey Hari  what how are you")

def normalized_Corpus(corpus):
    normalize_corpus=[]
    for doc in corpus:
        doc[0]=re.sub(r'[\r|\n|\r\n]+',' ',doc[0])
        doc[0]=lemmatization(doc[0])
        special_char_pattern = re.compile(r'([{.(-)!}])')
        doc[0] = remove_special_char(doc[0])  
        # remove extra whitespace
        doc[0] = re.sub(' +', ' ', doc[0])
        # remove stopwords
        doc[0] = remove_Stopword(doc[0])
        
        #if doc[0] turns out to be empty string, do not append this to the corpus.
        if doc[0] != "":
            normalize_corpus.append([doc[0],doc[1]])
    return normalize_corpus


"""Drugs['clean_text']=normalized_Corpus(Drugs['Query'])
norm_corpus=list(Drugs['clean_text'])

#Sample
Drugs.iloc[1][['Query','clean_text']].to_dict()"""


"""
sentence=str(Drugs.iloc[1].Query)
sentence_nlp=nlp(sentence)
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp if str(word).lower() not in stopword_list]
#spacy_pos_tagged2 =[]
#for x in spacy_pos_tagged:
#    if str(x[0]).lower() not in stopword_list:
#        print(x[0])
#        spacy_pos_tagged2.append(x)
#spacy_pos_tagged = [x for x in spacy_pos_tagged if str(x[0]).lower() not in stopword_list]
#print(type(spacy_pos_tagged2))

p=pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type'])
p
"""



'''
from spacy import displacy

displacy.render(sentence_nlp, jupyter=True, 
                options={'distance': 110,
                         'arrow_stroke': 2,
                         'arrow_width': 8})
                         '''

#sentence = str(Drugs.Query)
#nltk_pos_tagged = nltk.pos_tag(sentence.split())
#print(nltk_pos_tagged)


#Drugs.head()

Drugs['preprocessed'] = Drugs['Query'].apply(str.split)

Drugs['preprocessed'] = Drugs['preprocessed'].apply(nltk.pos_tag)

print(Drugs['preprocessed'][0])

Drugs['preprocessed'].apply(lambda arg: [list(x) for x in arg])

Drugs['preprocessed'] = Drugs['preprocessed'].apply(lambda arg: [list(x) for x in arg])

Drugs['pos'] = Drugs['preprocessed'].apply(normalized_Corpus)

print(Drugs.head())

print(Drugs['pos'][0])

m=Drugs['pos'].to_dict()
l=[]
for item in Drugs['pos']:
    d={}
    for i in item:
        d[i[0]]=i[1]
    l.append(d)

for l1 in l:
    print(l1)

Drugs['new']=l#pd.Series(l)

print(Drugs.head())

Drugs['dict'] = Drugs['pos'].apply({})
