'''
    This program is parser for the MiniJava language.
    It is used to parse the input file and return a list of tokens
    and the respective syntactic structure
    Where the tokens are defined in the file tokens.py
    This program is based on the ply library
'''

import ply.yacc as yacc
import tokens as tk

class Parser:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.parser = yacc.yacc(module=self)
        # self.parser.parse(self.file)
        self.tree = self.parser.parse(self.file)
        print(self.tree)
        

    # Estado inicial
    def p_program(self, p):
        '''program : class_decl_list'''
        p[0] = p[1]

    # Lista de classes
    def p_class_decl_list(self, p):
        '''class_decl_list : class_decl class_decl_list
                           | class_decl'''
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = [p[1]]

    # Declaração de classe
    def p_class_decl(self, p):
        '''
            class_decl : CLASS ID EXTENDS ID LBRACE class_body RBRACE
                       | CLASS ID LBRACE class_body RBRACE
        '''
        if len(p) == 8:
            p[0] = ('class', p[2], p[4], p[6])
        else:
            p[0] = ('class', p[2], None, p[4])

    # Corpo da classe
    def p_class_body(self, p):
        '''class_body : class_body class_member
                      | class_member'''
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = [p[1]]

    # Membros da classe
    def p_class_member(self, p):
        '''class_member : var_decl
                        '''
        p[0] = p[1]

    # Declaração de variável
    def p_var_decl(self, p):
        '''var_decl : type ID SEMICOLON'''
        p[0] = ('var', p[1], p[2])


    # Lista de declarações de variáveis
    def p_var_decl_list(self, p):
        '''var_decl_list : var_decl_list var_decl
                         | empty'''
        if len(p) == 3:
            p[0] = [p[1]] + p[2]
        else:
            p[0] = []

    

    # Tipo
    def p_type(self, p):
        '''type : LBRACKET INT RBRACKET
                | INT
                | BOOLEAN
                | ID'''
        if len(p) == 4:
            p[0] = ('array', p[2])
        else:
            p[0] = p[1]

    # empty
    def p_empty(self, p):
        '''empty :'''
        pass

    # erro
    def p_error(self, p):
        if p:
            # print value, line and column
            print("Syntax error at '%s' line %d" % (p.value, p.lineno))
        else:
            print("Syntax error at EOF")
        exit(1)

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data):
        return self.parser.parse(data)
    


    