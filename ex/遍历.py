import os

for folderName,subfolders,filename in os.walk(os.getcwd):
    print('当前目录是'+folderName)