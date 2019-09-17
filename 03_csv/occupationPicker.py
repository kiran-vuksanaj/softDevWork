
import csv
import random

# csv library makes reading the csv we have easier because there are "," in various spots and we can not simply split along the ","

with open('occupations.csv') as csv_file:
    #code by Vishwaa, edited by kiran
    read = csv.reader(csv_file, delimiter = ",")
    dict = {}
    l = 0
    for row in read:
        # print row
        if l == 0:
            # skip header row
            l = l + 1
        else:
            dict[row[0]] = float(row[1]) / 100

print dict

def randomOccupation(dict):
    randomVal = random.random()
    for key in dict:
        print key
        print dict[key]

randomOccupation(dict)
