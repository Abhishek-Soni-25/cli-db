import os

def createDB(dbname):
    filePath = os.path.join(os.getcwd(), "database", dbname)
    if not os.path.exists(filePath):
        os.mkdir(filePath)
        print("Database created Successfully")
    else:
        print("Database already exists")

def showDBS():
    filePath = os.path.join(os.getcwd(), "database")
    fileList = os.listdir(filePath)
    if len(fileList) != 0:
        for file in fileList:
            print(file)
    else:
        print("No database exists")

def deleteDB(dbname):
    filePath = os.path.join(os.getcwd(), "database", dbname)
    if os.path.exists(filePath):
        os.rmdir(filePath)
        print("Database deleted Successfully")
    else:
        print("Database not found")

def useDB(dbname):
    filePath = os.path.join(os.getcwd(), "database", dbname)
    flag = False
    if os.path.exists(filePath):
        flag = True
        return flag
    else:
        return flag