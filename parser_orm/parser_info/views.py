from parser_info.parser import final_result_info
from .functions import update_db
from parser_info.models import channel_content, group_content, group_video_content


def channel_content_db_add(dict_1):
    for i, k in dict_1.items():
        try:
            from_name = k[2]
        except:
            from_name = 'SmartTech Learning'
        text = i
        title = k[1]
        msg_id = k[0]
        data = {'form_name': from_name, 'text': text, 'title': title, 'message_id': msg_id}
        my_model_instance = channel_content(**data)
        my_model_instance.save()


def group_content_db_add(list2):
    for i in list2:
        from_name = i[0]
        text = i[1]
        content = i[2]
        data_title = i[3]
        message_details = i[4]
        msg_id = i[5]
        replied_message_details = i[6]
        reply_id = i[7]
        joined = i[8]
        data = {'from_name': from_name, 'text': text, 'content': content, 'title': data_title, 'message_details': message_details, 'message_id': msg_id, 'replied_message_details': replied_message_details, 'replied_message_id': reply_id, 'joined': joined}
        my_model_instance = group_content(**data)
        my_model_instance.save()


def group_video_content_db_add(list_v):
    for i in list_v:
        if i[0] != 'Null':
            text_from_learning = i[0]
            video_path = i[1]
            description = i[2]
            video_duration = i[3]
            data_title = i[4]
            message_details = i[5]
            msg_id = i[6]
            replied_message_details = i[7]
            replied_id = i[8]
            from_name = i[9]
            data = {'text_from_learning': text_from_learning, 'video_path': video_path, 'description': description, 'video_duration': video_duration, 'data_title': data_title, 'message_details': message_details, 'message_id': msg_id, 'replied_message_details': replied_message_details, 'replied_id': replied_id, 'from_name': from_name}
            my_model_instance = group_video_content(**data)
            my_model_instance.save()
        else:
            pass
        print("record inserted.")


while True:
    path = input('Type path: ')
    if path.lower() == 'update_db':
        update_db()
    else:
        info_list = final_result_info(path)
        for i in info_list[0]:
            channel_content_db_add(i)
        for k in info_list[1]:
            group_content_db_add(k)
        for j in info_list[2]:
            group_video_content_db_add(j)




