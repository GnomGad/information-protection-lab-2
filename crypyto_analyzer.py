from symbol_analyzer import SymbolAnalyzer

class CryptoAnalyzer():
    
    def __init__(self, sa: SymbolAnalyzer):
        self.sa = sa

    def brute_force(self, text:str) -> str:
        d = self.sa.get_symbols_frequency(text)
        print(d)
        lst = self.sa.get_frequency_analyse(d)
        return lst

if __name__ == '__main__':
    ca = CryptoAnalyzer
    ca.break_notepad(enc)