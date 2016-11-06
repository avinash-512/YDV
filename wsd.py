from pywsd1 import disambiguate


def wsd(keywords, text):
    dictionary = {}
    d = disambiguate(text)
    for key in keywords:
        for words in d:
            if key == words[0]:
                dictionary[key] = words[1]
                break
    return dictionary 

