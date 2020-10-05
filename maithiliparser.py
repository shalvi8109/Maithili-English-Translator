import unicodedata   #importing toRoman function from unicode data module to convert maithili text from devnagri script to roman script.
from msvcrt import getch  #importing getch function to stop the output screen in order to clearly show the output after execution

def toRoman(Sentence):   #sentence string is passed as argument to toRoman()
    engSentence=""
    print(Sentence)
    Words=Sentence.split()  #each word of the sentence are broken in order to generate their meaning using dictionay.txt
    #print(Words)
    for w in Words:
        #print(w)
        engword=""
        for c in w:
            #if w=='कल': print(c,'  ',unicodedata.name(c))
            charinfo=unicodedata.name(c).split()
            #print(charsplit)
            if len(charinfo)<2: continue
            lastsyll=charinfo[-1]
            if charinfo[1]=='VOWEL':
                engword+=lastsyll
            if charinfo[1]=='LETTER':
                engword+=lastsyll

        
        #print(w,'->',engword)
        engSentence+=engword+' '
    print(engSentence)
    return engSentence

def isVowel(c):  #function to check the character is vowel or not
    if c=='A' or c=='E' or c=='I' or c=='O' or c=='U' or c==':': return True
    else: return False

def match(word,root): #fuction which matches the word with the root word passed as an argument
    i=0
    j=0
    #if len(root)<pre or len(word)<pre: return False
    root+='$'
    word+='$'
    goodcon=0
    #print(word,'   ',root)
    
    while(word[i]!='$' and root[j]!='$'):
        #print('match ',word[i],' <-> ',root[j])
        if isVowel(word[i]):
            i=i+1
            #print('skip word')
        elif isVowel(root[j]):
            j=j+1
            #print('skip root')
        elif word[i]==root[j]:
            i=i+1
            j=j+1
            goodcon+=1
            #print('good match')
        else:
            #print('bad match')
            return False
    if goodcon<pre: return False
    else: return True

def matchcon(word,root):
    i=0
    j=0
    root+='$'
    word+='$'
    goodcon=0
    
    while(word[i]!='$' and root[j]!='$'):
        #print('match ',word[i],' <-> ',root[j])
        
        if isVowel(word[i]):
            i=i+1
            #print('skip word')
        elif isVowel(root[j]):
            j=j+1
            #print('skip root')
        elif word[i]==root[j]:
            i=i+1
            j=j+1
            goodcon+=1
            #print('good match')
        else:
            #print('bad match')
            i+=1
            j+=1

    return goodcon

    
#main program

with open("D:\Maithili-English Converter\dictionary.txt") as f: #using dictionary.txt which is a root word database to match words in order to find their english meanings
    i=1
    mydict=dict()
    for line in f:
        #print(i,'.',line)
        i+=1
        lsp=line.split()
        #print(lsp)
        key=lsp[0]
        val=lsp[1:]
        mydict[key]=val



print("Enter a Sentence in Maithili")
Sentence="नीतीश कुमार देशक किछु एहन नेता मे स छथि जिनकर लक्ष्य बुझब बड कठिन अछि"  #input sentence
#Sentence=input()
S=toRoman(Sentence)
print("Enter precision limit(1-3)") #precision selector
pre=3
pre=int(input())
multians='y' #Show multiple matches YES or NO
print("show multiple matches(y/n)?");
multians=input()
Words=S.split()
T=0
U=0
for w in Words:
    T=T+1
    print('')
    if w in mydict:
        print(w,'   ',w,'    ',mydict[w])
        continue
    found=False
    bestroot=""
    bestmatch=0
    bestval=""
    for key,val in mydict.items():
        if(match(w,key)):
            if(multians=='y'):
                print(w,'   ',key,'    ',val)
            found=True
            x=matchcon(w,key)
            if(x>=bestmatch):
                bestmatch=x
                bestroot=key
                bestval=val
    if multians!='y' and found==True:
        print(w,'   ',bestroot,'    ',bestval)
    if found==False:
        print(w,'     unknown')
        U+=1
print("precision=",pre)
print("total words=",T)
print("matched words=",T-U)
print("unmatched words=",U)
per=(T-U)*100/T
print("matching percentage=",per,'%\n\n')

leave = getch()  #calling the getch() function
        









