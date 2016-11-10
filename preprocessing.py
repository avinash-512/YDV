# INPUT: Files from subtitles directory
# OUTPUT: Files (normal text) to subtitle-text directory

    
        # OUTPUT FORMAT = All text files should have only text not the
        # timestamps!

import os
import pycaption


def pre_process(folder,output_folder):
    #Initializing WebVTT Reader
    webtv_reader = pycaption.WebVTTReader()
    current_path = os.getcwd()
    #Collecting file_names
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    list_command = "ls " + folder_path
    print("Collecting subtitle files......")
    file_list = os.popen(list_command).read().split("\n")
    file_list.remove('')
    output_folder = os.getcwd() + str("/") + str(output_folder)
    folder_path = str(current_path) + str("/") + str(folder) + str("/")
    #Converting files to srt format
    for f in file_list:
        if '.vtt' not in f:
            continue
        file_path = folder_path +  str(f)
        print("converting " + f + "....")
        output_path = output_folder + str("/") + str(f.replace('.vtt','.srt'))
        f1 = open(file_path,'r').read()
        n = webtv_reader.read(f1.decode('utf-8'))
        out = pycaption.SRTWriter().write(n).encode("utf-8").split("\n")
        fout = ''
        f = ''
        for line in out:
            if "-->" in line:
                continue
            if line in fout:
                continue
            if line == '\n':
                continue
            if line == '':
                continue
            try:
                x = int(line)
                continue
            except:
                fout += str(line)
                fout += str(" ")
        for line in fout.split("\n"):
            if line in f:
                continue
            else:
                f += str(line) + "\n"
        f2 = open(output_path,"w")
        f2.write(f)
        f2.close()


