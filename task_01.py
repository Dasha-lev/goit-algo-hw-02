import queue
import random
import time

#Створення черг для заявок
request_queue = queue.Queue()

#Функція для автоматичної генерації нових заявок
def generate_request():
    request_number = random.randint(1000, 9999)
    print(f"Нова заявка {request_number} додана до черги.")
    request_queue.put(request_number)  

#Функція для обробки заявок
def process_request():
    if not request_queue.empty(): 
        request_number = request_queue.get()  
        print(f"Заявка {request_number} оброблена.")
    else:
        print("Черга пуста. Немає заявок для обробки.")

#Автоматичне створення та обробка заявок
while True:
    generate_request()  
    time.sleep(1)  

    process_request()  
    time.sleep(1) 