from id3 import Id3Estimator, export_text
import numpy as np
import preprocess, csv

X = []
Y = []
feature_names = []

with open('aggregated_data.csv',mode='r') as infile:
    print('opened el file correcto')
    csvfile = csv.reader(infile,delimiter=',')
    row = 0
    for row in csvfile:
        if row == 0:
            feature_names = [row[0],row[1],row[2],row[4],row[6],row[7]]
        else:
            X.append([row[0],row[1],row[2],row[4],row[6],row[7]])
            Y.append(row[3])

X = np.array(X)
Y = np.array(Y)
clf = Id3Estimator()
clf.fit(X,Y, check_input=True)
print(export_text(clf.tree_,feature_names))