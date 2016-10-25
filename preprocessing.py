# INPUT: Files from subtitles directory
# OUTPUT: Files (normal text) to subtitle-text directory

    
        # OUTPUT FORMAT = All text files should have only text not the
        # timestamps!

import os

def list_files(folder):
    current_path = os.getcwd()
    print(current_path)
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    list_command = "ls " + folder_path
    file_list = os.popen(list_command).read().split("\n")
    file_list.remove('')
    return file_list

def process(file_list,folder):
    current_path = os.getcwd()
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    for f in file_list:
        file_path = folder_path + f
        f1 = open(file_path,'r')
        for line in f1:
            print line

file_list = list_files('subtitles')
process(file_list,'subtitles')

