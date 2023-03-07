import pandas as pd
import mysql.connector

lectures = pd.read_excel('excel_data/lessen.xlsx', usecols='A, B, C, D, J', skiprows=[0, 1, 2, 3, 8, 13, 23, 24, 25, 26, 27, 28, 35, 41, 42, 43, 44, 45, 46])

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="qr_codes"
)

mycursor = mydb.cursor()

id = 0

for entry in lectures.values:
    print(entry)
    print(f'insert into les (les_id, naam, tijdslot, spreker, locatie, dag) values ("{id}", "{entry[1]}", "{entry[0]}", "{entry[2]}", "{entry[3]}", "{entry[4]}")')
    mycursor.execute(f'insert into les (les_id, naam, tijdslot, spreker, locatie, dag) values ("{id}", "{entry[1]}", "{entry[0]}", "{entry[2]}", "{entry[3]}", "{entry[4]}")')
    mydb.commit()
    id += 1

mycursor.close()