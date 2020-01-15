# -*- coding: UTF-8 -*-

import os

import pandas as pd
from sklearn import tree
from sklearn.feature_extraction import DictVectorizer

dirname = os.path.abspath(os.path.dirname(__file__))
train_csv = os.path.join(dirname, 'train.csv')
test_csv = os.path.join(dirname, 'test.csv')
train_df = pd.read_csv(train_csv)
test_df = pd.read_csv(test_csv)
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
train_df['Fare'].fillna(train_df['Fare'].mean(), inplace=True)
train_df['Embarked'].fillna('S', inplace=True)
test_df['Age'].fillna(test_df['Age'].mean(), inplace=True)
test_df['Fare'].fillna(test_df['Fare'].mean(), inplace=True)
test_df['Embarked'].fillna('S', inplace=True)
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
train_features = train_df[features]
train_labels = train_df['Survived']
test_features = test_df[features]
dvec = DictVectorizer(sparse=False)
train_features = dvec.fit_transform(train_features.to_dict(orient='record'))
test_features = dvec.transform(test_features.to_dict(orient='record'))
print(dvec.feature_names_)
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(train_features, train_labels)
score = clf.score(train_features, train_labels)
print(score)
clf_predict = clf.predict(test_features)
print(clf_predict)
print(len(clf_predict))
