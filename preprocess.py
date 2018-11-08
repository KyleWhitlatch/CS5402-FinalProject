import csv

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
                    #print(temp[8] + ' ' + rows[8])
                    if '2018' not in temp[2]:
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