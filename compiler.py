import re

class SimpleLexer(object):
    def __init__(self):
        self.token_rules = [
            ('NUMBER', r'\d+'), 
            ('PLUS', r'\+'), 
            ('MINUS', r'-'), 
            ('MULTIPLY', r'\*'), 
            ('DIVIDE', r'/'), 
            ('LPAREN', r'\('), 
            ('RPAREN', r'\)'), 
            ('WS', r'\s+')
        ]
        self.token_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.token_rules)
        # (?P<NUMBER>\d+)|(?P<PLUS>\+)|(?P<MINUS>-)|(?P<MULTIPLY>\*)|(?P<DIVIDE>/)|(?P<LPAREN>\()|(?P<RPAREN>\))|(?P<WS>\s+)
        self.re_token_regex = re.compile(self.token_regex)

    def tokenize(self, code):
        for mo in self.re_token_regex.finditer(code): 
            '''
            if the given code is '27', then the first mo would be <re.Match object; span=(0, 2), match='27'>
            '''

            kind = mo.lastgroup 
            '''
            .lastgroup is a attribute (?) of a matchObject (which is a Match[str])
            since the code MIGHT match more than ONE token (but not in this case), so we only select the last one by using lastgroup
            【The name of the last matched capturing group, or None if the group didn't have a name, or if no group was matched at all.】
                - from official Python document
            '''

            value = mo.group()
            if kind == 'NUMBER': 
                value = int (value)
            elif kind == 'WS': 
                continue
            yield kind, value
            '''
            一旦我們的程式執行到 yield 後，程式就會把值丟出，並暫時停止。
            直到下一次的遞迴，程式才會從 yield 的下一行開始執行。
            那哪裡有遞迴呢？沒錯，最常被用到 for 迴圈裡，而且 for 迴圈自帶 next() 的功能。
            換句話說， for 迴圈會自動在程式內部進行下一輪的遞迴，因而觸動 yield 進行下一輪吐值。
            '''

code = str(input ())  # test: '27 + (43 / 36 - 48) * 51'
lexer = SimpleLexer()
tokens = list(lexer.tokenize(code))

print (tokens)