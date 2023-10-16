import os
import shutil

post_title = "form_builder_chips_input | @ Bads | Form Builders | Flutter".split('|') # post title divide to list
post_title.reverse()  # reverse created list

actual_path = 'D:\\test\\7\\' # path where we will save our data

#loop for creating
for i in post_title:
    actual_path = actual_path + i + "\\"
    os.mkdir(actual_path)
renamed_file = '\Copied_SmartDust Labs.mp4'
file_location = 'C:\\Users\\Administrator\\Downloads\\SmartDust Labs.mp4'
shutil.copyfile(file_location, actual_path + renamed_file)


def name_reducer(viriable):
    limit = 100
    if len(viriable) > limit:
        x = len(viriable) - limit
        viriable = viriable.replace(viriable[-x:], '')
    else:
        pass

def crop_title(): #приминяеться для удаления расширения медия
    a = "Don't put dots after folder name. Collect design related files only via Total Commander !!!.mp4"
    if '.mp4' in a:
        a = a.split(' ') # changing from str to lists (diving)
        del a[-1] #deleting .mp4
        print(a)
        
def removing_hashtags(): # убираются хэштеги
    pass
