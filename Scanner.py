# Scanner is a lexical analyzer for the Java language. It is used to tokenize the input file and return a list of tokens.
import ply.lex as lex
import re
import tokens as tk

# Palavras reservadas da linguagem Java
class Scanner:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.lexer = lex.lex(module=self)
        self.lexer.input(self.file)

    # ignorar espaços em branco
    t_ignore = ' \t'

    # ignorar comentários
    def t_ignore_COMMENT(self, t):
        r'(/\*(.|\n)*?\*/)|(//.*)'
        pass

    # ignorar quebras de linha
    def t_ignore_NEWLINE(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # identificar tokens
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t
    
    # identificar números inteiros
    def t_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t


