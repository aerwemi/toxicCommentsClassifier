def wordFreqDist(num, toxic_wordsSW):
    from nltk import FreqDist
    # Creating the word frequency distribution
    wordFreqDist = FreqDist(toxic_wordsSW)
    wordFreqDist
    # Plotting the word frequency distribution
    wordFreqDist.plot(num)
    return(wordFreqDist)
