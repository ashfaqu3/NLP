import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
data="Greetings of the day.Hi Ashfaque how are you"
print("Sentence:\n")
word_tokens=word_tokenize(data)
print(word_tokens)
print("\n Filtered Sentence:\n")
stop_words=set(stopwords.words('english'))
filtered_sentence=[w for w in word_tokens if not w in stop_words]
print(filtered_sentence)
print("\n Stop Words:\n")
print(stop_words)