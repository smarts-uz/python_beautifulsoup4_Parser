# import mysql.connector
#
#
# def read_mysql():
#     mydb = mysql.connector.connect(
#         host="192.168.100.100",
#         user="timurparser",
#         password="timurparser",
#         database="timurparser")
#     mycursor = mydb.cursor()
#     mycursor.execute("SELECT text_from_learning, video_path, description, video_duration, data_title, from_name FROM hr_tg_channel_video_content")
#     myresult = mycursor.fetchall()
#     # for i in myresult[100:150]:
#     #     print(i)
#     # return myresult[1:100]
#     return myresult[7784:]
#
#
# def read_mysql_all():
#     mydb = mysql.connector.connect(
#         host="192.168.100.100",
#         user="timurparser",
#         password="timurparser",
#         database="timurparser")
#     mycursor = mydb.cursor()
#     mycursor.execute("""SELECT from_name, text, content, title FROM hr_tg_group_content
# WHERE content not LIKE 'video%' and text != 'Null';""")
#     myresult = mycursor.fetchall()
#     # for i in myresult[1:100]:
#     #     print(i)
#     return myresult[59850:60000]
#
