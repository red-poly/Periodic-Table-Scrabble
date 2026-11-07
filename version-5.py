#This version is capable of inputting words from a .txt file, perfectly splitting them, counting points and outputting to a .txt file.
master_symbols={"h":1,"he":1,"li":2,"be":2,"b":2,"c":2,"n":2,"o":2,"f":2,"ne":2,"na":3,"mg":3,"al":3,"si":3,"p":3,"s":3,"cl":3,"ar":3,"k":4,"ca":4,"sc":4,"ti":4,"v":4,"cr":4,"mn":4,"fe":4,"co":4,"ni":4,"cu":4,"zn":4,"ga":4,"ge":4,"as":4,"se":4,"br":4,"kr":4,"rb":6,"sr":6,"y":6,"zr":6,"nb":6,"mo":6,"tc":6,"ru":6,"rh":6,"pd":6,"ag":6,"cd":6,"in":6,"sn":6,"sb":6,"te":6,"i":6,"xe":6,"cs":6,"ba":6,"la":6,"ce":6,"pr":6,"nd":6,"pm":6,"sm":6,"eu":6,"gd":6,"tb":6,"dy":6,"ho":6,"er":6,"tm":6,"yb":6,"lu":6,"hf":6,"ta":6,"w":6,"re":6,"os":6,"ir":6,"pt":6,"au":6,"hg":6,"tl":6,"pb":6,"bi":6,"po":6,"at":6,"rn":6,"fr":6,"ra":6,"ac":5,"th":5,"pa":5,"u":5,"np":5,"pu":5,"am":5,"cm":5,"bk":5,"cf":5,"es":5,"fm":5,"md":5,"no":5,"lr":5,"rf":6,"db":6,"sg":6,"bh":6,"hs":6,"mt":6,"ds":6,"rg":6,"cn":6,"nh":6,"fl":6,"mc":6,"lv":6,"ts":6,"og":6}
wordHolder = {
    
}
def wordSplitter(master_symbols, txt):
    symbols={"h":1,"he":1,"li":2,"be":2,"b":2,"c":2,"n":2,"o":2,"f":2,"ne":2,"na":3,"mg":3,"al":3,"si":3,"p":3,"s":3,"cl":3,"ar":3,"k":4,"ca":4,"sc":4,"ti":4,"v":4,"cr":4,"mn":4,"fe":4,"co":4,"ni":4,"cu":4,"zn":4,"ga":4,"ge":4,"as":4,"se":4,"br":4,"kr":4,"rb":6,"sr":6,"y":6,"zr":6,"nb":6,"mo":6,"tc":6,"ru":6,"rh":6,"pd":6,"ag":6,"cd":6,"in":6,"sn":6,"sb":6,"te":6,"i":6,"xe":6,"cs":6,"ba":6,"la":6,"ce":6,"pr":6,"nd":6,"pm":6,"sm":6,"eu":6,"gd":6,"tb":6,"dy":6,"ho":6,"er":6,"tm":6,"yb":6,"lu":6,"hf":6,"ta":6,"w":6,"re":6,"os":6,"ir":6,"pt":6,"au":6,"hg":6,"tl":6,"pb":6,"bi":6,"po":6,"at":6,"rn":6,"fr":6,"ra":6,"ac":5,"th":5,"pa":5,"u":5,"np":5,"pu":5,"am":5,"cm":5,"bk":5,"cf":5,"es":5,"fm":5,"md":5,"no":5,"lr":5,"rf":6,"db":6,"sg":6,"bh":6,"hs":6,"mt":6,"ds":6,"rg":6,"cn":6,"nh":6,"fl":6,"mc":6,"lv":6,"ts":6,"og":6}
    word=list(txt)
    global lstSymbols
    lstSymbols = []
    ltrList = []
    doConcat = True
    nextIndex = 1
    currentIndex = 0
    global validity
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
            break
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
        global listSymbols
        listSymbols = lstSymbols
    else:
        lstSymbols.clear()

def postProcessing(lstSymbols, master_symbols, wordHolder):
    #---------------------------------------------------------------------------------------------

    #point counter
    pointHolder = []
    if validity == True:
        for z in lstSymbols:
            pointHolder.append(master_symbols[z])
    else:
        pass
    #---------------------------------------------------------------------------------------------

    #converter
    conversionKey = {"h":"H","he":"He","li":"Li","be":"Be","b":"B","c":"C","n":"N","o":"O","f":"F","ne":"Ne","na":"Na","mg":"Mg","al":"Al","si":"Si","p":"P","s":"S","cl":"Cl","ar":"Ar","k":"K","ca":"Ca","sc":"Sc","ti":"Ti","v":"V","cr":"Cr","mn":"Mn","fe":"Fe","co":"Co","ni":"Ni","cu":"Cu","zn":"Zn","ga":"Ga","ge":"Ge","as":"As","se":"Se","br":"Br","kr":"Kr","rb":"Rb","sr":"Sr","y":"Y","zr":"Zr","nb":"Nb","mo":"Mo","tc":"Tc","ru":"Ru","rh":"Rh","pd":"Pd","ag":"Ag","cd":"Cd","in":"In","sn":"Sn","sb":"Sb","te":"Te","i":"I","xe":"Xe","cs":"Cs","ba":"Ba","la":"La","ce":"Ce","pr":"Pr","nd":"Nd","pm":"Pm","sm":"Sm","eu":"Eu","gd":"Gd","tb":"Tb","dy":"Dy","ho":"Ho","er":"Er","tm":"Tm","yb":"Yb","lu":"Lu","hf":"Hf","ta":"Ta","w":"W","re":"Re","os":"Os","ir":"Ir","pt":"Pt","au":"Au","hg":"Hg","tl":"Tl","pb":"Pb","bi":"Bi","po":"Po","at":"At","rn":"Rn","fr":"Fr","ra":"Ra","ac":"Ac","th":"Th","pa":"Pa","u":"U","np":"Np","pu":"Pu","am":"Am","cm":"Cm","bk":"Bk","cf":"Cf","es":"Es","fm":"Fm","md":"Md","no":"No","lr":"Lr","rf":"Rf","db":"Db","sg":"Sg","bh":"Bh","hs":"Hs","mt":"Mt","ds":"Ds","rg":"Rg","cn":"Cn","nh":"Nh","fl":"Fl","mc":"Mc","lv":"Lv","ts":"Ts","og":"Og"}
    convertedList = []
    if validity == True:
        for a in listSymbols:
            convertedList.append(conversionKey[a])
            joinedList = "".join(convertedList)
    else:
        pass
    #---------------------------------------------------------------------------------------------

    #word holder
    if validity == True:
        wordHolder.update({joinedList: sum(pointHolder)})
    else:
        pass
    convertedList.clear()
    pointHolder.clear()
print("Running...")
for line in open("input.txt"):
    line = line.lower()
    txt = line.strip()
    wordSplitter(master_symbols, txt)
    postProcessing(lstSymbols, master_symbols, wordHolder)
print (wordHolder)
print("Adding " + str(len(wordHolder)) + " word(s) to the file...")

ordered = list(wordHolder.items())
ordered.sort(key=lambda x: x[1], reverse=True)

with open("output.txt", "w") as f:
    for key, value in ordered:
        f.write(f"{key}: {value}\n")
    f.write("\n")
    f.write(f"Total words: {len(wordHolder)}\n")
    f.write(f"Total points: {sum(wordHolder.values())}\n")

clearFile = input("Done! Would you like to clear the file? (y/n): ")
if clearFile == "y":
    open("output.txt", "w").close()
    print("File cleared!")
