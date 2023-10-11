import mysql.connector


# Это функция сохранения данных из Learning Channel в базу-данных
# Attention !!! Использовать эту функцию для
def save_mysql_channel(list):
    mydb = mysql.connector.connect(
        host="192.168.1.236",
        user="timurparser",
        password="timurparser",
        database="timurparser")

    mycursor = mydb.cursor()
    dict_learning_id = list[0]
    for i, k in dict_learning_id.items():
        from_name = k[2]
        text = i
        title = k[1]
        msg_id = k[0]
        sql = "INSERT INTO hr_tg_channel_content(form_name, text, title, message_id) " \
              "VALUES (%s, %s, %s, %s)"
        val = (from_name, text, title, msg_id)
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")