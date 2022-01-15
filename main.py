import Dictionary
import SpellChecker

if __name__ == '__main__':
    d = Dictionary.Dictionary()
    d.add('hat')
    d.add('sat')
    d.add('bat')
    print(d)
    d.remove('bat')
    print(d)
    sp = SpellChecker.SpellChecker(d)
    x = sp.most_similar('sad', 1)
    print(x)
