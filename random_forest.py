from sklearn.ensemble import RandomForestClassifier
#from sklearn.datasets import make_classification
import pandas as pd
#from sklearn.model_selection import train_test_split


dataset = pd.read_csv("D:\\TEC\\ML\\pr.csv",index_col=None)
x = dataset.iloc[:,:1].values
y = dataset.iloc[:,1].values
clf = RandomForestClassifier(n_estimators=100)
x_train,y_train = clf.fit(x,y)
dataset = pd.read_csv("D:\\TEC\\ML\\pr.csv",index_col=None)
x_test = dataset.iloc[:,:1].values
#y_test = dataset.iloc[:,1].values
y_test = clf.predict(x_test)
