from __future__ import division
import csv
import string

csv_reader = csv.reader(open('E:/traindata/ga-gbt/result/result_50.csv'))
count =0
count_p =0
count_s =0
for row in csv_reader:
    flag = 0
    if(string.atoi(row[2]) == 1):
        count = count +1
    num = string.atoi(row[5])+string.atoi(row[6])+string.atoi(row[7])+string.atoi(row[8])+string.atoi(row[9])+string.atoi(row[10])+string.atoi(row[13])+string.atoi(row[14])+\
          string.atoi(row[15])+string.atoi(row[18])+string.atoi(row[20])+string.atoi(row[21])+string.atoi(row[22])
    if(num >=11):
        flag =1
        count_p = count_p+1
        if flag == string.atoi(row[2]):
            count_s = count_s +1

print count
print count_p
print count_s
a = count_s/count
print (a)
print (count_s/count_p)


