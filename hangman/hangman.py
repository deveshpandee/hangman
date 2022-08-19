import os
import hangmanInternal as h


h.lifeList=[h.h0,h.h1,h.h2,h.h3,h.h4,h.h5]

def play():
    word=h.pick()
    list2=["_" for i in range(0,len(word))]
    life=0
    while life<5:
        print(h.lifeList[life],"\n")
        print(" ".join(list2))
        print("\nGuess a letter: ")
        let=input()
        let=let.lower()
        flag=False
        for i in range(0,len(word)):
            if word[i]==let:
                list2[i]=let
                flag=True
        if flag==False:
            life+=1
            print(let," is not in this word. You lost a life")
        count=1
        if "_" not in list2:
            count=0
            break

    if count==0:
        print(" ")
        print(word.upper())
        print("YES, You got it right\n")
    else:
        print("\nSorry, You could not get it")
        print(f"Right answer would be: ",word.upper(),"\n")


play()