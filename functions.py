from bs4 import BeautifulSoup
import json
import sqlite3


def get_html(file_path):
    HtmlFile = open(file_path, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


def save_json(list):
    dict_learning_id = list[0]
    dict_learning_content = list[1]
    with open('dict_learning_id.json', 'w', encoding='UTF-8') as file:
        json.dump(dict_learning_id, file, indent=4)
    with open('dict_learning_content.json', 'w', encoding='UTF-8') as file1:
        json.dump(dict_learning_content, file1, indent=4)
    return 'Done✅'

def save_db(list):
    dict_learning_id = list[0]
    dict_learning_content = list[1]
    for title,message_id in dict_learning_id.items():
        database = sqlite3.connect('Parser.db')
        cursor = database.cursor()
        cursor.execute(f'''
            INSERT INTO Learning_id(title, message_id)
            VALUES(?,?)''', (title, message_id))
        database.commit()
        database.close()
    for reply_id,content in dict_learning_content.items():
        for i in content:
            database = sqlite3.connect('Parser.db')
            cursor = database.cursor()
            cursor.execute(f'''
                INSERT INTO Learning_content(replied_message_id, content)
                VALUES(?,?)''', (reply_id, i))
            database.commit()
            database.close()






