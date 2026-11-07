#this version is capable of splitting the word into its individual letters and checking if
#they are in the dictionary, it is able to check for valid symbols, however it is not capable
#of counting points and outputting the word as a string


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
    "ne": 2
}
def wordSplitter(symbols):
    txt=input("Enter a string: ")
    word=list(txt)
    lstSymbols = []
    ltrList = []
    concatNum = -1
    for x in word:
        #print(word) #goes at the end of the program along with the sum of the points
        ltrList.append(x)
        #print(symbols[x]) #replace with check if the symbol is in the dictionary and if it is, add the symbol to the list
        if x in symbols:
            lstSymbols.append(x)
        elif x not in symbols:
            concat = ltrList[concatNum] + x
            if concat in symbols:
                lstSymbols.append(concat)
            else:
                print(txt + " is not valid")
        concatNum = concatNum + 1
    print(lstSymbols)
wordSplitter(symbols)
