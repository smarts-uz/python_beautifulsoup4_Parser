import os
import shutil
from additional.functions import correct_data_title, correct_video_title, correct_post_title, correct_file_location, correct_url_name
from connect_db import read_mysql, read_mysql_all


def create_dirs_all(list_of_data):
    for item in list_of_data:
        from_name = item[0]
        text = correct_post_title(item[1])
        content = item[2]
        title = correct_data_title(item[3])
        if len(text) == 1:
            actual_path = 'D:\\108\\Test\\'
            if content.startswith('files') or content.startswith('photos'):
                for i in text:
                    actual_path_dir = actual_path + i + "\\"
                    if not os.path.exists(actual_path_dir):
                        os.mkdir(actual_path_dir)
                    file_location = correct_file_location(content, title)
                    shutil.copy2(file_location, actual_path_dir)
                    try:
                        with open(f'{actual_path_dir}{from_name}.txt', 'x', encoding='UTF-8') as file:
                            file.write(f'From_name: {from_name}')
                    except:
                        pass
                    print(actual_path + content + '___Succes_2!')
            elif content.startswith('https'):
                for i in text:
                    actual_path_dir = actual_path + i + "\\"
                    if not os.path.exists(actual_path_dir):
                        os.mkdir(actual_path_dir)
                    try:
                        with open(f'{actual_path_dir}{correct_url_name(content)}.url', 'x', encoding='UTF-8') as file:
                            file.write("""
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL="""+content+"""
IconIndex=13
HotKey=0
IconFile=C:\Windows\System32\SHELL32.dll
""")
                    except:
                        pass
        else:
            if content.startswith('files') or content.startswith('photos'):
                actual_path = 'D:\\108\\Test\\'
                file_location = correct_file_location(content, title)
                for i in text:
                    actual_path = actual_path + i + "\\"
                    if not os.path.exists(actual_path):
                        os.mkdir(actual_path)

                try:
                    shutil.copy2(file_location, actual_path)
                    with open(f'{actual_path}{from_name}.txt', 'x', encoding='UTF-8') as file:
                        file.write(f'From_name: {from_name}')
                except:
                    pass
                print(actual_path + content + '___Succes_2!')
            elif content.startswith('https'):
                actual_path = 'D:\\108\\Test\\'
                for i in text:
                    actual_path = actual_path + i + "\\"
                    if not os.path.exists(actual_path):
                        os.mkdir(actual_path)
                try:
                    with open(f'{actual_path}{correct_url_name(content)}.url', 'x', encoding='UTF-8') as file:
                        file.write("""
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=""" + content + """
IconIndex=13
HotKey=0
IconFile=C:\Windows\System32\SHELL32.dll""")
                except:
                    pass


def create_dirs_video(list_of_data):
    for item in list_of_data:
        post_title = correct_post_title(item[0])
        video_path = item[1]
        description = item[2]
        video_duration = item[3]
        data_title = correct_data_title(item[4])
        from_name = item[5]
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
Video_duration: {video_duration}
From_name: {from_name}''')
                        except:
                            file.write(f'''Description: None
Video_duration: {video_duration}
From_name: {from_name}''')
                except:
                    pass
                print(actual_path_dir + '___Succes_1!')
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
Video_duration: {video_duration}
From_name: {from_name}''')
                    except:
                        file.write(f'''Description: None
Video_duration: {video_duration}
From_name: {from_name}''')
            except:
                pass
            print(actual_path + '___Succes_2!')


create_dirs_all(read_mysql_all())
data = read_mysql()
create_dirs_video(data)


