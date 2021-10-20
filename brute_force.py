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
    def __init__(self, cores_count:int, start_end:list,app:str, file:str, edir:str)  -> None:
        self.cores = cores_count
        self.start_end = start_end
        self.file = file
        self.app = app
        self.dir = edir

        CORES = multiprocessing.cpu_count()

        if  cores_count < 1 or cores_count > CORES:
            self.cores = CORES

    def execute(self) -> float:
        lenB= max(self.start_end)+1 - min(self.start_end)
        start_time = time.time()
        with Pool(self.cores) as p:
            res = list(tqdm.tqdm(p.imap(self.command, list(range(min(self.start_end) ,max(self.start_end)+1 ))),total=lenB,desc='Ядрер использовано {0}'.format(self.cores)))
        end = time.time() - start_time
        return [self.cores, end, lenB]

    def command(self, i:int) -> int:
        """Выполнить необходимое действие"""
        cm = 'python {1} -a decrypt -i {2} -o {3} -k {0}'.format(i, self.app, self.file, os.path.join(self.dir, str(i)+'.txt'))
        proc = subprocess.Popen(cm, shell=True, stdout=PIPE)
        proc.wait()
        proc.communicate()
        return i