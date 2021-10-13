
import json
import re
import time 
import subprocess
from subprocess import Popen, PIPE
from multiprocessing import Process, Queue, Pool
from app import get_file_data
import multiprocessing
import tqdm

from app import write_data, get_file_data
path_lab1 = 'C:\\Users\\odin\\source\\github\\information-protection-lab-1\\'

"""Смысл в прямом подборе пароля. Работает только если пароль  x < 5 знаков"""

# TODO: Вынести в класс этот функционал

def execute(i):
        proc = subprocess.Popen('cd {1} && python app.py -a decrypt -i o.txt -o .\ex\{0}.txt -k {0}'.format(i,path_lab1), shell=True, stdout=PIPE)
        proc.wait()
        out = proc.communicate()
        return i

def check(i):
    s = get_file_data('{0}ex\\{1}.txt'.format(path_lab1, i))
    d = s.split(' ')
    new_lst = lst_words
    for word in d:
        word = word.lower()
        if  word in new_lst:
            new_lst.remove(word)
            if not new_lst:
                return i
keys = []
allProcesses = []

lst_words = 'что и в не я хочешь'.split(' ')
lenB = 10000

if __name__ == '__main__':
    PROCESSORS = multiprocessing.cpu_count()
    start_time = time.time()
    res = []
    # TODO: перенести в отдельную функцию дешифровку
    #with Pool(PROCESSORS) as p:
    #    res = list(tqdm.tqdm(p.imap(execute, list(range(lenB))),total=lenB))

    # TODO: перенести в отдельную функцию поиск
    with Pool(PROCESSORS) as p:
        res = list(tqdm.tqdm(p.imap(check, list(range(lenB))),total=lenB))
        for r in res:
            if r:
                print("Предположительный ключ:", r)
    print('Время выполнения:',time.time() - start_time, 'секунд')
    print('Все файлы находятся в {0}\\ex\\'.format(path_lab1))
