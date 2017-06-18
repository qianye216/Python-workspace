import os

for folderName,subfolders,filename in os.walk(os.get_cwd):
    print('当前目录是'+folderName)