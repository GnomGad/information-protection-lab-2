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
    with open(file_path, 'w+') as fp:
        fp.write(text)


def get_file_data(file_path):
    """Прочитать целиком файл по пути."""
    data = ''
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = fp.read()

    return data