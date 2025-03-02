import os
import re
import csv
from tabulate import tabulate

def createTable(dbname, tableName, columnNames):
    filePath = os.path.join(os.getcwd(), "database", dbname, tableName)
    if not os.path.exists(filePath):
        tokenizedCommand = re.split(r"[,()]", columnNames)
        columns = list(filter(None, tokenizedCommand)) 
        f = open(filePath, 'w')
        f.write(",".join(columns))
        f.close()
        print("Table created successfully")
    else:
        print("Table already exists")

def showTables(dbname):
    filePath = os.path.join(os.getcwd(), "database", dbname)
    fileList = os.listdir(filePath)
    if len(fileList) != 0:
        for file in fileList:
            print(file)
    else:
        print("No tables exists")

def deleteTable(dbname, tableName):
    filePath = os.path.join(os.getcwd(), "database", dbname, tableName)
    if os.path.exists(filePath):
        os.remove(filePath)
        print("Table deleted Successfully")
    else:
        print("Table not found")

def getTableDescription(dbname, tableName):
    filePath = os.path.join(os.getcwd(), "database", dbname, tableName)
    if os.path.exists(filePath):
        with open(filePath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            first_row = next(reader, None) 
        print(tabulate([first_row], tablefmt="fancy_grid"))
    else:
        print("Table not found")

def getTableInfo(dbname, tableName):
    filePath = os.path.join(os.getcwd(), "database", dbname, tableName)
    if os.path.exists(filePath):
        with open(filePath, newline='') as csvfile:
            reader = csv.reader(csvfile)
            data = [row for row in reader]
        print(tabulate(data, headers="firstrow", tablefmt="fancy_grid"))
    else:
        print("Table not found")

def insertDataInTable(dbname, data, tableName):
    filePath = os.path.join(os.getcwd(), "database", dbname, tableName)
    if os.path.exists(filePath):
        tokenizedCommand = re.split(r"[,()]", data)
        values = list(filter(None, tokenizedCommand)) 
        f = open(filePath, 'a')
        f.write("\n" + ",".join(values))
        f.close()
        print("Data inserted successfully")
    else:
        print("Table not found")