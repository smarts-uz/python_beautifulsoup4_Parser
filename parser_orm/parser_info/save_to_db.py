import mysql.connector
from .models import channel_content, group_content, group_video_content


def read_channel_db():
    dict_r = list(channel_content.objects.values_list('message_id', 'text'))
    result = {}
    for i in dict_r:
        result[i[0]] = i[1]
    return result


def get_info_from_db():
    # mydb = mysql.connector.connect(
    #     host="192.168.100.100",
    #     user="timurparser",
    #     password="timurparser",
    #     database="timurparser")
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT from_name, message_id, replied_message_id FROM hr_tg_group_content WHERE joined = 0;")
    # myresult = mycursor.fetchall()
    myresult = list(group_content.objects.filter(joined=0).values_list("from_name", "message_id", "replied_message_id"))
    return myresult


def get_info_from_db_2():
    # mydb = mysql.connector.connect(
    #     host="192.168.100.100",
    #     user="timurparser",
    #     password="timurparser",
    #     database="timurparser")
    # mycursor = mydb.cursor()
    # mycursor.execute("SELECT message_id FROM hr_tg_channel_video_content WHERE from_name IS NULL;")
    # myresult = mycursor.fetchall()
    myresult = list(group_video_content.objects.filter(from_name=None).values_list("message_id"))
    return myresult


def get_info_from_db_3():
    myresult = list(group_content.objects.filter(from_name=None).values_list("message_id"))
    return myresult


def update_video_name(dict_info):
    # mydb = mysql.connector.connect(
    #     host="192.168.100.100",
    #     user="timurparser",
    #     password="timurparser",
    #     database="timurparser")
    # mycursor = mydb.cursor()
    for x, y in dict_info.items():
        # sql = "UPDATE hr_tg_channel_video_content SET from_name = %s  WHERE message_id = %s"
        # val = (y, x)
        # mycursor.execute(sql, val)
        # mydb.commit()
        group_video_content.objects.filter(message_id=x).update(from_name=y)
        print(f"Message - {x}, updated with name - {y}!")


def update_group_name(dict_id):
    for x, y in dict_id.items():
        group_content.objects.filter(message_id=x).update(from_name=y)
        print(f"Message - {x}, updated with name - {y}!")


def update_group_text():
    dict_text_id = read_channel_db()
    for x, y in dict_text_id.items():
        group_content.objects.filter(text='Null', replied_message_id=x).update(text=y)
        print(f"Message - {x}, updated with text - {y}!")


# Это функция сохранения данных из Learning Channel в базу-данных
# Attention !!! Использовать эту функцию после тщательной верификации данных
# def save_mysql_channel(list):
#     mydb = mysql.connector.connect(
#         host="192.168.100.100",
#         user="timurparser",
#         password="timurparser",
#         database="timurparser")
#     mycursor = mydb.cursor()
#     dict_learning_id = list[0]
#     for i, k in dict_learning_id.items():
#         try:
#             from_name = k[2]
#         except:
#             from_name = 'SmartTech Learning'
#         text = i
#         title = k[1]
#         msg_id = k[0]
#         sql = "INSERT INTO hr_tg_channel_content(form_name, text, title, message_id) " \
#               "VALUES (%s, %s, %s, %s)"
#         val = (from_name, text, title, msg_id)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         print(mycursor.rowcount, "record inserted.")
#
#
# def save_mysql_group(list):
#     mydb = mysql.connector.connect(
#         host="192.168.100.100",
#         user="timurparser",
#         password="timurparser",
#         database="timurparser")
#     mycursor = mydb.cursor()
#     for i in list:
#         from_name = i[0]
#         text = i[1]
#         content = i[2]
#         data_title = i[3]
#         message_details = i[4]
#         msg_id = i[5]
#         replied_message_details = i[6]
#         reply_id = i[7]
#         joined = i[8]
#         sql = """INSERT INTO hr_tg_group_content(from_name, text, content, title, message_details, message_id, replied_message_details, replied_message_id, joined)
#         VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#         val = (from_name, text, content, data_title, message_details, msg_id, replied_message_details, reply_id, joined)
#         mycursor.execute(sql, val)
#         mydb.commit()
#         print(mycursor.rowcount, "record inserted.")
#
#
# def save_mysql_video(list_v):
#     mydb = mysql.connector.connect(
#         host="192.168.100.100",
#         user="timurparser",
#         password="timurparser",
#         database="timurparser")
#     mycursor = mydb.cursor()
#     for i in list_v:
#         if i[0] != 'Null':
#             text_from_learning = i[0]
#             video_path = i[1]
#             description = i[2]
#             video_duration = i[3]
#             data_title = i[4]
#             message_details = i[5]
#             msg_id = i[6]
#             replied_message_details = i[7]
#             replied_id = i[8]
#             from_name = i[9]
#             sql = """INSERT INTO hr_tg_channel_video_content(text_from_learning, video_path, description, video_duration, data_title, message_details, message_id, replied_message_details, replied_id, from_name)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
#             val = (text_from_learning, video_path, description, video_duration, data_title, message_details, msg_id, replied_message_details, replied_id, from_name)
#             mycursor.execute(sql, val)
#             mydb.commit()
#         else:
#             pass
#         print(mycursor.rowcount, "record inserted.")


