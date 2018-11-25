from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
list_urls=[]
chrome_options =webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://www.5442.com/tag/rosi.html")

html = driver.page_source
driver.close()

bf=BeautifulSoup(html,'html.parser')
print(bf.title)
