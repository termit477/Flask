# Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами от 1 до 100.
# При решении задачи нужно использовать асинхронность.
# В каждом решении нужно вывести время выполнения вычислений.

from random import randint
import time

import asyncio


main_array: list[int] = []
sum: int = 0


async def sum_number_mass(arr: list[int]):
    global sum
    temp = 0

    for i in arr:
        temp += i
    sum += temp


async def main():
    global main_array
    tasks: list[asyncio.Task] = []

    for _ in range(1000):
        array = [randint(1, 100) for _ in range(1000)]
        task = asyncio.create_task(sum_number_mass(array))
        main_array.extend(array)
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start_time = time.time()

    asyncio.run(main())

    print(main_array)
    print(f'Количество элементов в массиве: {len(main_array)}')
    print(f'Сумма чисел массива равна: {sum}')
    print(f'Функция завершена за {round(time.time() - start_time, 2)} секунд.')