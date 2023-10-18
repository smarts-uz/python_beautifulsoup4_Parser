import os
import shutil
import mysql.connector
import json
from os import listdir
from additional.functions import correct_data_title, correct_video_title, correct_post_title, correct_file_location, correct_video_duration


def read_mysql():
    mydb = mysql.connector.connect(
        host="192.168.100.100",
        user="timurparser",
        password="timurparser",
        database="timurparser")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT text_from_learning, video_path, description, video_duration, data_title FROM hr_tg_channel_video_content")
    myresult = mycursor.fetchall()
    # for i in myresult:
    #     print(i)
    return myresult[0:100]


def create_dirs(list_of_data):
    actual_path = 'D:\\108\\Test\\'  # There should be path of directory where you want to save all videos
    for item in list_of_data:
        post_title = correct_post_title(item[0])
        video_path = item[1]
        description = item[2]
        video_duration = correct_video_duration(item[3])
        data_title = correct_data_title(item[4])
        video_title = correct_video_title(video_path, post_title)
        for i in post_title:
            actual_path_dir = actual_path + i + "\\"
            if not os.path.exists(actual_path_dir):
                os.mkdir(actual_path_dir)
            file_location = correct_file_location(video_path, data_title)
            shutil.copy2(file_location, actual_path_dir + video_title)
            with open(f'{actual_path_dir}{video_duration}.txt', 'x', encoding='UTF-8') as file:
                try:
                    file.write(description)
                except:
                    file.write('There is no description')


data = read_mysql()
#create_dirs(data)


