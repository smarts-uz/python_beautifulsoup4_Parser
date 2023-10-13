from functions import get_html, save_json, save_db



fname = r"D:\python\parser\mhtlm_files\messages6.html"


def get_info(html):
    page_body = html.find('div', class_='history')
    messages_1 = page_body.find_all('div', class_='message default clearfix')
    messages_2 = page_body.find_all('div', class_='message default clearfix joined')
    dict_learning_id = {}
    dict_learning_content = {}
    for i in messages_1:
        msg_id = ''.join(i.get('id').split('message'))
        body = i.find('div', class_='body')
        from_name = ' '.join(body.find('div', class_='from_name').get_text().split())
        try:
            if from_name == 'SmartTech Learning':
                text = ' '.join(body.find('div', class_='text').get_text().split())
                dict_learning_id[text] = int(msg_id)

            elif from_name == 'SmartTech Learning Group':
                reply_id_details = body.find('div', class_='reply_to details')
                reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    dict_learning_content[reply_id] = [file_link]
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id] = [url]
                    except:
                        text_content = body.find('div', class_='text').get_text()
                        dict_learning_content[reply_id] = [text_content]
            else:
                reply_id_details = body.find('div', class_='reply_to details')
                #reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                try:
                    reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
                    reply_id = int(reply_id)
                except:
                    reply_id = reply_id_details.find('a').get('href').split('#go_to_message')
                    reply_id = reply_id[1]
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    dict_learning_content[reply_id] = [file_link]
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id] = [url]
                    except:
                        text_content = body.find('div', class_='text').get_text()
                        dict_learning_content[reply_id] = [text_content]

        except:
            pass
    for i in messages_2:
        body = i.find('div', class_='body')
        if body.find('div', class_='reply_to details'):
            reply_id_details = body.find('div', class_='reply_to details')
            reply_id = ''.join(reply_id_details.find('a').get('href').split('#go_to_message'))
            # try:
            #     if int(reply_id):
            #         reply_id = reply_id
            # except:
            #     reply_id = reply_id_details.find('a').get('href').split('#go_to_message')
            #     reply_id = reply_id[1]
            try:
                if body.find('div', class_='media_wrap clearfix'):
                    box = body.find('div', class_='media_wrap clearfix')
                    file_link = box.find('a').get('href')
                    dict_learning_content[reply_id].append(file_link)
                else:
                    try:
                        box_url = body.find('div', class_='text')
                        url = box_url.find('a').get('href')
                        dict_learning_content[reply_id].append(url)
                    except:
                        text_content = body.find('div', class_='text').get_text()
                        dict_learning_content[reply_id].append(text_content)



            except:
                pass
        else:
            pass
    results = [dict_learning_id, dict_learning_content]
    return results


main_html = get_html(fname)
result = get_info(main_html)
save_json(result)
#save_db(result)