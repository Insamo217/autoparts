import psycopg2
import csv

'''
    Добавление категорий через copy_from
'''

conn = psycopg2.connect\
    (dbname='spares_2021', user='insamo', password='217', host='localhost')
cursor = conn.cursor()
with open('spares.csv', 'r') as f:
    next(f)
    cursor.copy_from(f, 'spares_category', sep=',')
conn.commit()

'''
    Добавление запчастай через csv.reader
'''

conn = psycopg2.connect\
    (dbname='spares_2021', user='insamo', password='217', host='localhost')
cursor = conn.cursor()
with open('spares_name_original.csv', 'r') as f:
    reader = csv.reader(f)
    next(f)
    for row in reader:
        cursor.execute("INSERT INTO spares_spares VALUES (%s, %s, %s, %s, %s, %s, %s)", row
        )
        conn.commit()
    conn.commit()

