'''Написать программу, которая скачивает изображения с заданных URL-адресов и сохраняет их на диск. Каждое изображение должно сохраняться в отдельном файле, название которого соответствует названию изображения в URL-адресе.
Например, URL-адрес: https://example/images/image1.jpg -> файл на диске: image1.jpg
— Программа должна использовать многопоточный, многопроцессорный и асинхронный подходы.
— Программа должна иметь возможность задавать список URL-адресов через аргументы командной строки.
— Программа должна выводить в консоль информацию о времени скачивания каждого изображения и общем времени выполнения программы.'''


# Для Linux
# python3 app.py http://klublady.ru/uploads/posts/2022-02/1644966179_2-klublady-ru-p-krasivie-kapkeiki-foto-2.jpg https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663336066_54-mykaleidoscope-ru-p-melburn-stolitsa-krasivo-59.jpg http://thepointsguy.global.ssl.fastly.net/us/originals/2022/02/Brighton-bathing-boxes-and-Melbourne-skyline.jpg

# Для Windows
# python app.py http://klublady.ru/uploads/posts/2022-02/1644966179_2-klublady-ru-p-krasivie-kapkeiki-foto-2.jpg https://mykaleidoscope.ru/x/uploads/posts/2022-09/1663336066_54-mykaleidoscope-ru-p-melburn-stolitsa-krasivo-59.jpg http://thepointsguy.global.ssl.fastly.net/us/originals/2022/02/Brighton-bathing-boxes-and-Melbourne-skyline.jpg


import os
import sys
import threading
import time
import requests
from urllib.parse import urlparse
import threading
import multiprocessing
import asyncio
import httpx




folder = 'images'
threads = []
processes = []


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

# Получаем имена файлов из адресов url
def get_filename(url):
    return os.path.join(folder, os.path.basename(urlparse(url).path))

# Скачиваем изображения по указанным адресам
def download_data(url):
    image_content = requests.get(url, stream = True).content
    filename = get_filename(url)
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


# Многопроцессорный подход
@time_of_function
def dowload_images_proc():
    urls = get_urls()
    for url in urls:
        process = multiprocessing.Process(target=download_data, args=[url])
        processes.append(process)
        process.start()

    for proc in processes:
        proc.join()
    print('Многопроцессорный подход:')


# Асинхронный подход
async def save_files(url):
    filename = get_filename(url)
    with open(filename, 'wb') as f:
        async with httpx.AsyncClient() as client:
            async with client.stream('GET', url) as r:
                r.raise_for_status()
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

@time_of_function
async def main():
    print('Асинхронный подход:')
    loop = asyncio.get_running_loop()
    urls = get_urls()
    tasks = [loop.create_task(save_files(url)) for url in urls]
    await asyncio.gather(*tasks, return_exceptions = True)
    

if __name__ == "__main__":
    if not os.path.exists(folder):
        os.mkdir(folder)
    dowload_images()
    dowload_images_thr()
    dowload_images_proc()
    asyncio.run(main())
    
    