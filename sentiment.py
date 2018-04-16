from textblob import TextBlob

def getSolution(v):
    if v==0.0:
        return 'Have a great Day! Let me know if you want to talk more'
    elif v==1.0:
        return 'You seem to be having a great day! Carry On!'
    elif v==-1.0:
        return "You seem sad! Don't Lose Hope!"
    elif v>0.0:
        return "Carry on with your awesome day!"
    elif v<0.0:
        return "Dont worry, be Happy"

def getMood(q):    
    wiki=TextBlob(q)
    y=['die','death','sad','suicide','depress','help']
    if any(y in q for y in y):
        return getSolution(-1.0)
    else:
        return getSolution(wiki.sentiment.polarity)