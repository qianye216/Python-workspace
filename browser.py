import webbrowser
import sys
import pyperclip

webbrowser.open('https://www.baidu.com')

adress = pyperclip.paste()
print(adress)
