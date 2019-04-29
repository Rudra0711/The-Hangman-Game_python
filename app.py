import random

WORDS=[];
with open('words.txt','r') as wordsFile:
    WORDS=[name.strip() for name in wordsFile.readlines()]

random=random.randrange(1,100,1)
WORDS[random]="decision"
ques_word=["*" for letter in WORDS[random]]
wa=ques_word.count('*')

def genList(ques_word):
    for i in ques_word:
        print(i,end="")
    return ""

attempted=[]

while wa>0:
    i=0;
    ch=input(f"{genList(ques_word)}     [Wrong attempts left : {wa}]\nCharacter : ")
    if ch in attempted:
        print("You already attempted this!")
    else:
        if(WORDS[random].find(ch)!=-1):
            for name in WORDS[random]:
                if(WORDS[random][i]==ch):
                    ques_word[i]=ch
                i+=1
        else:
            wa-=1
    attempted.insert(0,ch)
    try:
        ques_word.index('*')
    except ValueError:
        print('Congo! You won the game')
        break
else:
    print('Oops!You lost.\nTry again')
