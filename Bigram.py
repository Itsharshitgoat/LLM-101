#for analyzing 1 word like in cold - co then it see ld and assign probability to it characters this is called bigram ( i.e only two word or characters )
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
bigrams = list(ngrams(tokens, 2)) # Bigram

print(bigrams)