"""
From this paper: https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf

External dependencies: nltk, numpy, networkx

"""

import io
import nltk
import itertools
from operator import itemgetter
import networkx as nx
import os

def unique_everseen(iterable, key=None):
    # Set of unique terms
    unique = set()
    unique_add = seen.add
    if key is None:
        for element in itertools.ifilterfalse(seen.__contains__, iterable):
            unique_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in unique:   
                unique_add(k)
                yield element

def keywords(text):
    #word-tokenization and tag
    token = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(token)

    #tag-filteration
    need_tag = ["NN","JJ","NNP"]
    filtered_tag = [item for item in tagged if item[1] in need_tag]
  
    #normalized tokens
    normalized_token = [(item[0].replace('.',''),item[1]) for item in filtered_tag)
    
    #unique_wordset
    unique_wordset = unique_everseen([x[0] for x in normalized_token])
    wordset = list(unique_wordset)

    #Build Word-Graph
    w-graph = BuildGraph(wordset)

    #Calculate TextRank
    w-graph-rank = nx.pagerank(w-graph,alpha="0.8",weight='weight')

    #Sort on the basis of the valueof nodes
    keywords = sorted(w-graph-rank, key=w-graph-rank.get, reverse=True)

    top = 0.2*len(keywords)

    return keywords[0:top]

def score(word1,word2,text,wordset):
    # Number of connections between two words, a connection is when both words
    # occur in same sentence
    score = 0
    for sentence in text.split('\n'):
        if word in sentence:
            if word1 in sentence and word2 in sentence:
                score += 1
    return score

def BuildGraph(nodes):
    "nodes - list of hashables that represents the nodes of the graph"
    graph = nx.Graph() #initialize an undirected graph
    graph.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))
    #add edges to the graph (weighted by score)
    for pair in nodePairs:
        word1 = pair[0]
        word2 = pair[1]
        w = float(1/score(word1, word2))
        graph.add_edge(word1, word2, weight=w)
    return graph
