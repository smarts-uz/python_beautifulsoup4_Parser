from bs4 import BeautifulSoup
import json


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
        dict_reply_id_name[int(x)] = y[1]
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
    print(result)
    return result
















