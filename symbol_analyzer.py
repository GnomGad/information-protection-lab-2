import argparse
import os.path
import json
from collections import Counter 
from app import get_file_data, write_data


class SymbolAnalyzer:
    """Функционал для работы с анализом символов"""

    def get_symbols_frequency(self, data:str) ->  dict:
        """Из текстовой строки анализирует частоту появления каждого символа"""
        dct = dict(Counter(data))
        dst = {k:dct[k] for k in self.get_alphabet(dct)}
        print(dst)
        return dst

    def get_symbols_frequency_from_alphabet(self, data:str, alp:list) -> dict:
        """Из текстовой строки анализирует частоту появления каждого символа и выдает результат только по алфавиту"""
        symbols_frequency = dict(self.get_symbols_frequency(data))
        only_symbols = [i for i in symbols_frequency.keys()]
        dst = {k:symbols_frequency[k] for k in list(set(only_symbols) & set(alp))}
        return {k:dst[k] for k in self.get_alphabet(dst)}

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


def main(args) -> None:
    sa = SymbolAnalyzer()
    data = None
    freq_symb = None
    created_alp = None
    if args.file and os.path.exists(args.file):
        data = get_file_data(args.file)

        if args.lower:
            data = data.lower()
        if args.alp and os.path.exists(args.alp):
            freq_symb = sa.get_symbols_frequency_from_alphabet(data, get_file_data(args.alp))
        else:
            freq_symb = sa.get_symbols_frequency(data)
        created_alp = sa.get_alphabet(freq_symb)
    if args.analyse_freq:
        if args.percents:
            sa.write(sa.get_frequency_analyse(freq_symb), args.analyse_freq)
        else:
            sa.write(freq_symb, args.analyse_freq)
    if args.alp_create:
        write_data(args.alp_create, args.separ.join(created_alp))

# python symbol_analyzer.py -f C:\Users\odin\source\github\information-protection-lab-2/ex/5914.txt -a 'an.json' -c 'file.txt' --lower -A alp -p

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Анализатор символов')
    parser.add_argument('-f','--file', dest='file', default=None, help='Файл с данными для анализа', required=True)
    parser.add_argument('-a','--analyse', dest='analyse_freq', default=None, help='Проанализировать частоту явления символов и вывести в файл')
    parser.add_argument('-p','--percents', dest='percents',action='store_true', default=False, help='Вывод в процентах')
    parser.add_argument('-c', '--create-alp', dest='alp_create', default=None, help='Создать алфавит сортированный')
    parser.add_argument('--lower', dest='lower',action='store_true', default=False, help='Привести данные из файла к lower')
    parser.add_argument('-A', dest='alp', default=None, help='Применить алфавит')
    parser.add_argument('-s',dest='separ', default='', help='Символ сепарации для алфавита')
    main(parser.parse_args())