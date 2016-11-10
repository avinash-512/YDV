from nltk.corpus import wordnet as wn
import operator
import nltk

def words(text):
    token = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(token)
    need_tag = ["NN","JJ","NMP"]
    filtered_tag = [item for item in tagged if item[1] in need_tag]
    wordset = set()
    for x in filtered_tag:
        wordset.add(x[0])
    return [i for i in wordset]

def make_sense(text):
    wordset = words(text)
    dictionary = {}
    for word in wordset:
        dictionary[word] = wn.synsets(word)
    
    return dictionary

def calculate_keysenses(text):
    sense_dict = make_sense(text)
    sense_count = {}
    for word in sense_dict:
        for sense in sense_dict[word]:
            if sense in sense_count:
                sense_count[sense] += 1
            else:
                sense_count[sense] = 1
    sorted_keysenses = sorted(sense_count.items(),key=operator.itemgetter(1))
    pct = int(len(text.split(' '))*0.3)
    return [x[0] for x in sorted_keysenses]

