from selenium import webdriver
from bs4 import BeautifulSoup
#Get the driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")
#The main url
url = 'https://www.amazon.com/'
#Make a url based on product search
def get_url(search_term):
    tempurl = 'https://www.amazon.com/s?k={}&ref=nb_sb_ss_ts-doa-p_1_6'
    search_term = search_term.replace(' ', '+')
    return tempurl.format(search_term)

url = get_url('dog food')
# driver.get(url)
#Get the data
soup = BeautifulSoup(driver.page_source, 'html.parser')
results = soup.find_all('div', {'data-component-type': 's-search-result'})
print(len(results))