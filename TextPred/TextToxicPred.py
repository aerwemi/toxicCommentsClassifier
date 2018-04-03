text=input(print("Text:"))

import pandas as pd
from keras.models import Sequential
from keras.utils import to_categorical
from keras.layers import Dense

labels = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
from sentimentAnalyzer3 import sentimentAnalyzer
dFCom1=pd.DataFrame([text]).reset_index()
dFCom1.columns = ['id','comment_text']
dFCom1 = sentimentAnalyzer(dFCom1)[['Compound', 'Caps', 'Negative', 'Neutral']]


wordsF2 = pd.read_csv('wordsF.csv')['0'].tolist()



from toxic_funcs import Cleaner
dfComm = pd.DataFrame([Cleaner(text)])
dfComm.columns = ['comment_text']


from makeToxicFeatures2 import makeToxicFeatures
dfComm=makeToxicFeatures(dfComm, wordsF2)
dfComm.head()


X_Text = dFCom1.join(pd.DataFrame(dfComm))
X_Text.head()


# Load the model
from keras.models import load_model
Toxic_model = load_model("toxic_model_trained.h5")

text_Pred = Toxic_model.predict(X_Text)
text_Pred

TPred = (pd.DataFrame(text_Pred) > .49999) * 1
TPred.columns = labels
print(TPred)
