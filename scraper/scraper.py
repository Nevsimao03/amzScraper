import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
from random import random

# url = 'https://www.amazon.com/'

def get_url(search_term):
    #make a url
    tempurl = 'https://www.amazon.com/s?k={}&ref=nb_sb_ss_ts-doa-p_1_6'
    search_term = search_term.replace(' ', '+')
    #pagination
    url = tempurl.format(search_term)
    url += '&page{}'

    return url

def extract_data(item):
    #description & url
    atag = item.h2.a
    description = atag.text.strip()
    url = 'https://www.amazon.com' + atag.get('href')
    #price
    try:
        price_parent = item.find('span', 'a-price')
        price = price_parent.find('span', 'a-offscreen').text
    except AttributeError:
        return
    #rating & review
    try:
        rating = item.i.text
    except AttributeError:
        rating = ''
    try:
        review_count = item.find('span', {'class': 'a-size-base', 'dir': 'auto'}).text
    except AttributeError:
        review_count = ''
    
    result = (description, price, review_count, rating, url)

    return result

def main(search_term):
    driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")

    records = []
    url = get_url(search_term)

    for page in range(1, 21):
        driver.get(url.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        results = soup.find_all('div', {'data-component-type': 's-search-result'})

        for item in results:
            record = extract_data(item)
            if record:
                records.append(record)
                # time.sleep(3)

    driver.close()

    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Description', 'Price', 'Rating', 'ReviewCount', 'Url'])
        writer.writerows(records)

main('xbox games')