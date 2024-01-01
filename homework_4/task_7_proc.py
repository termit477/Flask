# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать многопроцессорность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import time

import multiprocessing


def sum_number_mass(arr: list[int], temp: multiprocessing.Value):
    current_sum = 0

    for i in arr:
        current_sum += i

    with temp.get_lock():
        temp.value += current_sum


def main():
    sum = multiprocessing.Value('i', 0)
    main_array: list[int] = []
    processes: list[multiprocessing.Process] = []

    for _ in range(1000):
        array = [randint(1, 100) for _ in range(1000)]
        process = multiprocessing.Process(target=sum_number_mass, args=(array, sum))
        main_array.extend(array)
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(main_array)
    print(f'Количество элементов в массиве: {len(main_array)}')
    return sum


if __name__ == "__main__":
    start_time = time.time()
    
    result = main()

    with result.get_lock():
        sum = result.value

    print(f'Сумма чисел массива равна: {sum}')
    print(f'Функция завершена за {round(time.time() - start_time, 2)} секунд.')