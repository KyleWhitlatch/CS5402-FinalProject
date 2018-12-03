import csv
from sklearn import tree
import pandas as pd
import numpy as np

files = ['January2018.csv','February2018.csv','March2018.csv','April2018.csv','May2018.csv','June2018.csv',
         'July2018.csv','August2018.csv','September2018.csv', 'October2018.csv']
data = []
linesread = 0
colsToDelete = [3,4,5,6,7,11,12,13,14,15,16,17]
for file in files:
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            linesread += 1
            checkFlag = False
            temp = row
            #column6
            if data == []:
                temp = np.delete(temp,colsToDelete).tolist()
                data.append(temp)
            else:
                for rows in data:
                    #print (len(temp))
                    #print(temp[8] + ' ' + rows[8])
                    if '2018' not in temp[2]:
                        checkFlag = True
                    elif (temp[18] == "0" and temp[19] == "0"):
                        checkFlag = True
                    if checkFlag:
                        break
                if checkFlag:
                    pass
                else:
                    temp = np.delete(temp,colsToDelete).tolist()
                    #print(temp)
                    data.append(temp)
with open('aggregated_data.csv',mode= 'w',newline='') as outfile:
    writer = csv.writer(outfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
#print(linesread)
#print(data)

#The Lines below can be put into a different python script so that we aren't preprocessing data everytime
#need to split the data into the target(prediction) feature and the rest
#data = pd.read_csv('aggregated_data.csv')
#print (data.head())
#clf = tree.DecisionTreeClassifier()
