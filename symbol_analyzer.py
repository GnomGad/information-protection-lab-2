import json
from collections import Counter 

class SymbolAnalyzer:
    """Функционал для работы с анализом символов"""

    def get_symbols_frequency(self, data:str) ->  dict:
        """Из текстовой строки анализирует частоту появления каждого символа"""
        return dict(Counter(data) )


    def get_frequency_analyse(self, data:dict,) -> dict:
        """Подсчитывает частоту появление"""
        l = sum(data.values(), 0)
        return { i:data[i] / l for i in data}


    def write(self, data:dict, file:str) -> None:
        """Записать словарь в json файл"""
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

    def read(self, file:str)-> dict:
        """Читать json и вернуть словарь"""
        with open(file, encoding='UTF-8') as file:
            d = json.load(file)
        return d
    
    def get_alphabet(self, data:dict) -> list:
        """Сортирует по убыванию данных и возвращает лист"""
        return list(dict(sorted(data.items(), key=lambda kv: kv[1], reverse=True)).keys())


if __name__ == '__main__':
    s = 'keksss'
    f = 'anas12s218s.json'
    sa = SymbolAnalyzer()
    #sa.write(sa.get_frequency_analyse(sa.get_symbols_frequency(s)), f)
    print(sa.get_sorted_list_symbols(sa.get_symbols_frequency(s)))
    
