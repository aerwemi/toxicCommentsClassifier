def toxicWords(df):
    #target = 'toxic'
    #print(target)
    #print(type(target))
    labels=['toxic', 'severe_toxic', 'obscene', 'threat','insult', 'identity_hate']

    toxic=df[(df[labels[0]] == 1) | (df[labels[1]] == 1) | (df[labels[2]] == 1) | (df[labels[3]] == 1) | (df[labels[4]] == 1) | (df[labels[5]] == 1)]['comment_text'].tolist()

    toxic_words=[]
    for i in toxic:
        wordL = i.split()
        for j in wordL:
            toxic_words.append(j.lower())

    # Getting the English stop words from nltk
    import nltk
    from nltk.corpus import stopwords
    sw = stopwords.words('english')

    # Appending to words_ns all words that are in words but not in sw
    toxic_wordsSW=[]
    for word in toxic_words:
        if word not in sw:
            toxic_wordsSW.append(word)
    return(toxic_wordsSW)
