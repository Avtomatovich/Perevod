import sys
from translate import Translator

class Perevod:
        
    def _is_cyrillic(self, text):
        cyrillic_unicode = range(0x0400, 0x04FF)
        
        for char in text:
            if ord(char) in cyrillic_unicode:
                return True
            
    def convert(self, text):
        if self._is_cyrillic(text):
            translator = Translator(from_lang="ru", to_lang="en")
        else:
            translator = Translator(from_lang="en", to_lang="ru")

        return translator.translate(text)
        
def main():
    if len(sys.argv) != 2:
        print("Usage: python perevod.py <text>")
        return
    
    perevod = Perevod()
    text = sys.argv[1]
    response = perevod.convert(text)
    print(text + ":\n\t->" + response)
        
if __name__ == "__main__":
    perevod = Perevod()
    while True:
        text = input('>> ')
        if text != 'exit':
            print(perevod.convert(text))
        else:
            break
