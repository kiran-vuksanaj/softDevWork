# Kiran Vuksanaj & Amanda Chen: Colorful Cats
# SoftDev1 pd1
# K18 -- Average
# 2019-10-15

import sqlite3

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE) # connect to the database
c = db.cursor() # like a sqlite3 shell!


# (following official python documentation usage)
# executing a SELECT returns an iterable thing! with each result!

command = 'SELECT name, students.id, mark FROM students, courses WHERE students.id = courses.id'
averages = {} # key: id, value: grades list
for row in c.execute(command):
    # print(row)
    if row[1] in averages:
        averages[ row[1] ] += [ row[2] ]
    else:
        averages[ row[1] ] = [ row[2] ] #add grade to the dict output

command = 'CREATE TABLE stu_avg(id INTEGER PRIMARY KEY, average REAL )'
c.execute(command)

for id in averages:
    average = float(sum(averages[id])) / len(averages[id])
    command = 'INSERT INTO stu_avg values(?, ?)'
    c.execute(command,[id,average])

db.commit()
db.close()
