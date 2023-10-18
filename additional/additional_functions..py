import os
from os import listdir


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