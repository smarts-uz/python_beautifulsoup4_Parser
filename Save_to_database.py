import sqlite3

database = sqlite3.connect('Parser.db')
cursor = database.cursor()

cursor.execute(f'''
CREATE TABLE IF NOT EXISTS Learning_id(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    message_id int
);
''')

cursor.execute(f'''
CREATE TABLE IF NOT EXISTS Learning_content(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    replied_message_id int,
    content TEXT
);
''')
database.commit()
database.close()
