import collections
import json
from collections import Counter 

def pizdec():
    d = collections.Counter() #collections.defaultdict(int)
    l = 0
    with open('d.txt', 'r')as f:
        data = f.read()
        d = Counter(data) 
        l = len(data)
    d = d.most_common()
    for i in d:
        print(i,'=', i[1]/l)

def generate_list_for_frequency_analyse(d: dict = None):
    if d is None:
        with open('freq.json', encoding='UTF-8') as file:
            d = json.load(file)

    return [element[0] for element in sorted(d.items(), key=lambda x: x[1], reverse=True)]

if __name__ == '__main__':
    #print(generate_list_for_frequency_analyse())
    pizdec()