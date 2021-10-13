import collections
import json
from collections import Counter
import time 
import subprocess
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue
from multiprocessing import Pool
import multiprocessing

def write_data(file_path, text, encoding='utf-8'):
    """Записать данные в файл."""
    with open(file_path, 'w') as fp:
        fp.write(text)


def get_file_data(file_path):
    """Прочитать целиком файл по пути."""
    data = ''
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = fp.read()

    return data

def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x

if __name__ == '__main__':
    answer =0
    PROCESSORS = multiprocessing.cpu_count()
    start_time = time.time()
    with Pool(PROCESSORS) as p:
        answer = sum(p.map(if_prime, list(range(1000000))))
    print(answer)
    print('Время выполнения:',time.time() - start_time, 'секунд')
