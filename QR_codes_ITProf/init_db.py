import os
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",

)

mycursor = mydb.cursor()
""" mycursor.execute('drop database qr_codes')
mycursor.execute('create database qr_codes') """
mydb.database = 'qr_codes'

path = os.listdir('sql_scripts')

""" for file in path:
    print(f'sql_scripts/{file}')
    file_read = open(f'sql_scripts/{file}', 'r')
    mycursor.execute(file_read.read(), multi=True)
mydb.commit() """

os.system('py python_scripts/lessen_naar_db.py')
os.system('py python_scripts/persoon_naar_db.py')
os.system('py python_scripts/persoon_naar_les.py')