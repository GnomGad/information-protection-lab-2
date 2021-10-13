import collections
import json
from collections import Counter 


def file_frequency_analyse(file_path:str) -> dict:
    """Прочитать целиком файл по пути."""
    data = ''
    with open(file_path, 'r', encoding='utf-8') as fp:
        data = fp.read()
    return frequency_analyse(data)

def frequency_analyse(data:str) -> dict:
    """Функция реализующая подсчет """
    d = collections.Counter() #collections.defaultdict(int)
    d = Counter(data) 
    l = len(data)
    d = dict(d)
    with open('f.json', 'w',encoding='utf-8') as f:
        json.dump(d,f,ensure_ascii=False)


if __name__ == '__main__':
    file_frequency_analyse('d.data')