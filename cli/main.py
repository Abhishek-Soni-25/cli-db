from tokens import convertCommandToTokens
from db import *
from table import *

print("-----Welcome-----")

command = " "
while command != "exit":
    command = input("\033[1mcli-db> \033[0m")
    tokenizedCommand = convertCommandToTokens(command)
    
    # CREATE DATABASE <DBNAME>
    if tokenizedCommand[0] == "create":
        if tokenizedCommand[1] == "database":
            createDB(tokenizedCommand[2])
        else:
            print("Invalid command")

    # SHOW DATABASES
    elif tokenizedCommand[0] == "show":
        if tokenizedCommand[1] == "databases":
            showDBS()
        else:
            print("Invalid command")

    # DELETE <DBNAME>
    elif tokenizedCommand[0] == "delete":
        deleteDB(tokenizedCommand[1])

    # USE <DBNAME>
    elif tokenizedCommand[0] == "use":
        flag = useDB(tokenizedCommand[1])
        if flag:
            innerCommand = " "
            while innerCommand != "exit":
                innerCommand = input("\033[1mcli-db> \033[0m")
                innerTokenizedCommand = convertCommandToTokens(innerCommand)
                
                # SHOW TABLES
                if innerTokenizedCommand[0] == "show":
                    if innerTokenizedCommand[1] == "tables":
                        showTables(tokenizedCommand[1])
                    else:
                        print("Invalid command")

                # DELETE <TABLENAME>
                elif innerTokenizedCommand[0] == "delete":
                    deleteTable(tokenizedCommand[1], innerTokenizedCommand[1])

                # VIEW DESC/INFO <TABLENAME>
                elif innerTokenizedCommand[0] == "view":

                    # VIEW DESC <TABLENAME>
                    if innerTokenizedCommand[1] == "desc":
                        getTableDescription(tokenizedCommand[1], innerTokenizedCommand[2])
                    
                    # VIEW INFO <TABLENAME>
                    if innerTokenizedCommand[1] == "info":
                        getTableInfo(tokenizedCommand[1], innerTokenizedCommand[2])

                # CREATE TABLENAME (COLUMN1,COLUMN2,...)
                elif innerTokenizedCommand[0] == "create":
                    createTable(tokenizedCommand[1], innerTokenizedCommand[1], innerTokenizedCommand[2])

                # INSERT (DATA1,DATA2,..) TABLENAME
                elif innerTokenizedCommand[0] == "insert":
                    insertDataInTable(tokenizedCommand[1], innerTokenizedCommand[1], innerTokenizedCommand[2])

                elif not innerTokenizedCommand[0] == "exit":
                    print("Invalid Command")

        else:
            print("Database not found")

    elif not tokenizedCommand[0] == "exit":
        print("Invalid Command")
