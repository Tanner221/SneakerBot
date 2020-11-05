import sqlite3

conn = sqlite3.connect('user_info.db')

print ("Opened database successfully")

conn.execute('''CREATE TABLE USER_INFO
         (ID INT PRIMARY KEY     NOT NULL,
         USERNAME     TEXT     NOT NULL,
         PASSWORD     TEXT     NOT NULL);''')

conn.commit()

conn.close()