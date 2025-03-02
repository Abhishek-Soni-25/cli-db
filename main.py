import os

database = os.path.join(os.getcwd(), 'database')
if not os.path.exists(database):
    os.mkdir(database)
