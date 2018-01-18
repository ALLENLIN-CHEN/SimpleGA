# 0.0 coding:utf-8 0.0
# 解码并计算值

import math
import csv
import string

#将二进制个体解码为十进制数
def decodechrom(pop, chrom_length):
    temp = []
    for i in range(len(pop)):
        t = 0
        for j in range(chrom_length):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp


def calobjValue(pop, chrom_length, max_value):
    temp1 = []
    obj_value = []
    data_list = [[]]
    temp1 = decodechrom(pop, chrom_length)
    csv_reader = csv.reader(open('E:/traindata/ga-gbt/result/result_50.csv'))
    for row in csv_reader:
        data_list.append(row)
    data_list.remove([])
    print data_list
    for i in range(len(pop)):
        count = 0
        j = 0
        while j < len(data_list):
            """
            if pop[i][0] == pop[i][1] == pop [i][2] == pop[i][3] == pop[i][4] == 1:
                print (pop[i])
            """
            num = pop[i][0]*string.atoi(data_list[j][3])+pop[i][1]*string.atoi(data_list[j][4])+pop[i][2]*string.atoi(data_list[j][5])+\
                  pop[i][3]*string.atoi(data_list[j][6])+pop[i][4]*string.atoi(data_list[j][7])+pop[i][5]*string.atoi(data_list[j][8])+ \
                  pop[i][6] * string.atoi(data_list[j][9])+pop[i][7]*string.atoi(data_list[j][10])+pop[i][8]*string.atoi(data_list[j][11])+ \
                  pop[i][9] * string.atoi(data_list[j][12])+pop[i][10]*string.atoi(data_list[j][13])+pop[i][11]*string.atoi(data_list[j][14])+ \
                  pop[i][12] * string.atoi(data_list[j][15])+pop[i][13]*string.atoi(data_list[j][16])+pop[i][14]*string.atoi(data_list[j][17])+ \
                  pop[i][15] * string.atoi(data_list[j][18])+pop[i][16]*string.atoi(data_list[j][19])+pop[i][17]*string.atoi(data_list[j][20])+ \
                  pop[i][18] * string.atoi(data_list[j][21])+pop[i][19]*string.atoi(data_list[j][22])
            if num >= 11:
                num = 1
            else:
                num = 0
            if num == string.atoi(data_list[j][2]) and num == 1:
                count += 1
                j += 1
            else:
                j += 1
                continue
        obj_value.append(count)
        print obj_value
    return obj_value
if __name__ == '__main__':
    pass
