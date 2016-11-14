from preprocessing import pre_process
from extract_senses import calculate_keysenses
from wordnet import assign_domains
import os
from accuracy import ans
from assign_cat import assign
pre_process('test','subtitles-text')
current_path = os.getcwd()
list_command = "ls " + current_path + str("/") + 'subtitles-text' +str("/")
file_list = os.popen(list_command).read().split("\n")
file_list.remove('')
uni = set()
cat_dict = {}
f2 = open("final.txt",'w')
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
        f2.write(f)
        cat_dict[f] = category
        f2.write("\t")
        f2.write(category[0])
        f2.write("\n")

ans_dict = ans()
count = 0
for f in ans_dict:
    if ans_dict[f] in cat_dict[f]:
        count +=1
n = count
d = len(ans_dict)
acc = (float(n)/float(d))*100
print acc
