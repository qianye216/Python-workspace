import os
import zipfile

# exampleZip = zipfile.ZipFile('./归档.zip')
# print(exampleZip.namelist())
newZip = zipfile.ZipFile('ceshi.zip', 'w')
newZip.write('./遍历.py', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
