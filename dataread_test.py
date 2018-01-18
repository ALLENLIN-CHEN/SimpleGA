
import csv

csv_reader = csv.reader(open('E:/traindata/result/RF_GBT_result100_1.csv'))
count = 0
for row in csv_reader:
    if row[3]==row[4]:
        count = count +1
    print (row)

print (count)







