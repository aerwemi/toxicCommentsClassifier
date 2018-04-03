def sentimentAnalyzer(df):

    import pandas as pd

    # Import and Initialize Sentiment Analyzer
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()

    #Place holders#
    compounds=   []
    neg_score=   []
    pos_score=   []
    neu_score=   []
    ltSums   =   []
    ltCaps   =   []
    idsS     =   []
    #

    comment_text = df['comment_text']
    ids          = df['id']
    for i in range(len(comment_text)):
                text=comment_text[i]
                compound=analyzer.polarity_scores(text)['compound']
                compounds.append(compound)

                neg=analyzer.polarity_scores(text)['neg']
                neg_score.append(neg)

                pos=analyzer.polarity_scores(text)['pos']
                pos_score.append(pos)

                neu=analyzer.polarity_scores(text)['neu']
                neu_score.append(neu)

                splitT = text.split()
                ltSum=0
                ltCap=0

                for words in splitT:
                    ltSum = ltSum + len(words)
                    ltCap = ltCap + sum(1 for l in words if l.isupper())
                ltSums.append(ltSum)
                ltCaps.append(ltCap)

                idsS.append(ids[i])

    scores={'Compound':compounds,
            'Negative':neg_score,
            'Positive':pos_score,
            'Neutral':neu_score,
            'NumL':ltSums,
            'NumC': ltCaps,
            'id'  : idsS
           }

    df_score=pd.DataFrame(scores)
    df_score['Caps'] = df_score.NumC / df_score.NumL
    df_score= df_score[['id','Compound', 'Negative', 'Positive', 'Neutral', 'NumC', 'NumL', 'Caps']]
    return(df_score.fillna(0))
