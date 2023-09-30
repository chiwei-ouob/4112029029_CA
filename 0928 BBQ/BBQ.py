import sqlite3

conn = sqlite3.connect('BBQ.db')
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS meat(
id INTEGER PRIMARY KEY,
name TEXT,
price INTEGER,
quantity INTEGER
)''')

cursor.execute("INSERT INTO meat (id, name, price, quantity) VALUES (1, 'chicken', 30, 5)")
cursor.execute("INSERT INTO meat (id, name, price, quantity) VALUES (2, 'beaf', 55, 10)")
cursor.execute("INSERT INTO meat (id, name, price, quantity) VALUES (3, 'pork', 40, 15)")

def lookup():
    cursor.execute("SELECT * FROM meat")
    meat = cursor.fetchall()
    print ("表格內容: ")
    for ingredient in meat: 
        print (ingredient)
        
lookup()

cursor.execute("UPDATE meat SET price=35 WHERE name='pork'")
cursor.execute("UPDATE meat SET quantity=30 WHERE name='chicken'")
lookup()

cursor.execute("DELETE FROM meat WHERE price=40") #沒有資料會被刪除
lookup()

cursor.close()
conn.close()