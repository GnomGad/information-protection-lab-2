import os.path
import multiprocessing
from brute_force import BruteForce
from app import get_file_data, write_data

import numpy as np
import matplotlib.pyplot as plt

def graphic(height, bars):
    y_pos = np.arange(len(bars))
    data = plt.bar(y_pos, height)

    data[np.argmin(height)].set_color('red')

    plt.xticks(y_pos, bars)
    plt.ylabel('сек', fontweight='bold', color = 'blue', fontsize='12')
    plt.xlabel('количество ядер', fontweight='bold', color = 'orange', fontsize='16')
    plt.show()

def main():
    cores = multiprocessing.cpu_count()
    krange = [100,999]
    lab1 = os.path.join('..\\','information-protection-lab-1')
    lab2 = os.path.join('.')
    app_bf = os.path.join(lab1, 'app.py')
    encrypted= os.path.join(lab2, 'benchmark', 'encrypted.txt')
    dir= os.path.join(lab2, 'benchmark','data')
    alp = os.path.join(lab2, 'alp')
    lst_res = []
    for i in range(1, cores+1):
        bf = BruteForce(i, krange, app_bf, encrypted, dir)
        a = bf.execute()
        lst_res.append(a)
    graphic([ i[1] for i in lst_res], [ i[0] for i in lst_res])


if __name__ == '__main__':
   main()
   #pass