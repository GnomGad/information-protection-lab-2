import argparse
import os.path
import collections
import os
from brute_force import BruteForce
from text_analyzer import TextAnalyzer
from symbol_analyzer import SymbolAnalyzer
from app import get_file_data, write_data


def read_action(dir, count, files:list):
    print(files)
    for file in files:
        data = get_file_data('{0}/{1}.txt'.format(dir,file))
        print(file)
        print(data[0:count])



def main(args):
    cores = 2 if not args.cores else args.cores
    krange = [1,1]
    bf = None
    verify = None

    # Если нету вообще ничего
    if not args.count and not args.range:
        raise Exception('Необходимо указать диапазон' )

    # Если есть ренж
    elif args.range:
        krange = args.range.split(':')
        if len(krange) != 2 or not (krange[0].isdigit() and krange[1].isdigit()):
            raise Exception('Диапазон указан неверно' )
        krange[0] = int(krange[0])
        krange[1] = int(krange[1])
    # Если нет ренжа
    else :
        krange[1] = abs(args.count)

    # Если нет папки то создать
    if not os.path.exists(args.dir):
        os.makedirs(args.dir)

    # Если есть bf и путь с файлом
    if args.bf and os.path.exists(args.bf):
        if not args.encrypted or not os.path.exists(args.encrypted):
                raise Exception('Нет зашифрованого файла' )
        bf = BruteForce(cores, krange, args.bf, args.encrypted, args.dir)
        res = bf.execute()
        print('Секунд ', res[1])

    # если есть verify то отобразить
    if args.verify:
        if not os.path.exists(args.verify):
            raise Exception('Файла со словами не существует')
        ta = TextAnalyzer(cores, krange, args.verify, args.dir)
        res = ta.execute()
        print('Секунд', res[1])
        print('Возможные ключи', res[3])
        if(args.read):
            read_action(args.dir, args.read, res[3])



# Путь с декодированием
# Путь к папке с app.py
# Путь к файлу со словами для проверки
# Количество проходов
# python main.py  /home/odin/Source/information-protection-lab-2/ex -b /home/odin/Source/information-protection-lab-1/app.py -e /home/odin/Source/information-protection-lab-1/o.txt  -v words.txt -r 100:500 -C 16
# python main.py C:\Users\odin\source\github\information-protection-lab-2/ex -b C:\Users\odin\source\github\information-protection-lab-1/app.py -e C:\Users\odin\source\github\information-protection-lab-1/o.txt -r 1000:9999 -C 12
# python main.py C:\Users\odin\source\github\information-protection-lab-2/ex -v C:\Users\odin\source\github\information-protection-lab-2/words -e -r 1000:9999 -C 12

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='Путь к папке с результатом для брутфосом')
    parser.add_argument('-b', '--brute', dest='bf', help='Если нужен брутфорс, то необходимо указать путь к  app.py из первой лабы')
    parser.add_argument('-e', '--encrypted', dest='encrypted', help='Файл для расшифроки')
    parser.add_argument('-v', '--verify', dest='verify', help='Если нужно проверить результат брутфорса, то необходимо указать путь к файлу со словами')
    parser.add_argument('-r','--range', dest='range',type=str, help='Диапазон в формате 1000:5000')
    parser.add_argument('-c', '--count', dest='count',type=int,  help='Диапазон от 0 до count')
    parser.add_argument('-C','--cores', dest='cores', type=int, help='Количество ядер процессора, что участвуют в процессе max или количество')
    parser.add_argument('-R','--read', dest='read',type=int, default=0, help='Прочитать количество символов')
    args = parser.parse_args()

    main(args)