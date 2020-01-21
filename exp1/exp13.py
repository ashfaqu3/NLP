import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
f=open("sample","r")
data=f.read().replace('\n','')
print(data)
noise=[';',',','!','.','<p>','<h>','@','/']
for i in noise:
    data=data.replace(i, '')
print(data)