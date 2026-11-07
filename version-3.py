#This version is capable of perfectly splitting words
master_symbols = {
    "h": 1,
    "he": 1,
    "li": 2,
    "be": 2,
    "b": 2,
    "c": 2,
    "n": 2,
    "o": 2,
    "f": 2,
    "ne": 2,
    "y": 2
}
def wordSplitter(master_symbols):
    global symbols
    symbols = {
        "h": 1,
        "he": 1,
        "li": 2,
        "be": 2,
        "b": 2,
        "c": 2,
        "n": 2,
        "o": 2,
        "f": 2,
        "ne": 2,
        "y": 2
    }
    txt=input("Enter a string: ")
    word=list(txt)
    global lstSymbols
    lstSymbols = []
    ltrList = []
    doConcat = True
    nextIndex = 1
    currentIndex = 0
    validity = True
    for x in word:
        ltrList.append(x)
        if nextIndex >= len(word):
            doConcat = False
        if doConcat == True:
            concat = x + word[nextIndex]
            if concat in symbols:
                lstSymbols.append(concat)
                word[currentIndex] = concat
                word.pop(nextIndex)
                symbols.pop(concat)
            nextIndex = nextIndex + 1
        elif x in symbols:
            lstSymbols.append(x)
            symbols.pop(x)
            nextIndex = nextIndex + 1
        if nextIndex >= len(word):
            doConcat = False
        currentIndex = currentIndex + 1
    lstSymbols.clear()
    for y in word:
        if y in master_symbols:
            lstSymbols.append(y)
        else:
            print(txt + " is not valid")
            validity = False
            break
    if validity == True:
        print(lstSymbols)
        global listSymbols
        listSymbols = lstSymbols
    else:
        lstSymbols.clear()
wordSplitter(master_symbols)

