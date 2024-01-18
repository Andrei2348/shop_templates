'''Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.'''



# python3 app.py http://klublady.ru/uploads/posts/2022-02/1644966179_2-klublady-ru-p-krasivie-kapkeiki-foto-2.jpg https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663336066_54-mykaleidoscope-ru-p-melburn-stolitsa-krasivo-59.jpg http://thepointsguy.global.ssl.fastly.net/us/originals/2022/02/Brighton-bathing-boxes-and-Melbourne-skyline.jpg


import os
import sys
import threading
import time
import requests
from urllib.parse import urlparse
import threading

folder = 'images'
threads = []


# Функция-декоратор для измерения времени выполнения функции
def time_of_function(function):
    def wrapped_function(*args):
        start_time = time.time()
        result = function(*args)
        print(f'Время выполнения функции: {time.time() - start_time}')
        return result
    return wrapped_function


# Получаем адреса из командной строки
def get_urls():
    return sys.argv[1:]


# Скачиваем изображения по указанным адресам
def download_data(url):
    image_content = requests.get(url).content
    filename = (os.path.join(folder, os.path.basename(urlparse(url).path)))
    with open(filename, 'wb') as f:
        f.write(image_content)


# Синхронный подход
@time_of_function
def dowload_images():
    urls = get_urls()
    for url in urls:
        download_data(url)
    print('Синхронный подход:')


# Многопоточный подход
@time_of_function
def dowload_images_thr():
    urls = get_urls()
    for url in urls:
        thread = threading.Thread(target=download_data, args=[url])
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
    print('Многопоточный подход:')


if __name__ == "__main__":
    if not os.path.exists(folder):
        os.mkdir(folder)
    dowload_images()
    dowload_images_thr()
   