import pandas as pd
from sklearn import tree
from sklearn import svm
import numpy as np

in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
out_data = full_data['Survived']
data = full_data.drop(['Survived', 'PassengerId', 'Name', 'Ticket', 'Fare', 'Cabin', 'Embarked'], axis=1)
data.loc[data.loc[:, "Sex"] == 'male'] = 0
data.loc[data.loc[:, "Sex"] == 'female'] = 1
# print(data.head())
# clf = tree.DecisionTreeClassifier(max_depth=3)
# clf.fit(data, out_data)
# pred = clf.predict(data)
# clf = svm.SVC()
# clf.fit(data, out_data)
# pred = clf.predict(data)
pred = np.zeros(891)
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, out_data)
print(acc)
