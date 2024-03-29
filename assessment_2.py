# -*- coding: utf-8 -*-
"""Assessment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HRPjQFs_vqPkfzsBOVTtwQ7wkudFA1Gj
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LogisticRegression

df = pd.read_excel("/content/Data set.xlsx",1)

df = df.dropna()

df.shape

X = df.iloc[:,1:6]
Y = df.iloc[:,6]

classifier = LogisticRegression()
classifier.fit(X,Y)

y_pred = classifier.predict(X)
y_pred

y_pred_df= pd.DataFrame({'actual': Y, 'predicted_prob': y_pred})
y_pred_df

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(Y,y_pred)
print (confusion_matrix)

N = 381+197+123+395
TP = 381
FP = 197
FN = 123
TN = 395

Accuracy = ((TP+TN)/N)*100
Accuracy

Error_rate = ((FP+FN)/N)*100
Error_rate

Sensitivity = (TP/(TP+FN))*100
Sensitivity

Specificity = (TN/(TN+FP))*100
Specificity

FNR = (FN/(FN+TP))*100
FNR

FPR = (FP/(TN+FP))*100
FPR

from sklearn.metrics import classification_report
print(classification_report(Y,y_pred))

from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score

FPR, TPR, thresholds = roc_curve(Y, classifier.predict_proba (X)[:,1])

auc = roc_auc_score(Y, y_pred)

import matplotlib.pyplot as plt
plt.plot(FPR, TPR, color='red', label='logit model ( area  = %0.2f)'%auc)
plt.plot([0, 1], [0, 1], 'k--')
plt.xlabel('False Positive Rate or [1 - True Negative Rate]')
plt.ylabel('True Positive Rate')