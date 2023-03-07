import pandas as pd
import mysql.connector

namen = pd.read_excel('excel_data/data.xlsx', usecols=['ID', 'First name', 'Surname'])

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="qr_codes"
)

mycursor = mydb.cursor()

for entry in namen.values:
    print(f"insert into student (id, first_name, last_name) values ({entry[0]}, '{entry[1]}', '{entry[2]}')")
    mycursor.execute(f'insert into student (id, first_name, last_name) values ("{entry[0]}", "{entry[1]}", "{entry[2]}")')
    mydb.commit()

mycursor.close()
