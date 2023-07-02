# from bs4 import BeautifulSoup
# import requests
#
#
# url = "https://www.gumtree.com.au/s-seller/Jenni/1021104876/date/1"
# response = requests.get(url)
# html_code = response.content
# html_variable = html_code.decode("utf-8")
# print(html_variable)
# # soup = BeautifulSoup(html_code, "lxml")
# # print(soup.prettify())
from selenium import webdriver

url = "https://www.gumtree.com.au/s-seller/Jenni/1021104876/date/1"

# Инициализация браузера
driver = webdriver.Chrome(r"C:\Users\strel\PycharmProjects\chromedriver.exe")  # Укажите путь к драйверу для выбранного браузера
driver.get(url)

# Получение полного состояния страницы после выполнения JavaScript
html_code = driver.page_source

# Закрытие браузера
driver.quit()

# Теперь у вас есть полный HTML-код страницы, включая результаты выполнения JavaScript
print(html_code)
