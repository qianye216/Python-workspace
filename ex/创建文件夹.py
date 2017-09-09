import os


def create_project_dir(directory):
    if not os.path.exists(directory):
        print('创建文件夹' + directory)
        os.makedirs(directory)
    else:
        print(directory + '文件夹已存在')


create_project_dir('mylovee')
