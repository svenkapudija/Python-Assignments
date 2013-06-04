#!/usr/bin/env python
# encoding: utf-8

import os

def importStudentsFromFile(fileName):
    students = {}
    
    with open(fileName, "r") as file:
        for line in file.readlines():
            jmbag, name = line.split(",")
            
            jmbag = jmbag.strip()
            firstNameLastName = name.strip().split()
            
            students[jmbag] = {
                "firstName": firstNameLastName[1],
                "lastName": firstNameLastName[0],
                "labs": {}
            }
            
    return students

def importLabScores(fileName, students):
    labGroupName = fileName.replace("Lab_", "").replace(".txt","").split("_")
    labName = int(labGroupName[0])
    
    with open(fileName, "r") as file:
        for line in file.readlines():
            jmbag, score = line.split(",")
            
            jmbag = jmbag.strip()
            score = score.strip()
            
            if not(jmbag in students):
                print("Warning! Student with JMBAG " + jmbag + " doesn't exist in student database. Ignoring...")
            else:
                if(labName in students[jmbag]["labs"]):
                    print("Warning! Student with JMBAG " + jmbag + " already has score "+ str(students[jmbag]["labs"][labName]) + " for 'lab " + str(labName) + "'. Overwriting with score '" + str(score) + "'.")
                
                students[jmbag]["labs"][labName] = float(score)
            
    return labName

def printScores(students, labs):
    print("{:<12s}{:<25s}".format("JMBAG", "Prezime, Ime"), end = "")
    for lab in labs:
        print("{:<10s}".format("L" + str(lab)), end = "")
    print()
    
    for studentJmbag in students.keys():
        print("{:<12s}{:<25s}".format(studentJmbag, students[studentJmbag]["lastName"] + ", " + students[studentJmbag]["firstName"]), end = "")
        for lab in labs:
            if(lab in students[studentJmbag]["labs"]):
                print("{:<10.2f}".format(students[studentJmbag]["labs"][lab]), end = "")
            else:
                print("{:<10s}".format(""), end = "")
        print()
    
if __name__ == "__main__":
    students = importStudentsFromFile("studenti.txt")
    
    labs = set({})
    files = os.listdir(".")
    for fileName in files:
        if(fileName.startswith("Lab_")):
            lab = importLabScores(fileName, students)
            labs.add(lab)
            
    printScores(students, labs)
