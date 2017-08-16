from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#chrome_options.binary_location = '/opt/google/chrome/chrome'

driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://www.168seo.cn')
print("当前标题",driver.title)
print("当前网址",driver.current_url)

driver.quit()