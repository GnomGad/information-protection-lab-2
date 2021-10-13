import os.path
import collections
from symbol_analyzer import SymbolAnalyzer
from app import get_file_data, write_data
path_lab1 = '../information-protection-lab-1'
sa = SymbolAnalyzer()

def exp_1(): #не сработало
    data = get_file_data('e.data')
    # два алфавита
    freq_alp = sa.get_alphabet(sa.read('freq.json'))
    enc_freq = sa.get_alphabet(sa.get_frequency_analyse(sa.get_symbols_frequency(data)))
    new_list = []
    for c in enc_freq:
        if c in freq_alp:
            new_list.append(c)
    new_data = data
    for i in range(len(freq_alp)):
        new_data = new_data.replace(freq_alp[i],new_list[i])
    write_data('out.txt', new_data)

    print(freq_alp,'\n')
    print(new_list)


if __name__ == "__main__":
    data = get_file_data('e.data')
    # два алфавита
    freq_alp = sa.get_alphabet(sa.read('freq.json'))
    enc_freq = sa.get_alphabet(sa.get_frequency_analyse(sa.get_symbols_frequency(data)))
    new_list = []
    for c in freq_alp:
        if c in enc_freq:
            new_list.append(c)
    new_data = data
    for i in range(len(new_list)):
        new_data = new_data.replace(freq_alp[i],new_list[i])
    write_data('out.txt', new_data)

    print(freq_alp,'\n')
    print(new_list)
    