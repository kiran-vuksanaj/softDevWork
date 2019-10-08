#Kiran Vusksanaj
#SoftDev pd1
#skeleton :: SQLITE3 BASICS
#07 Oct 2019

# initialized from care packagej

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >


# command = "CREATE TABLE roster(name TEXT, age INTEGER, id INTEGER PRIMARY KEY)"          # test SQL stmt in sqlite3 shell, save as string
# c.execute(command)    # run SQL statement
c.execute("CREATE TABLE roster(name TEXT,age INTEGER,id INTEGER PRIMARY KEY)")
with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['name'],row['age'],row['id'])
        print("INSERT INTO roster (name,age,id) VALUES("+row['name']+","+row['age']+","+row['id']+")");
        c.execute("INSERT INTO roster (name,age,id) VALUES(\""+row['name']+"\","+row['age']+","+row['id']+")");

#==========================================================

db.commit() #save changes
db.close()  #close database
