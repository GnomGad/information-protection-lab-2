import time 
from subprocess import Popen, PIPE
from multiprocessing import Pool
from app import get_file_data
import tqdm

from app import write_data, get_file_data


class TextAnalyzer():
    def __init__(self, cores_count:int, start_end:list, file:str, edir:str):
        self.cores = cores_count
        self.start_end = start_end
        self.file = file
        self.dir = edir
        self.words = get_file_data(file).split(' ')
    

    def command(self, i:int):
        s = get_file_data('{0}/{1}.txt'.format(self.dir, i))
        d = s.split(' ')
        new_words = self.words
        for word in d:
            word = word.lower()
            if  word in new_words:
                new_words.remove(word)
                if not new_words:
                    return i
                    
    def execute(self ):
        lenB= max(self.start_end)+1 - min(self.start_end)
        start_time = time.time()
        lst_keys = list()
        with Pool(self.cores) as p:
            res = list(tqdm.tqdm(p.imap(self.command, list(range(min(self.start_end) ,max(self.start_end)+1 ))),total=lenB,desc='Ядрер использовано {0}'.format(self.cores)))
            for r in res:
                if r:
                    lst_keys.append(r)

        end = time.time() - start_time
        return [self.cores, end, lenB, lst_keys]





