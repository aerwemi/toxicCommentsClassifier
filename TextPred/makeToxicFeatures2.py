def makeToxicFeatures(df, wordsF):

    import numpy as np
    import pandas as pd

    data = df['comment_text'].tolist()


    dataWL=[]
    for i in data:
        words=i.split()
        dataWL.append(words)


    # Getting the English stop words from nltk
    import nltk
    from nltk.corpus import stopwords
    sw = stopwords.words('english')

    # Appending to words_ns all words that are in words but not in sw
    dataWlSw=[]
    for item in dataWL:
        SW=[]
        for word in item:
            if word not in sw:
                SW.append(word)
        dataWlSw.append(SW)



    toxicL=[]
    for item in dataWlSw:
        word_counts=[]
        word_count=[]
        for i in item:
            for j in range(len(wordsF)): # Words featueres
                count=0
                if i == wordsF[j]:
                    count=count+1
                word_count.append(count)
            word_counts.append(word_count)
            word_count=[]
            
        toxicL.append(np.sum(word_counts, axis=0))



    LD={}
    count=0
    for i in range(len(toxicL)):
        LD[count]=toxicL[i].tolist()
        count=count+1

    return(pd.DataFrame(LD).T)
