import os
import time
from dotenv import load_dotenv

import gspread
from oauth2client.service_account import ServiceAccountCredentials

from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

load_dotenv()

TABLE_URL = os.getenv("INPUT_URL")
TABLE_URL_OUTPUT = os.getenv("OUTPUT_URL")
RESULT = {}


def get_data_from_table(sheet_url):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url).sheet1

    values = sheet.col_values(1)

    return values


def scraping(urls):
    driver = webdriver.Chrome()

    driver.get("https://linkedin.com/uas/login")
    username = driver.find_element('id', "username")
    username.send_keys(os.getenv("LOGIN"))
    password = driver.find_element('id', "password")
    password.send_keys(os.getenv("PASSWORD"))
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(10)
    for url in urls:
        driver.get(url)
        response = driver.page_source

        soup = BeautifulSoup(response, 'lxml')
        data = soup.find('dd', {'class': 't-black--light text-body-small mb1'}).text.strip()
        RESULT[url] = data

    driver.quit()


def write_data_to_table(dict_data, link):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open_by_url(link).sheet1

    for key, value in dict_data.items():
        sheet.append_row([key, value])


def main():
    start = time.time()
    links = get_data_from_table(TABLE_URL)

    scraping(links)

    write_data_to_table(RESULT, TABLE_URL_OUTPUT)
    timer = time.time() - start
    print(timer)


if __name__ == '__main__':
    main()
