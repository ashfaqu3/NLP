import nltk
from nltk.stem import PorterStemmer
print("Porter Stemmer")

pst=PorterStemmer()
p=pst.stem("eating")
print("After stemming",p)
print()

list=["Give","giving","given","Given","giver","gives","gave","regives"]
for word in list:
	print(word+":"+pst.stem(word))
print("\Stemming a sentence")
from nltk.tokenize import word_tokenize
text="In Brazil they drive on the right-hand side of the road. Brazil has a large coastline on the eastern side of south America. Brazil is rich in natural resources"

text1=word_tokenize(text)
for word in text1:
	print(pst.stem(word))

#with different stemmer
print("\n==========================\n")
print("Lancaster Stemmer")
from nltk.stem import LancasterStemmer
lst=LancasterStemmer()

list=["Give","giving","given","Given","giver","gives","gave","regives"]
for word in list:
	print(word+":"+lst.stem(word))
