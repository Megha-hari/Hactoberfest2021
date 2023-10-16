                         """                    PYTHON PROGRAM FOR WORD JUMPLE GAME
            Word Jumble is one of the most popular and challenging games that will test, not only your vocabulary, but also your spelling skills. 
            All you have to do is rearrange a group of letters that are in complete disorder to form the correct word, or set of words  """



import random
def choose():
    words=['water','computer','honey','sugar','coding','lemon']
    pick=random.choice(words)
    return pick
def jump(word): 
    jumpled="".join(random.sample(word,len(word)))
    return jumpled
def thank(p1name,p2name,ppt1,ppt2):
    print(p1name,'your score :',ppt1)
    print(p2name,'your score:',ppt2)
    print('thank you')
def play():
    p1name=input('enter p1 name')
    p2name=input('enter p2 name')
    ppt1=0
    ppt2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jump(picked_word)
        print(qn)
        if turn%2==0:
            print(p1name,'yout turn')
            ans=input('what on your mind')
            if ans==picked_word:
                ppt1=ppt1+1
                print('your scor:',ppt1)
            else:
                print('better luck next time')
                c=input('press 1 for continue or 0 for quit')
                if c==0:
                    thank(p1name,p2name,ppt1,ppt2)
                    break
        else:
            print(p2name,'yout turn')
            ans=input('whats on your mind')
            if ans==picked_word:
                ppt2=ppt2+1
                print('your score:',ppt2)
            else:
                print('better luck next time')
                c=input('press 1 for continue or 0 for quit')
                if c==0:
                    thank(p1name,p2name,ppt1,ppt2)
                    break
        turn=turn+1
