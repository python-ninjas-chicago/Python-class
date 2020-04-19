#from random import randint
#randint(0,9)
#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('mydb.db')
conn.execute('''select * from students;''')

print("Opened database successfully")