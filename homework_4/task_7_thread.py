# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопоточность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import time

import threading


def sum_number_mass(arr: list[int]):
    global sum
    temp = 0

    for i in arr:
        temp += i
    sum += temp


if __name__ == "__main__":
    start_time = time.time()
    
    sum: int = 0
    main_array = []
    threads: list[threading.Thread] = []


    for _ in range(1000):
        array: list[int] = [randint(1, 100) for _ in range(1000)]
        thread = threading.Thread(target=sum_number_mass, args=[array])
        main_array.extend(array)
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()
        
    print(main_array)
    print(f'Количество элементов в массиве: {len(main_array)}')
    print(f'Сумма чисел массива равна: {sum}')
    print(f'Функция завершена за {round(time.time() - start_time, 2)} секунд.')