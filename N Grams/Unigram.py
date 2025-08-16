#for analyzing 1 word like in cold - c then it see o and assign probability to it characters this is called unigram ( i.e only one word or characters )
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
unigrams = list(ngrams(tokens, 1))
print('Unigrams:', unigrams)

print(unigrams)
