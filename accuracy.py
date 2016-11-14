import os

def ans():
    path = os.getcwd()
    ans_path = path + str("/") + str("answers.csv")
    ans_dict = {}
    with open(ans_path,'r') as f:
        for line in f.read().split("\n"):
            if len(line.split(",")) == 2:
                ans_dict[line.split(",")[0]] = line.split(",")[1].replace('\r','')
    return ans_dict
