from preprocessing import pre_process
from textrank import keywords
import os
from wsd import wsd
pre_process('subtitles','subtitles-text')
current_path = os.getcwd()
list_command = "ls " + current_path + str("/") + 'subtitles-text' +str("/")
file_list = os.popen(list_command).read().split("\n")
file_list.remove('')
for f in file_list:
    print("Extracting keywords and its sense from " + f +".....")
    file_path = current_path + str("/") + 'subtitles-text' + str("/") + str(f)
    with open(file_path,'r') as f1:
        text =f1.read().decode('utf-8')
        keys = keywords(text)
        sense_dictionary = wsd(keys,text)


