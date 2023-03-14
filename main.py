from bs4 import BeautifulSoup
from setup import URL
import requests

filteredNews = []
allNews = []


def get_url(url) -> str:
    """Отпровляем GET запрос сайту"""
    get_request = requests.get(url)
    return get_request


def get_data() -> list:
    """Парсим полученные данные"""
    html_docx = BeautifulSoup(get_url(URL).text, "html.parser")
    allNews = html_docx.findAll('div', class_='sc-aef7b723-0 dDQUel priceTitle')
    for data in allNews:
        first, two = data
        if two.find('span', class_='icon-Caret-up') is not None:
            filteredNews.append(two.text)
            return filteredNews


def transformation(text: str) -> float:
    end_result = ''
    percent = text
    for i in percent:
        if i != '%':
            end_result += i
    return float(end_result)


if __name__ == "__main__":
    start_percent = transformation(get_data()[0])
    print("Начальный процент: ", start_percent)

    while True:
        end_percent = transformation(get_data()[0])
        if (end_percent / start_percent) * start_percent - start_percent >= 1.0 or (
                end_percent - start_percent) / start_percent * 100 >= 1.0:
            print('Данные изменились на 1%: ', end_percent)

"""Не стал делать в ООП, так как посчитал это излишним для данного задания"""