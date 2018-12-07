import csv
#from sklearn import tree
import pandas as pd
import numpy as np

files = ['January2018.csv', 'February2018.csv', 'March2018.csv', 'April2018.csv', 'May2018.csv', 'June2018.csv', 'July2018.csv', 'August2018.csv', 'September2018.csv']
#files = ['October2018.csv']
data = []
linesread = 0
colsToDelete = [3,4,5,6,7,10,11,12,13,14,15,16,17]
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
                    if temp[1][-2:] != temp[2].split('/')[0]:
                        checkFlag = True    
                    elif '2018' not in temp[2]:
                        checkFlag = True
                    elif (temp[18] == "0" and temp[19] == "0"):
                        checkFlag = True
                    if (sum(c.isdigit() for c in (temp[8])) >= 6):
                        checkFlag = True
                    elif (sum(c.isdigit() for c in (temp[8])) < 6):
                        if(temp[8] != "1" and temp[8] != "2" and temp[8] != "3" and temp[8] != "4" and temp[8] != "5" and temp[8] != "6" and temp[8] != "7" and temp[8] != "8" and temp[8] != "9"):
                            #print (temp[8])
                            temp[8] = temp[8][1]
                        #print (temp[8])
                        #print (temp[8][1])
                        #temp[8] = temp[8][1]
                    #print temp[8]
                    if checkFlag:
                        break
                if checkFlag:
                    pass
                else:
                    temp = np.delete(temp,colsToDelete).tolist()
                    #print (temp[8])
                    #temp[8] = temp[8][0]
                    #print(temp)
                    data.append(temp)
with open('aggregated_data.csv',mode= 'w') as outfile:
    writer = csv.writer(outfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for row in data:
        writer.writerow(row)


#print(linesread)
#print(data)

#The Lines below can be put into a different python script so that we aren't preprocessing data everytime
#need to split the data into the target(prediction) feature and the rest

data = pd.read_csv('aggregated_data.csv')
data = data.drop_duplicates(subset ="Complaint", keep = 'first')
datasplit = data['DateOccur'].apply(lambda x: pd.Series(str(x).split('/')))
datasplit.columns = ['Month', 'Day', 'Time']
del data['DateOccur']
data['Day'] = datasplit['Day']
data['Time'] = datasplit['Time']
data['Time'] = data['Time'].map(lambda x: x.lstrip('2018'))
data['Time'] = data.Time.apply(lambda x: x.replace(':',''))

data['Time'] = pd.to_numeric(data['Time'])


data['Time'] = np.where(data['Time'].between(0,599), 3, data['Time'])
data['Time'] = np.where(data['Time'].between(600,1159), 1, data['Time'])
data['Time'] = np.where(data['Time'].between(1200,1800), 2, data['Time'])
data['Time'] = np.where(data['Time'].between(1800,2400), 3, data['Time'])





data.to_csv('aggregated_data.csv', sep=',', index=False)


#print (data.head())
#clf = tree.DecisionTreeClassifier()
