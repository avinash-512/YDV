import nltk

text = nltk.word_tokenize("And now for somethong completely different")
tag = nltk.pos_tag(text)

print(text, tag)
