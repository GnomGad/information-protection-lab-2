import json
from collections import Counter 
from app import get_file_data


class SymbolAnalyzer:
    """Функционал для работы с анализом символов"""

    def get_symbols_frequency(self, data:str) ->  dict:
        """Из текстовой строки анализирует частоту появления каждого символа"""
        return dict(Counter(data))

    def get_symbols_frequency_from_alphabet(self, data:str, alp:list) -> dict:
        """Из текстовой строки анализирует частоту появления каждого символа и выдает результат только по алфавиту"""
        symbols_frequency = dict(self.get_symbols_frequency(data))
        only_symbols = [i for i in symbols_frequency.keys()]
        return {k:symbols_frequency[k] for k in list(set(only_symbols) & set(alp))}


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
    alp=list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    sa = SymbolAnalyzer()
    s = get_file_data('file.txt').lower()
    print(sa.get_alphabet(sa.get_frequency_analyse(sa.get_symbols_frequency_from_alphabet(s,alp))))
