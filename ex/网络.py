import requests

res = requests.get('http://down.115.com/client/mac/115br_v8.4.0.19.dmg')
# print(res.text)
# print(len(res.text))
# print(res.text[:3])
# print(res.text[2000:])
res.raise_for_status()
playfile = open('./115chrome.dmg', 'wb')
for chunk in res.iter_content(100000):
    playfile.write(chunk)

playfile.close()
print('下载文件成功')
