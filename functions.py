from bs4 import BeautifulSoup
import json
from save_to_db import get_info_from_db, get_info_from_db_2, update_db


# Здесь происходит первый парсинг через библиотеку BeautifulSoup
def get_html(file_path):
    HtmlFile = open(file_path, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup


# Здесь сохраняются данные в формате json для дальнейшей обработки
def save_json(list):
    dict_learning_id = list[0]
    dict_learning_content = list[1]
    dict_all_content = list[2]
    dict_learning_id_2 = list[3]
    with open('dict_learning_id.json', 'w', encoding='UTF-8') as file:
        json.dump(dict_learning_id, file, indent=4)
    with open('dict_learning_content.json', 'w', encoding='UTF-8') as file1:
        json.dump(dict_learning_content, file1, indent=4)
    with open('dict_all_content.json', 'w', encoding='UTF-8') as file2:
        json.dump(dict_all_content, file2, indent=4)
    with open('dict_learning_id_2.json', 'w', encoding='UTF-8') as file3:
        json.dump(dict_learning_id_2, file3, indent=4)
    return 'Done✅'


# def save_test(all):
#     with open('dict_learning_id_all.json', 'a', encoding='UTF-8') as f:
#         json.dump(all, f, indent=4)


def read_json():
    with open('dict_learning_id_all.json', 'r', encoding='UTF-8') as file:
        dict_r = json.loads(file.read())
        return dict_r


# Здесь происходит первичная обработка и корректировка данных из Learning Group
def prepare_group_info(list):
    dict_learning_id = list[0]
    dict_all_content = list[2]
    test = []
    for x, y in dict_all_content.items():
        try:
            reply_id = int(y[5])
            text = get_text(dict_learning_id, reply_id)
            content = y[4]
            title = y[1]
            message_details = y[2]
            msg_id = x
            replied_message_details = y[0]
            joined = y[3]
            try:
                from_name = y[6]
            except:
                from_name = None
            test.append([from_name, text, content, title, message_details, msg_id, replied_message_details, reply_id, joined])
        except:
            pass
    return test


# Здесь также происходит обработка данных, а точнее получения заголовка к replied message
def get_text(list1, reply_id):
    id_dict = {}
    if type(list1) == list:
        for prepared_dict in list1:
            for x, y in prepared_dict.items():
                id_dict[y[0]] = x
    else:
        for x, y in list1.items():
            id_dict[y[0]] = x
    try:
        text = id_dict[reply_id]
    except:
        text = 'Null'
    return text


# Функция возвращает словарь с replied_id и from_name, что также необходимо для конечной обработки данных
def get_from_name_joined(list2):
    dict_learning_content = list2[1]
    dict_reply_id_name = {}
    for x, y in dict_learning_content.items():
        try:
            dict_reply_id_name[int(x)] = y[1]
        except:
            from_name = None
            dict_reply_id_name[int(x)] = from_name
    return dict_reply_id_name


# Данная функция возвращает конечные данные, готовые для отправки в бд
def get_from_name(list_info, dict_reply):
    result = list_info
    for i in list_info:
        if i[0] is None:
            for x, y in dict_reply.items():
                if i[-2] == x:
                    i[0] = y
                else:
                    pass
    return result


def prepare_video_info(dict_v, list_r):
    dict_learning_id = list_r[0]
    dict_learning_id_all = read_json()
    result = []
    for x, y in dict_v.items():
        msg_id = x
        description = y[1]
        video_path = y[2]
        video_duration = y[3]
        data_title = y[4]
        message_details = y[5]
        replied_message_details = y[6]
        replied_id = y[0]
        text_from_learning = get_text(dict_learning_id_all, replied_id)
        try:
            from_name = y[7]
        except:
            from_name = None
        result.append([text_from_learning, video_path, description, video_duration, data_title,
                      message_details, msg_id, replied_message_details, replied_id, from_name])
    return result


def prepare_name_info(dict_info, list_name):
    result_dict = {}
    for i, k in dict_info.items():
        from_name = k[-1]
        for t in list_name:
            if t in k:
                result_dict[t] = from_name
    return result_dict


def correct_info(list):
    result = []
    for i in list:
        result.append(i[0])
    return result


def correct_info_id(list_i):
    result = []
    for i in list_i:
        result.append(i[1])
    return result


def correct_info_name(list_n):
    result_name = []
    for i in list_n:
        result_name.append(i[0])
    return result_name


def get_from_name_for_video(list_of_msg_id, list_of_name):
    dict_result = {}
    for i in list_of_msg_id:
        index = list_of_msg_id.index(i)
        try:
            difference = list_of_msg_id[index + 1] - list_of_msg_id[index]
            dict_result[i] = [k for k in range(i, i+difference)]
            dict_result[i].append(list_of_name[index])
        except:
            dict_result[i] = [i]
            dict_result[i].append(list_of_name[index])
    return dict_result


# list_of_msg_id = get_info_from_db()
# list_of_name = correct_info(get_info_from_db_2())
# correct_list_id = correct_info_id(list_of_msg_id)
# correct_list_name = correct_info_name(list_of_msg_id)
# dict_id = get_from_name_for_video(correct_list_id, correct_list_name)
# result = prepare_name_info(dict_id, list_of_name)


#update_db(result)
# example_list = [12, 15, 16, 18, 25, 29, 30, 35]
# get_from_name_for_video(example_list) 14424








