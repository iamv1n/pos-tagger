# -*- coding: utf-8 -*-
"""pos_tagger.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z-nqX1RVgBFzjiTFCpHkZMGJ1SYiDLb_
"""

import nltk
nltk.download('treebank')
nltk.download('punkt')


from nltk import word_tokenize, pos_tag

import nltk

tagged_sentences = nltk.corpus.treebank.tagged_sents()
 
print (tagged_sentences[0])
print ("Tagged sentences: ", len(tagged_sentences))
print ("Tagged words:", len(nltk.corpus.treebank.tagged_words()))

"""#Feature Extraction"""

def features(sentence, index):
    """ sentence: [w1, w2, ...], index: the index of the word """
    return {
        'word': sentence[index],
        'is_first': index == 0,
        'is_last': index == len(sentence) - 1,
        'is_capitalized': sentence[index][0].upper() == sentence[index][0],
        'is_all_caps': sentence[index].upper() == sentence[index],
        'is_all_lower': sentence[index].lower() == sentence[index],
        'prefix-1': sentence[index][0],
        'prefix-2': sentence[index][:2],
        'prefix-3': sentence[index][:3],
        'suffix-1': sentence[index][-1],
        'suffix-2': sentence[index][-2:],
        'suffix-3': sentence[index][-3:],
        'prev_word': '' if index == 0 else sentence[index - 1],
        'next_word': '' if index == len(sentence) - 1 else sentence[index + 1],
        'has_hyphen': '-' in sentence[index],
        'is_numeric': sentence[index].isdigit(),
        'capitals_inside': sentence[index][1:].lower() != sentence[index][1:]
    }

import pprint 
pprint.pprint(features(['This', 'is', 'a', 'sentence'], 2))
 
# {'capitals_inside': False,
#  'has_hyphen': False,
#  'is_all_caps': False,
#  'is_all_lower': True,
#  'is_capitalized': False,
#  'is_first': False,
#  'is_last': False,
#  'is_numeric': False,
#  'next_word': 'sentence',
#  'prefix-1': 'a',
#  'prefix-2': 'a',
#  'prefix-3': 'a',
#  'prev_word': 'is',
#  'suffix-1': 'a',
#  'suffix-2': 'a',
#  'suffix-3': 'a',
#  'word': 'a'}

# Small helper function to strip the tags from our tagged corpus and feed it to our classifier
def untag(tagged_sentence):
    return [w for w, t in tagged_sentence]

"""## Building training set

"""

# Split the dataset for training and testing
cutoff = int(.75 * len(tagged_sentences))
training_sentences = tagged_sentences[:cutoff]
test_sentences = tagged_sentences[cutoff:]
 
print (len(training_sentences))   # 2935
print (len(test_sentences))       # 979
 
def transform_to_dataset(tagged_sentences):
    X, y = [], []
 
    for tagged in tagged_sentences:
        for index in range(len(tagged)):
            X.append(features(untag(tagged), index))
            y.append(tagged[index][1])
 
    return X, y
 
X, y = transform_to_dataset(training_sentences)

"""## **Training**

Training the Classifier with Decision Tree Classifier
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
 
clf = Pipeline([
    ('vectorizer', DictVectorizer(sparse=False)),
    ('classifier', DecisionTreeClassifier(criterion='entropy'))
])
 
clf.fit(X[:20000], y[:20000])   
 
print ('Training completed')
 
X_test, y_test = transform_to_dataset(test_sentences)
 
print ("Accuracy:", clf.score(X_test, y_test))

def pos_ttag(sentence):

    sent = word_tokenize(sentence)
    tags = clf.predict([features(sent, index) for index in range(len(sent))])
    return [(sent[i], tags[i]) for i in range(len(sent))]
 

sentence = "Hi, My name is Vineet and I am a Developer"

print (pos_ttag(sentence))

"""### POS Tags for Reference

1.	CC	Coordinating conjunction
2.	CD	Cardinal number
3.	DT	Determiner
4.	EX	Existential there
5.	FW	Foreign word
6.	IN	Preposition or subordinating conjunction
7.	JJ	Adjective
8.	JJR	Adjective, comparative
9.	JJS	Adjective, superlative
10.	LS	List item marker
11.	MD	Modal
12.	NN	Noun, singular or mass
13.	NNS	Noun, plural
14.	NNP	Proper noun, singular
15.	NNPS	Proper noun, plural
16.	PDT	Predeterminer
17.	POS	Possessive ending
18.	PRP	Personal pronoun
19.	PRP	Possessive pronoun
20.	RB	Adverb
21.	RBR	Adverb, comparative
22.	RBS	Adverb, superlative
23.	RP	Particle
24.	SYM	Symbol
25.	TO	to
26.	UH	Interjection
27.	VB	Verb, base form
28.	VBD	Verb, past tense
29.	VBG	Verb, gerund or present participle
30.	VBN	Verb, past participle
31.	VBP	Verb, non-3rd person singular present
32.	VBZ	Verb, 3rd person singular present
33.	WDT	Wh-determiner
34.	WP	Wh-pronoun
35.	WP	Possessive wh-pronoun
36.	WRB	Wh-adverb

"""