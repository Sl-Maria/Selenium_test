from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

def search_wikipedia(query):
    search_box = browser.find_element(By.ID,"searchInput")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)

def list_paragraphs():
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)
        input()

def navigate_to_related_page():
    hatnotes = []
    for element in browser.find_elements(By.TAG_NAME, "div"):
        cl = element.get_attribute("class")
        if cl == "hatnote navigation-not-searchable":
            hatnotes.append(element)
    if hatnotes:
        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
        header = browser.find_element(By.TAG_NAME, "h1").text
        print ("Текущая статья: " + header)
    else:
        print("Нет связанных страниц.")

def user_interaction():
    while True:
        print("\nДоступные действия:")
        print("1. Листать параграфы текущей статьи")
        print("2. Перейти на одну из связанных страниц")
        print("3. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            list_paragraphs()
        elif choice == '2':
            navigate_to_related_page()
        elif choice == '3':
            print("Выходим из программы...")
            break
        else:
            print("Неверный ввод. Повторите попытку.")


initial_query = input("Введите поисковый запрос на Wikipedia: ")
browser = webdriver.Chrome()
browser.get("https://www.wikipedia.org/")
assert "Wikipedia" in browser.title
time.sleep(2)
search_wikipedia(initial_query)
time.sleep(2)
user_interaction()
time.sleep(1)
browser.quit()
