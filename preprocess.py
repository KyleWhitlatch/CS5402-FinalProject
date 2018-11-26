import csv
from sklearn import tree
import pandas as pd

files = ['September2018.csv', 'October2018.csv']
data = []
linesread = 0
for file in files:
    with open(file) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            linesread += 1
            checkFlag = False
            temp = row
            #column6
            if data == []:
                data.append(temp)
            else:
                for rows in data:
                    #3,4,5,6,7,14,15
                    del temp[3]
                    del temp[4]
                    del temp[5]
                    del temp[6]
                    del temp[7]
                    del temp[14]
                    del temp[15]
                    #print(temp[8] + ' ' + rows[8])
                    if '2018' not in temp[2]:
                        checkFlag = True
                    elif (temp[18] == "0" and temp[19] == "0")
                        checkFlag = True
                    if checkFlag:
                        break
                if checkFlag:
                    pass
                else:
                    data.append(temp)
with open('aggregated_data.csv',mode= 'w') as outfile:
    writer = csv.writer(outfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)
#print(linesread)
#print(data)

#need to split the data into the target(prediction) feature and the rest
#data = pd.read_csv('aggregated_data.csv')
#clf = tree.DecisionTreeClassifier()
