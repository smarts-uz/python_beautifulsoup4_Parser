import os
import shutil

post_title = "form_builder_chips_input | @ Bads | Form Builders | Flutter".split('|') # post title divide to list
post_title.reverse()  # reverse created list

# path where we will save our data
actual_path = 'D:\\test\\11\\'

renamed_file = '\Copied_SmartDust Labs.mp4'
#loop for creating

def folder_structure(post_title, actual_path, renamed_file):
    for i in post_title:
        actual_path = actual_path + i + "\\"
        if not os.path.exists(actual_path):
            os.mkdir(actual_path)
    file_location = fr'C:\Users\Administrator\Downloads\SmartDust Labs.mp4'
    shutil.copyfile(file_location, actual_path + renamed_file)


def name_reducer(viriable):
    limit = 10
    if len(viriable) > limit:
        x = len(viriable) - limit
        extension = (viriable[-5:])
        viriable = viriable.replace(viriable[-x:], '') + extension
        return viriable
    else:
        pass

def crop_title(): #приминяеться для удаления расширения медия
    a = "Don't put dots after folder name. Collect design related files only via Total Commander !!!.mp4"
    if '.mp4' in a:
        a = a.split(' ') # changing from str to lists (diving)
        del a[-1] #deleting .mp4
        print(a)
        
def removing_hashtags(target): # remove hashtags
    target = target.replace("#", " ")


folder_structure(post_title, actual_path,name_reducer(renamed_file))