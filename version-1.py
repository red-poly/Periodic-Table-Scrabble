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
    for x in word:
        #print(word) #goes at the end of the program along with the sum of the points
        print(symbols[x]) #replace with check if the symbol is in the dictionary and if it is, add the symbol to the list
        lstSymbols.append(x) #add at the end of the function, reserved for successfully found symbols in the dictionary
    print(lstSymbols)

wordSplitter(symbols)
