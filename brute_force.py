import json
import re
import time 
import subprocess
from subprocess import PIPE
from multiprocessing import  Pool
from app import get_file_data
import multiprocessing
import tqdm
import os.path


class BruteForce():
    """Смысл в прямом подборе пароля. Работает только если пароль  x < 5 знаков"""
    def __init__(self, cores_count:int, start_end:list,app:str, file:str, edir:str, alp:str=None)  -> None:
        self.cores = cores_count
        self.start_end = start_end
        self.file = file
        self.app = app
        self.dir = edir
        self.alp = alp
        CORES = multiprocessing.cpu_count()

        if  cores_count < 1 or cores_count > CORES:
            self.cores = CORES

    def execute(self) -> list:
        lenB= max(self.start_end)+1 - min(self.start_end)
        lst = self.get_full_range()
        start_time = time.time()
        with Pool(self.cores) as p:
            res = list(tqdm.tqdm(p.imap(self.command, lst),total=lenB,desc='Ядер использовано {0}'.format(self.cores)))
        end = time.time() - start_time
        return [self.cores, end, lenB]
    
    def command(self, i:int) -> int:
        """Выполнить необходимое действие"""
        alp = '--alp {0}'.format(self.alp) if self.alp is not None else ''
        cm = 'python {1} -a decrypt -i {2} -o {3} -k {0} {4}'.format(i, self.app, self.file, os.path.join(self.dir, str(i)+'.txt'),alp)
        proc = subprocess.Popen(cm, shell=True, stdout=PIPE)
        proc.wait()
        proc.communicate()
        return i
    
    def get_full_range(self):
        _min = min(self.start_end)
        _max = max(self.start_end)
        lst = []

        count = len(str(_max)) - len(str(_min))
        for i in range(_min, _max+1):
            if i in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]:
                count -= 1
            lst.append('0'*count+str(i))
        return lst

def sex()->list():
    lst = []
    start_end=[0, 999]
    count = len(str(start_end[1])) - len(str(start_end[0]))

    for i in range(start_end[0], start_end[1]+1):
        if i in [10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000]:
            count -= 1
        lst.append('0'*count+str(i))

    return lst

    
