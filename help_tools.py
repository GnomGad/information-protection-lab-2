from symbol_analyzer import SymbolAnalyzer

def get_dict(file:str) -> dict:
    symbols = []
    freq = []
    with open(file, 'r')as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if (i+1) % 2 != 0:
            symbols.extend(lines[i].replace('\n','').split(' '))
            continue
        freq.extend(lines[i].replace(',','.').replace('\n','').split(' '))
    return {symbols[i]: freq[i] for i in range(len(symbols))}

if __name__ == "__main__":
    sa = SymbolAnalyzer()
    #sa.write(get_dict('symbol_frequency_ru'),'s_ru.json')
    sa.write(sa.get_frequency_analyse(sa.read('freq.json')),'freq_real.json')