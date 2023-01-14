from sys import argv
punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~«»\n'

def parseStringListToSentence(l:list) -> str:
    s = ""
    for i in l:
        s = s+i+" "
    return s

with open(argv[1], "r") as textfile:
    f = textfile.read()
    text = f.replace("\n", " ").translate(str.maketrans('', '', punctuation)).lower().split(" ")
    with open(argv[2], "r") as searchsentensefile:
        searchwords = searchsentensefile.read().replace("\n", "").split(" ")
        for i in range(len(text)-len(searchwords)):
            for j in range(len(searchwords)):
                if searchwords[j] == "_":
                    if j == len(searchwords)-1:
                        print(parseStringListToSentence(text[i:i+len(searchwords)]))
                    else:
                        continue
                elif text[i+j] == searchwords[j]:
                    if j == len(searchwords)-1:
                        print(parseStringListToSentence(text[i:i+len(searchwords)]))
                else:
                    break