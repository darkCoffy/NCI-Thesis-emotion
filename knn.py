import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix


def feature_only_knn(input_dataset):
    X = input_dataset.drop('emotion_name', axis=1)
    y = input_dataset['emotion_name']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # feature scaling on train set
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # KNN
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    csv_classification = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
    csv_classification.to_csv('Metrics\\feature_only_knn.csv',  sep=',')


def feature_gender_knn(input_dataset):
    X = input_dataset.drop('emotion_name', axis=1)
    y = input_dataset['emotion_name']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # feature scaling on train set
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # KNN with
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    csv_classification = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
    csv_classification.to_csv('Metrics\\feature_gender_knn.csv', sep=',')


def feature_gender_intensity_knn(input_dataset):
    X = input_dataset.drop('emotion_name', axis=1)
    y = input_dataset['emotion_name']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

    # feature scaling on train set
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)

    # KNN with
    classifier = KNeighborsClassifier(n_neighbors=5)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    csv_classification = pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
    csv_classification.to_csv('Metrics\\feature_gender_intensity_knn.csv', sep=',')


if __name__ == '__main__':
    full_data = pd.read_csv('maxFeatures.csv')
    no_high = full_data[full_data.intensity != 1]
    feature_only_data = no_high.drop(['filename', 'value', 'gender', 'intensity'], axis=1)
    feature_gender_data = no_high.drop(['filename', 'value', 'intensity'], axis=1)
    no_low = full_data[full_data.intensity != 0]
    feature_gender_intensity_data = no_low.drop(['filename', 'value'], axis=1)
    feature_only_knn(feature_only_data)
    feature_gender_knn(feature_gender_data)
    feature_gender_intensity_knn(feature_gender_intensity_data)
