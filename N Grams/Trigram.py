#for analyzing 1 word like in cold - col then it see old and assign probability to it characters this is called trigrams ( i.e only three word or characters )
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams

sentence = "I am learning AI"
tokens = word_tokenize(sentence)
trigrams = list(ngrams(tokens, 3))
print('Trigrams:', trigrams)

print(trigrams)
