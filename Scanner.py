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
        # verificar se é palavra reservada
        if(t.value in self.reserved):
            t.type = self.reserved[t.value]
        else:
            # verifica se é um token válido
            if(t.value in self.tokens):
                t.type = t.value
            else:
                t.type = 'ID'
        return t
    
    # identificar números inteiros
    def t_INT_LITERAL(self, t):
        r'\d+'
        t.value = int(t.value)
        return t
    
    def t_STRING_LITERAL(self, t):
        r'\".*?\"'
        t.value = t.value[1:-1]
        return t

    # identificar números reais
    def t_FLOAT_LITERAL(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t
    
    #  identificar booleanos
    def t_BOOLEAN_LITERAL(self, t): 
        r'(true|false)'
        t.value = True if t.value == 'true' else False
        return t

    # Print caractere e tokens analisados
    def printTokens(self):
        while True:
            tok = self.lexer.token()
            if not tok: break
            print(tok)

    def t_error(self, t):
        # chamada de erro mostrando caractere e linha
        print("Illegal character '%s' at line %d" % (t.value[0], t.lexer.lineno))
        t.lexer.skip(1)
        exit()

    # Regular expression rules for simple tokens
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_EQUAL = r'='
    t_EQUALS = r'=='
    t_NOT_EQUALS = r'!='
    t_LESS_THAN = r'<'
    t_LESS_THAN_OR_EQUAL = r'<='
    t_GREATER_THAN = r'>'
    t_GREATER_THAN_OR_EQUAL = r'>='
    t_AND = r'&&'
    t_OR = r'\|\|'
    t_NOT = r'!'
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_LSQUARE = r'\['
    t_RSQUARE = r'\]'
    t_COMMA = r','
    t_SEMICOLON = r';'
    t_DOT = r'\.'
    t_PLUS_PLUS = r'\+\+'
    t_MINUS_MINUS = r'--'
    t_TRUE = r'true'
    t_FALSE = r'false'