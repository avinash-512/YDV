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
path = os.getcwd()
file_path = path + str('/') + str('wn-domains-3.2-20070223')
synset2domains = defaultdict(list)
for i in open(file_path,'r'):
    ssid,doms = i.strip().split('\t')
    doms = doms.split()
    synset2domains[ssid] = doms

def assign_domains(sense_dict):
    domains = {}
    for key in sense_dict:
        if sense_dict['key'] == 'None':
            continue
        flag,key_domains = extract_domain(key)
        if not flag:
            continue
        for key_domain in key_domains:
            if key_domain in domains:
                doimains[key_domain] += 1
            else:
                domains[key_domain] = 1
    sorted_domains = sorted(domains.items(),key=operator.itemgetter(1))
    return sorted_domains

def extarct_domain(key):
    ssid = str(key.offset).zfill(8) + "-" + key.pos()
    if sysnset2domains[ssid]:
        return 1,synset2domains[ssid]
    else:
        return 0,0
