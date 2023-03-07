import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="qr_codes"
)

mycursor = mydb.cursor()

col_ids = ((2, 3), 4, (5, 6), 7, 8, 10, 11, 12, (13, 14) , 16, 18, (19, 20), 21, 22, 24, 25, 26, (28, 29), 31, 32)

data = pd.read_excel('excel_data/student_naar_les.xlsx', usecols='N:AG')
column_id = 0
for column in data:
  gaat_naar_matrix = (data[column] == "Yes, I will participate.")
  student_id = 1
  for gaat_naar in gaat_naar_matrix:
    if gaat_naar:
      if type(col_ids[column_id]) is tuple:
        for i in col_ids[column_id]: 
          print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, {i}, {gaat_naar})')
          mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, {i}, {gaat_naar})')
      else:
        print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, {col_ids[column_id]}, {gaat_naar})')
        mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, {col_ids[column_id]}, {gaat_naar})')
      mydb.commit()
    student_id += 1
  column_id += 1
  
options1 = pd.read_excel('excel_data/student_naar_les.xlsx', usecols='Y')
options2 = pd.read_excel('excel_data/student_naar_les.xlsx', usecols='AE')

student_id = 1
for answer in options1.values:
  if answer == 'Option 1: Cancer across borders':
    print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 19, 1)')
    mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 19, 1)')
  if answer == 'Option 2: Social mobility & higher education (max. 20 participants)':
    print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 20, 1)')
    mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 20, 1)')
  mydb.commit()
  student_id+=1

student_id = 1
for answer in options2.values:
  if answer == 'Option 2: Circular entrepreneurship':
    print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 29, 1)')
    mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 29, 1)')
  if answer == 'Option 1: Wood, use it or lose it!?':
    print(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 28, 1)')
    mycursor.execute(f'insert into gaat_naar (student_id, les_id, gaat_naar) values ({student_id}, 28, 1)')
  student_id+=1
  mydb.commit()
mycursor.close()