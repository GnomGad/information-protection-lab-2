import os.path
import collections

path_lab1 = '../information-protection-lab-1'


if __name__ == "__main__":
    lines = []
    summ = 0
    with open('chars', 'r')as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if (i+1) % 2 != 0:
            continue
        
        for num in lines[i].replace(',','.').split(' '):
            summ += float(num)
    
    print(summ)

    print(os.path.exists(path_lab1))
    