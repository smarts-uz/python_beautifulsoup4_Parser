import os
import shutil
import mysql.connector
from os import listdir
import json


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
    return myresult

def correct_post_title(post_title):
    first_step = post_title.split(' | ')
    second_step = first_step[-1].split('#')
    third_step = second_step[0]
    first_step[-1] = third_step
    first_step.reverse()
    print(first_step)
    return first_step


def correct_video_title(video_path, post_title):
    first_step = video_path.split('video_files')
    if first_step[-1].startswith('/Rec'):
        video_title = '\\' + post_title[-1] + '.mp4'
    else:
        video_title = first_step[-1]
    return video_title


def correct_data_title(data_title):
    year = data_title[6:11]
    return year


def correct_file_location(video_path, data_title):
    base_dir = r"\\" + "192.168.100.100\SmartTech Learning Group\\"
    file_directory = base_dir + data_title
    file_path_list = listdir(file_directory)
    for i in file_path_list:
        link = file_directory + '\\' + i
        video_link = link + '\\' + video_path
        if os.path.isfile(video_link):
            return video_link

def create_dirs(list_of_data):
    actual_path = 'D:\\108\\Test\\'  # There should be path of directory where you want to save all videos
    for item in list_of_data:
        post_title = correct_post_title(item[0])
        video_path = item[1]
        description = item[2]
        video_duration = item[3]
        data_title = correct_data_title(item[4])
        video_title = correct_video_title(video_path, post_title)
        for i in post_title:
            actual_path = actual_path + i + "\\"
            if not os.path.exists(actual_path):
                os.mkdir(actual_path)
        file_location = correct_file_location(video_path, data_title)
        shutil.copy2(file_location, actual_path + video_title)

data = read_mysql()
create_dirs(data)














#  correct_file_location(r'video_files\«Account» folder of Services.mp4', '2023')

#  "\\192.168.100.100\SmartTech Learning Group\2023\9-8\video_files\«Account» folder of Services.mp4"
#  \\192.168.100.100\SmartTech Learning Group\\2023\9-8\video_files\«Account» folder of Services.mp4

# my_path = listdir(r'\\192.168.100.100\SmartTech Learning Group\\2021') # \\192.168.100.100\SmartTech Learning Group\2021
# for i in my_path:
#     print(i)


# path where we will save our data
# actual_path = 'D:\\108\\Test\\'
#
#
# renamed_file = '\\Succes_2.mp4'
#
# post_title = "Uztelecom | circleci.com| CICD".split('|')  # post title divide to list
# post_title.reverse()


def folder_structure(post_title, actual_path, renamed_file):
    for i in post_title:
        actual_path = actual_path + i + "\\"
        if not os.path.exists(actual_path):
            os.mkdir(actual_path)
    file_location = fr'\\192.168.100.100\SmartTech Learning Group\2021\2021-9\video_files\flutter map + polyline.mp4'
    shutil.copy2(file_location, actual_path + renamed_file)


def name_reducer(viriable):
    limit = 10
    if len(viriable) > limit:
        x = len(viriable) - limit
        extension = (viriable[-5:])
        viriable = viriable.replace(viriable[-x:], '') + extension
        print(viriable)
        return viriable
    else:
        pass


#folder_structure(post_title, actual_path, name_reducer(renamed_file))