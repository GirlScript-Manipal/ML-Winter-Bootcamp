#modules
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
from matplotlib import cm

df=pd.read_csv("LogReg_Cancer.csv")

#making dummy variables
df.diagnosis = [0 if each == 'M' else 1 for each in df.diagnosis]
df=df.drop(['id'], axis = 1)
df=df.drop(['Unnamed: 32'], axis = 1)

#identifying which features are important
sns.set(style="ticks", color_codes=True)
visual= sns.pairplot(df, palette = ('b', 'r'), hue="diagnosis", height=2.5)
plt.show()

#function to see what features are important
def features_matrix(df):
    fig = plt.figure()
    fig.set_size_inches(18.5, 10.5)
    ax1 = fig.add_subplot(111)
    cmap = cm.get_cmap('jet', 100)
    cax = ax1.imshow(df.corr().abs(), interpolation="nearest", cmap=cmap)
    ax1.grid(True)
    plt.title('Correlation Matrix of the WBCD features',fontsize=20)
    labels=list(df.columns)
    
    ax1.set_xticks(np.arange(len(labels)))
    ax1.set_yticks(np.arange(len(labels)))
    
    ax1.set_xticklabels(labels,fontsize=15,\
              horizontalalignment="left", rotation='vertical')
    
    ax1.set_yticklabels(labels,fontsize=15)
    fig.colorbar(cax, ticks=[-1.0, -0.8, -0.6, -0.4, -0.2, 0, \
                             0.2, 0.4, 0.6, 0.8, 1])
    plt.show()

#function call
df_features=df.drop(df.columns[-1],axis=1)
features_matrix(df_features)

#to drop the feautres that are not important
corr_matrix = df_features.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool))
to_drop = [column for column in upper.columns if any(upper[column] > 0.9)]
final= df_features.drop(df_features[to_drop], axis=1)
#replotting  containing only important features
features_matrix(final)

#logistic regression code
X=final.drop('diagnosis', axis='columns')
y=final.diagnosis

#splitting train set and test set
x_train,x_test,y_train,y_test=train_test_split(X,y)
reg = linear_model.LogisticRegression(max_iter=2500)
reg.fit(X,y)

#prediciton and accuracy
y_pred = reg.predict(x_test)
accuracy_score(y_test,y_pred)
confusion_matrix(y_pred, y_test)


