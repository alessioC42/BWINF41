from sys import argv
vocals = list("aeiouäöü")
def getRhymepart(word:str):
    vocallist = []
    for i in range(len(word)):
        if word[i] in vocals:
            vocallist.append(i)
    for i in range(len(vocallist)-1, -1, -1):
        if vocallist[i]-1 in vocallist:
            vocallist.pop(i)
    if len(vocallist) == 1:
        return word[vocallist[0]:]
    elif len(vocallist) >= 2:
        return word[vocallist[len(vocallist)-2]:]
    else:
        return -1

def match(wordlist:list) -> None:
    count = 0
    for i in range(len(wordlist)):
        for j in range(i+1, len(wordlist)):
            wordA = wordlist[i].copy()
            wordB = wordlist[j].copy()

            if not ((wordA["word"].endswith(wordB["word"]))
             or (wordB["word"].endswith(wordA["word"]))):
                if (str(wordA["rhymepart"]) == str(wordB["rhymepart"])):
                    print(wordA["word"] + " - "+wordB["word"])
                    count+=1
    print("\nfound "+str(count)+" matches in "+ argv[1])


words = []
with open(argv[1], "r") as file:
    file = file.read().splitlines()
    for word in file:
        w = word.lower()
        rhymepart = getRhymepart(w)
        if rhymepart == -1: continue
        if len(rhymepart)<len(w)/2:continue
        words.append({
            "word": w,
            "rhymepart": rhymepart
        })

match(words)

