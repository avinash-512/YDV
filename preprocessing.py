# INPUT: Files from subtitles directory
# OUTPUT: Files (normal text) to subtitle-text directory

    
        # OUTPUT FORMAT = All text files should have only text not the
        # timestamps!

import os
import pycaption
def list_files(folder):
    current_path = os.getcwd()
    print(current_path)
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    list_command = "ls " + folder_path
    file_list = os.popen(list_command).read().split("\n")
    file_list.remove('')
    return file_list

def process(file_list,folder):
    webtv_reader = pycaption.WebVTTReader()
    current_path = os.getcwd()
    output_folder = os.getcwd() + str("/") + str(output_folder)
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    for f in file_list:
        file_path = folder_path + str("/") + str(f)
        print("converting "+f+"....")
        output_path = outtput_folder + str("/") + str(f)
        f1 = open(file_path,'r')
        out = pycation.WebVTTWriter().write(f1).encode("utf-8")
        fout = f.replace(".vtt",".srt")
        f2 = open(output_path,"w")
        f2.write(fout)
        f2.close()
        f1.close()

