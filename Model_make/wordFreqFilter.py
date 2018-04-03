def wordFreqFilter(Num, freqdist):
    print('Number of words: ')
    freqdistEd={k: v for k, v in freqdist.items() if v>Num}
    wordsF = [i for i in freqdistEd.keys()] # output words Features
    print(len(wordsF))
    return(wordsF)
