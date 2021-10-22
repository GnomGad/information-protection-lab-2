import os.path
import multiprocessing
import argparse
from brute_force import BruteForce
from app import get_file_data, write_data
from cpuinfo import get_cpu_info

import numpy as np
import matplotlib.pyplot as plt

def graphic(height, bars, name):
    y_pos = np.arange(len(bars))
    data = plt.bar(y_pos, height)
    data[np.argmin(height)].set_color('red')
    plt.xticks(y_pos, bars)
    plt.ylabel('сек', fontweight='bold', color = 'blue', fontsize='12')
    plt.xlabel('количество ядер', fontweight='bold', color = 'orange', fontsize='16')
    for i in range(len(y_pos)):
        plt.text(x = y_pos[i] - (data[i]._width / 2) , y = height[i]+0.02, s = f"{height[i]:.{4}}", size = 8)
    figure = plt.gcf()  # get current figure
    figure.set_size_inches(9.6, 5.4)
    plt.savefig(name,dpi=300)
    plt.show()


def main(krange:list, cores:list, enc: str, name:str):
    #cores = multiprocessing.cpu_count()
    lab1 = os.path.join('..\\','information-protection-lab-1')
    lab2 = os.path.join('.')
    app_bf = os.path.join(lab1, 'app.py')
    encrypted= os.path.join(enc)
    dir= os.path.join(lab2,'ex')
    if not os.path.exists(dir):
        os.makedirs(dir)
    alp = os.path.join(lab2, 'alp')
    lst_res = []
    for i in range(cores[0], cores[1]+1):
        bf = BruteForce(i, krange, app_bf, encrypted, dir)
        a = bf.execute()
        lst_res.append(a)

    graphic([ i[1] for i in lst_res], [ i[0] for i in lst_res],name)


def get_normalized_range(d : str) -> list:
    krange = [1,1]
    if d:
        krange = d.split(':')
        if len(krange) != 2 or not (krange[0].isdigit() and krange[1].isdigit()):
            raise Exception('Диапазон указан неверно' )
        krange[0] = int(krange[0])
        krange[1] = int(krange[1])
    return [min(krange), max(krange)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c','--cores', dest='cores', type=str, help='Диапазон ядер в формате 1:4', required=True)
    parser.add_argument('-r','--range', dest='range',type=str, help='Диапазон ключей в формате 1000:5000', required=True)
    parser.add_argument('-e', '--encrypted', dest='encrypted', help='Файл для расшифроки', required=True)

    args = parser.parse_args()
    cores = get_normalized_range(args.cores)
    krange = get_normalized_range(args.range)
    enc = args.encrypted
    if not os.path.exists(enc):
        raise Exception('Файл не указан')
    file_len = len(get_file_data(enc))
    directory = get_cpu_info()['brand_raw']
    if not os.path.exists(directory):
        os.makedirs(directory)
    name = os.path.join(directory,'cores({0}_{1})range({2}_{3})len({4}).png'.format(cores[0],cores[1], krange[0], krange[1],file_len))
    main(krange,cores,enc, name)
    #pass