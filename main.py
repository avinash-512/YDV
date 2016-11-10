from preprocessing import pre_process
from extract_senses import calculate_keysenses
from wordnet import assign_domains
import os
from wsd import wsd
from assign_cat import assign
pre_process('subtitles','subtitles-text')
current_path = os.getcwd()
list_command = "ls " + current_path + str("/") + 'subtitles-text' +str("/")
file_list = os.popen(list_command).read().split("\n")
file_list.remove('')
uni = set()
for f in file_list:
    print("Extracting keywords and its sense from " + f +".....")
    file_path = current_path + str("/") + 'subtitles-text' + str("/") + str(f)
    with open(file_path,'r') as f1:
        text =f1.read().decode('utf-8')
        keys = calculate_keysenses(text)
        domains = assign_domains(keys)
        category = assign(domains)
        if len(category) == 0:
            category.append('others')
