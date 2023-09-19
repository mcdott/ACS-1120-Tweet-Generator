import re
import sys

class TextTokenizer:
    def __init__(self, text=""):
        self.text = text

    def tokenize(self):
        no_punc_text = self.remove_punctuation()
        tokens = self.split_on_whitespace(no_punc_text)
        return tokens

    def remove_punctuation(self):
        no_punc_text = re.sub('[,.()]', '', self.text)
        no_punc_text = re.sub('--', ' ', no_punc_text)
        return no_punc_text

    def split_on_whitespace(self, text):
        return re.split('\s+', text)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        source = open(filename).read()
        tokenizer = TextTokenizer(source)
        tokens = tokenizer.tokenize()
        print(tokens)
    else:
        print('No source text filename given as argument')