from functions import get_html, save_json, prepare_group_info, get_from_name_joined, get_from_name, prepare_video_info
from save_to_db import save_mysql_channel, save_mysql_group, save_mysql_video


# В данную переменную необходимо вставить путь к mhtml-файлу, который вы хотите спарсить
# Attention !!! mhtml-файлы должны быть взяты исключительно из \\192.168.100.100\SmartTech Learning Group


# В данной функции происходит вся магия)
# функция парсит все необходимые данные и на выходе дает список словарей со всей спарсенной информацией
def get_info(html):
    page_body = html.find('div', class_='history')
    messages_1 = page_body.find_all('div', class_='message default clearfix')
    messages_2 = page_body.find_all('div', class_='message default clearfix joined')
    dict_learning_id = {}
    dict_learning_id_2 = {}
    dict_learning_content = {}
    dict_all_content = {}
    for i in messages_1:
        message_details = i.get('id')  # message_details
        msg_id = ''.join(i.get('id').split('message'))  # message_id
        body = i.find('div', class_='body')
        from_name = ' '.join(body.find('div', class_='from_name').get_text().split())  # from_name
        title = body.find('div', class_='pull_right date details').get('title')  # time_data
        joined = False
        try:
            if from_name == 'SmartTech Learning':
                text = ' '.join(body.find('div', class_='text').get_text().split())  # text
                dict_learning_id[text] = [int(msg_id)]
                dict_learning_id[text].append(title)
                dict_learning_id[text].append(from_name)

            elif from_name == 'SmartTech Learning Group':
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')  # replied_message_details
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))  # replied_message_id
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                dict_all_content[msg_id] = [replied_message_details]
                dict_all_content[msg_id].append(title)
                dict_all_content[msg_id].append(message_details)
                dict_all_content[msg_id].append(joined)
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')  # file
                    dict_learning_content[reply_id] = [file_link]
                    dict_learning_content[reply_id].append(from_name)
                    dict_all_content[msg_id].append(file_link)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')  # url
                        dict_learning_content[reply_id] = [url]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text').get_text()  # text
                        dict_learning_content[reply_id] = [text_content]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(text_content)
                dict_all_content[msg_id].append(reply_id)
                dict_all_content[msg_id].append(from_name)
            else:
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                dict_all_content[msg_id] = [replied_message_details]
                dict_all_content[msg_id].append(title)
                dict_all_content[msg_id].append(message_details)
                dict_all_content[msg_id].append(joined)
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    dict_learning_content[reply_id] = [file_link]
                    dict_learning_content[reply_id].append(from_name)
                    dict_all_content[msg_id].append(file_link)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id] = [url]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text').get_text()
                        dict_learning_content[reply_id] = [text_content]
                        dict_learning_content[reply_id].append(from_name)
                        dict_all_content[msg_id].append(text_content)
                dict_all_content[msg_id].append(reply_id)
                dict_all_content[msg_id].append(from_name)
        except:
            pass
    for i in messages_2:
        message_details = i.get('id')  # message_details
        msg_id = ''.join(i.get('id').split('message'))  # message_id
        body = i.find('div', class_='body')
        title = body.find('div', class_='pull_right date details').get('title')  # time_data
        joined = True
        if body.find('div', class_='reply_to details'):
            reply_id_details = body.find('div', class_='reply_to details')
            replied_message_details = reply_id_details.find('a').get('href')
            reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
            try:
                if int(reply_id):
                    pass
            except:
                reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                reply_id = reply_id_list[1]
            dict_all_content[msg_id] = [replied_message_details]
            dict_all_content[msg_id].append(title)
            dict_all_content[msg_id].append(message_details)
            dict_all_content[msg_id].append(joined)
            try:
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    try:
                        dict_learning_content[reply_id].append(file_link)
                    except:
                        dict_learning_content[reply_id] = [file_link]
                    dict_all_content[msg_id].append(file_link)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id].append(url)
                        dict_all_content[msg_id].append(url)
                    except:
                        text_content = body.find('div', class_='text').get_text()
                        dict_learning_content[reply_id].append(text_content)
                        dict_all_content[msg_id].append(text_content)
            except:
                pass
            dict_all_content[msg_id].append(reply_id)
        else:
            try:
                text = ' '.join(body.find('div', class_='text').get_text().split())
                # dict_learning_id_2[text] = [title] 332
                # dict_learning_id_2[text].append(msg_id)
                dict_learning_id[text] = [int(msg_id)]
                dict_learning_id[text].append(title)
            except:
                pass

    results = [dict_learning_id, dict_learning_content, dict_all_content, dict_learning_id_2]
    return results


def get_video_info(html):
    dict_video_info = {}
    page_body = html.find('div', class_='history')
    messages_1 = page_body.find_all('div', class_='message default clearfix')
    messages_2 = page_body.find_all('div', class_='message default clearfix joined')
    for i in messages_1:
        message_details = i.get('id')  # message_details
        msg_id = ''.join(i.get('id').split('message'))  # message_id
        body = i.find('div', class_='body')
        if body.find('div', class_='reply_to details'):
            if body.find('div', class_='media_wrap clearfix'):
                box = body.find('div', class_='media_wrap clearfix')
                data_title = body.find('div', class_='pull_right date details').get('title')
                from_name = ' '.join(body.find('div', class_='from_name').get_text().split())
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')  # replied_message_details
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                if box.find('a', class_='video_file_wrap clearfix pull_left'):
                    video_box = box.find('a', class_='video_file_wrap clearfix pull_left')
                    video_path = video_box.get('href')
                    video_duration = ' '.join(video_box.find('div', class_='video_duration').get_text().split())
                    try:
                        description = ' '.join(body.find('div', class_='text').get_text().split())
                    except:
                        description = None
                    dict_video_info[int(msg_id)] = [int(reply_id), description, video_path, video_duration, data_title, message_details, replied_message_details, from_name]
                else:
                    pass
    for k in messages_2:
        message_details = k.get('id')  # message_details
        msg_id = ''.join(k.get('id').split('message'))  # message_id
        body = k.find('div', class_='body')
        if body.find('div', class_='reply_to details'):
            if body.find('div', class_='media_wrap clearfix'):
                box = body.find('div', class_='media_wrap clearfix')
                data_title = body.find('div', class_='pull_right date details').get('title')
                reply_id_details = body.find('div', class_='reply_to details')
                replied_message_details = reply_id_details.find('a').get('href')  # replied_message_details
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                try:
                    if int(reply_id):
                        pass
                except:
                    reply_id_list = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id_list[1]
                if box.find('a', class_='video_file_wrap clearfix pull_left'):
                    video_box = box.find('a', class_='video_file_wrap clearfix pull_left')
                    video_path = video_box.get('href')
                    video_duration = ' '.join(video_box.find('div', class_='video_duration').get_text().split())
                    try:
                        description = ' '.join(body.find('div', class_='text').get_text().split())
                    except:
                        description = None
                    dict_video_info[int(msg_id)] = [int(reply_id), description, video_path, video_duration, data_title, message_details, replied_message_details]
    return dict_video_info


fname = fr"Z:\SmartTech Learning Group\2023\9-24\messages3.html"
main_html = get_html(fname)  #  Здесь мы передаем путь к mhtml-файлу и происходит первичный парсинг через bs4
result = get_info(main_html)  #  Результат выше указанной функции(get_html) мы передаем в данную функцию(get_info), где и происходит основной сбор данных(парсинг)
save_json(result)  #  На данном этапе мы сохраняем полученныет данные в json формат, для первичного визуального анализа и дальнейшей обработки данных
prepare_info = prepare_group_info(result)  #  Здесь происходит первичная обработка данных
dict_reply = get_from_name_joined(result)  #  Здесь мы получаем словарь с replied_id и from_name
print(dict_reply)
ready_information = get_from_name(prepare_info, dict_reply) #  Данная функция возвращает на выходе готовый список данных из Learning Group для отправки в бд
video_dict = get_video_info(main_html)
result_2 = prepare_video_info(video_dict, result)


# save_mysql_video(result_2)
# save_mysql_group(ready_information)
# save_mysql_channel(result)  # Эта функция для сохранения в базу-данных информации для Learning channel
