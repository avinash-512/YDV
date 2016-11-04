from preprocessing import pre_process
from textrank import keywords
import os

pre_process('subtitles','subtitles-text')
current_path = os.getcwd()
list_command = "ls " + current_path + str("/") + 'subtitles-text' +str("/")
file_list = os.popen(list_command).read().split("\n")
file_list.remove('')
os.system('mkdir sub-key')
for f in file_list:
    print("Extracting keywords from " + f +".....")
    file_path = current_path + str("/") + 'subtitles-text' + str("/") + str(f)
    key_path = current_path + str("/") + 'sub-key' + str("/")
    key_file = key_path + str(f.replace('.srt','.txt'))
    with open(file_path,'r') as f1:
        keys = keywords(f1.read().decode('utf-8'))
        with open(key_file,'a') as f2:
            print("Writing keywords to " + f.replace('.srt','.txt')+"......")
            for key in keys:
                f2.write(key.encode('utf-8'))
                f2.write("\n")


