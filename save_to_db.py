import mysql.connector


# Это функция сохранения данных из Learning Channel в базу-данных
# Attention !!! Использовать эту функцию после тщательной верификации данных
def save_mysql_channel(list):
    mydb = mysql.connector.connect(
        host="192.168.1.236",
        user="timurparser",
        password="timurparser",
        database="timurparser")

    mycursor = mydb.cursor()
    dict_learning_id = list[0]
    for i, k in dict_learning_id.items():
        try:
            from_name = k[2]
        except:
            from_name = 'SmartTech Learning'
        text = i
        title = k[1]
        msg_id = k[0]
        sql = "INSERT INTO hr_tg_channel_content(form_name, text, title, message_id) " \
              "VALUES (%s, %s, %s, %s)"
        val = (from_name, text, title, msg_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")


def save_mysql_group(list):
    mydb = mysql.connector.connect(
        host="localhost",
        user="sherlock",
        password="23082004",
        database="home_sql")
    mycursor = mydb.cursor()
    for i in list:
        from_name = i[0]
        text = i[1]
        content = i[2]
        data_title = i[3]
        message_details = i[4]
        msg_id = i[5]
        replied_message_details = i[6]
        reply_id = i[7]
        joined = i[8]
        sql = """INSERT INTO learning_group(from_name, text, content, data_title, message_details, message_id, replied_message_details, reply_id, joined) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (from_name, text, content, data_title, message_details, msg_id, replied_message_details, reply_id, joined)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")




# def creating_mysql_group():
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="sherlock",
#         password="23082004",
#         database="home_sql")
#     mycursor = mydb.cursor()
#     mycursor.execute("""CREATE TABLE learning_group(id int NOT NULL AUTO_INCREMENT, from_name VARCHAR(255), text VARCHAR(255), content TEXT, data_title VARCHAR(255),
#     message_details VARCHAR(255), message_id INT, replied_message_details VARCHAR(255), reply_id INT, joined BOOLEAN, PRIMARY KEY (id))""")
# creating_mysql_group()

