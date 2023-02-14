import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://greenatom.ru/"


def start_webdriver():
    WebDriverWait(driver, 1).until(lambda driver_: driver.execute_script('return document.readyState') == 'complete')
    driver.get(url)
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    all_elements = soup.find_all()
    return all_elements


def get_all_html_tags():
    all_elements = start_webdriver()
    sp_tags = ([tag.name for tag in all_elements])
    amount_sp_tags = len(sp_tags)
    return amount_sp_tags


def get_html_tags_with_attribute():
    all_elements = start_webdriver()
    sp_tag_attrs = [tag.attrs for tag in all_elements if tag.attrs != {}]
    amount_sp_tag_attrs = len(sp_tag_attrs)
    return amount_sp_tag_attrs


if __name__ == "__main__":
    print('Количество HTML-тегов:', get_all_html_tags())
    print('Количество HTML-тегов с аттрибутами:', get_html_tags_with_attribute())
