import operator
import os
from collections import defaultdict
from nltk.corpus import wordnet as wn

"""
        Mention what input you need
        Input:

        Mention the output format
        Output:
"""
def initialize():
    path = os.getcwd()
    file_path = path + str('/') + str('wn-domains-3.2-20070223')
    synset2domains =  defaultdict(list)
    for i in open(file_path,'r'):
        ssid,doms = i.strip().split('\t')
        doms = doms.split()
        synset2domains[ssid] = doms
    return synset2domains

def assign_domains(sense_dict):
    domains = {}
    synset2domains = initialize()
    for key in sense_dict:
        flag,key_domains = extract_domain(key,synset2domains)
        if not flag:
            continue
        for key_domain in key_domains:
            if key_domain == 'factotum':
                continue
            if key_domain in domains:
                domains[key_domain] += 1
            else:
                domains[key_domain] = 1
    sorted_domains = sorted(domains.items(),key=operator.itemgetter(1),reverse=True)
    return sorted_domains

def extract_domain(key,synset2domains):
    all_keys = key.hyponyms()
    answer =[]
    all_keys.append(key)
    for k in all_keys:
        try:
            k.offset()
        except:
	    continue 
        ssid = str(k.offset()).zfill(8) + "-" + key.pos()
        if synset2domains[str(ssid)]:
            for i in synset2domains[ssid]:
                answer.append(i) 
    if len(answer):
	return 1,answer
    else:
	return 0,answer
