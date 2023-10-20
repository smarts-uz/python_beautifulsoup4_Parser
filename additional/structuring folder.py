import os
import shutil
import mysql.connector
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
    # for i in myresult[100:150]:
    #     print(i)
    # return myresult[1:100]
    return myresult[1:100]


def create_dirs(list_of_data):
    for item in list_of_data:
        post_title = correct_post_title(item[0])
        video_path = item[1]
        description = item[2]
        video_duration = item[3]
        data_title = correct_data_title(item[4])
        video_title = correct_video_title(video_path, post_title)
        if len(post_title) == 1:
            actual_path = 'D:\\108\\Test\\'  # There should be path of directory where you want to save all videos
            for i in post_title:
                actual_path_dir = actual_path + i + "\\"
                if not os.path.exists(actual_path_dir):
                    os.mkdir(actual_path_dir)
                file_location = correct_file_location(video_path, data_title)
                shutil.copy2(file_location, actual_path_dir + video_title)
                try:
                    with open(f'{actual_path_dir}{video_title}.txt', 'x', encoding='UTF-8') as file:
                        try:
                            file.write(f'''Description: {description}
Video_duration: {video_duration}''')
                        except:
                            file.write(f'''Description: None
Video_duration: {video_duration}''')
                except:
                    pass
                print(actual_path_dir + '== Succes_1!')
        else:
            actual_path = 'D:\\108\\Test\\'  # There should be path of directory where you want to save all videos
            file_location = correct_file_location(video_path, data_title)
            for i in post_title:
                actual_path = actual_path + i + "\\"
                if not os.path.exists(actual_path):
                    os.mkdir(actual_path)
            shutil.copy2(file_location, actual_path + video_title)
            try:
                with open(f'{actual_path}{video_title}.txt', 'x', encoding='UTF-8') as file:
                    try:
                        file.write(f'''Description: {description}
Video_duration: {video_duration}''')

                    except:
                        file.write(f'''Description: None
Video_duration: {video_duration}''')
            except:
                pass
            print(actual_path + '== Succes_2!')


data = read_mysql()
create_dirs(data)


