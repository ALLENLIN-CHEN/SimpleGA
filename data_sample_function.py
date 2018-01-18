import random
import csv

def loadDataSet(filename):
    dataMat = [[]]
    csv_reader = csv.reader(open(filename))
    for row in csv_reader:
        dataMat.append(row)
    dataMat.remove([])
    return dataMat

def repretition_random_sampling(dataMat, num):
    samples = random.sample(dataMat, num)
    return samples