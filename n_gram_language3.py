"""
Learning goal: In this tutorial, you'll learn how to find all the n-grams in a corpus 
& count how often each is used.
"""

# load in all the modules we're going to need
import nltk, re, string
from collections import Counter
from nltk.util import ngrams # function for making ngrams

# this corpus is pretty big, so let's look at just one of the files in it

#with open("../input/spanish_corpus/spanishText_15000_20000", "r", encoding='latin-1') as file:
with open("spanish_corpus/spanishText_15000_20000", "r", encoding='latin-1') as file:
    text = file.read()

# check to make sure the file read in alright; let's print out the first 1000 characters
#print(text[0:1000])
print('=====================================')
# let's do some preprocessing. We don't care about the XML notation, new lines 
# or punctuation marks other than periods. (We'll consider the end of the sentence
# a "word") We also don't want to consider capitalization. 

# get rid of all the XML markup
text = re.sub('<.*>','',text)

# get rid of the "ENDOFARTICLE." text
text = re.sub('ENDOFARTICLE.','',text)

# get rid of punctuation (except periods!)
punctuationNoPeriod = "[" + re.sub("\.","",string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)

# make sure it looks ok
#print(text[0:1000])

#text1=text[0:1000]
print('====================================')
# first get individual words
tokenized = text.split()

# and get a list of all the bi-grams
esBigrams = list(ngrams(tokenized, 3))

# If you like, you can uncomment the next like to take a look at 
# the first ten to make sure they look ok. Please note that doing so 
# will consume the generator & will break the next block of code, so you'll
# need to re-comment it and run this block again to get it to work.
#print((esBigrams)[10:50])

print('=======================================')

# get the frequency of each bigram in our corpus
#esBigramFreq = collections.Counter(esBigrams)
esBigramFreq = Counter(esBigrams)

# what are the ten most popular ngrams in this Spanish corpus?
count= esBigramFreq.most_common(10)

print(count)