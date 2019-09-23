import csv
with open("occupations.csv") as csvfile:
    for row in csvfile:
        for elt in row:
            print(elt)
