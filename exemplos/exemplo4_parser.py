# This file analyze a .java file and create a parse tree.

import ply.yacc as yacc
import tokens as tk

class Parser:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.parser = yacc.yacc(module=self)
        self.parser.parse(self.file)

    # Programa
    def p_program(self, p):
        '''
        program : class_declaration_list
                | empty
        '''
        p[0] = p[1]

    # Lista de declarações de classes
    def p_class_declaration_list(self, p):
        '''
            class_declaration_list : class_declaration class_declaration_list
                                    | empty
        '''
        

    # Declaração de classe
    def p_class_declaration(self, p):
        '''
            class_declaration : class_header LEFT_BRACE var_declaration_list method_declaration_list RIGHT_BRACE
        '''
        

    # Cabeçalho de classe
    def p_class_header(self, p):
        '''
            class_header : CLASS ID extends_clause implements_clause
                        | access_modifier CLASS ID extends_clause implements_clause
        '''
        

    # Modificador de acesso
    def p_access_modifier(self, p):
        '''
            access_modifier : PUBLIC
                            | PRIVATE
                            | PROTECTED
        '''
        p[0] = p[1]

    # Extensão de classe
    def p_extends_clause(self, p):
        '''
            extends_clause : EXTENDS ID
                            | empty
        '''
        

    # Implementação de classe
    def p_implements_clause(self, p):
        '''
            implements_clause : IMPLEMENTS ID
                            | empty
        '''
        

    # Lista de declarações de variáveis
    def p_var_declaration_list(self, p):
        '''
            var_declaration_list : var_declaration var_declaration_list
                                | empty
        '''
        p[0] = p[1] or p[2]

    # Declaração de variável
    def p_var_declaration(self, p):
        '''
            var_declaration : type ID SEMICOLON
                            | type ID ASSIGN expression SEMICOLON
        '''
        # declaração de variável
        if len(p) == 4:
            p[0] = p[2] = p[4]

    # Lista de declarações de métodos
    def p_method_declaration_list(self, p):
        '''
            method_declaration_list : method_declaration method_declaration_list
                                    | empty
        '''
        p[0] = p[1] or p[2]

    # Declaração de método
    def p_method_declaration(self, p):
        '''
            method_declaration : method_header LEFT_PAREN formal_parameter_list RIGHT_PAREN method_body
            | empty
        '''
        # declaração de método
        if len(p) == 6:
            p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

    # Cabeçalho de método
    def p_method_header(self, p):
        '''
            method_header : PUBLIC STATIC type ID
                            | type ID
        '''
        # declaração de método
        if len(p) == 5:
            p[0] = p[1] + p[2] + p[3] + p[4]
        else:
            p[0] = p[1] + p[2]

    # Lista de parâmetros formais
    def p_formal_parameter_list(self, p):
        '''
            formal_parameter_list : formal_parameter formal_parameter_tail
                                    | empty
        '''
        p[0] = (p[1], p[2])

    # formal parameter tail
    def p_formal_parameter_tail(self, p):
        '''
            formal_parameter_tail : COMMA formal_parameter formal_parameter_tail
                                    | empty
        '''
        p[0] = (p[1], p[2], p[3])

    # Parâmetro formal
    def p_formal_parameter(self, p):
        '''
            formal_parameter : type ID
        '''
        p[0] = (p[1], p[2])

    # Corpo de método
    def p_method_body(self, p):
        '''
            method_body : LEFT_BRACE var_declaration_list statement_list RIGHT_BRACE
        '''
        p[0] = p[2] + p[3]

    # statement list
    def p_statement_list(self, p):
        '''
            statement_list : statement statement_list
                            | empty
        '''
        p[0] = p[1] + p[2]

    # statement
    def p_statement(self, p):
        '''
            statement : block
                    | assignment_statement
                    | if_statement
                    | while_statement
                    | print_statement
                    | expression_statement
        '''
        p[0] = p[1]

    # block
    def p_block(self, p):
        '''
            block : LEFT_BRACE statement_list RIGHT_BRACE
        '''
        p[0] = p[1] + p[2] + p[3]

    # assignment statement
    def p_assignment_statement(self, p):
        '''
            assignment_statement : ID ASSIGN expression SEMICOLON
        '''
        if p[2] == '=':
            p[0] = p[1] 

    # if statement
    def p_if_statement(self, p):
        '''
            if_statement : IF LEFT_PAREN expression RIGHT_PAREN statement else_statement
        '''
        p[0] = {'if': p[3], 'statement': p[5], 'else': p[6]}

    # else statement
    def p_else_statement(self, p):
        '''
            else_statement : ELSE statement
                            | empty
        '''
        p[0] = p[2]

    # while statement
    def p_while_statement(self, p):
        '''
            while_statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement
        '''
        p[0] = {'while': p[3], 'statement': p[5] }

    # print statement
    def p_print_statement(self, p):
        '''
            print_statement : SYSTEM DOT OUT DOT PRINTLN LEFT_PAREN expression RIGHT_PAREN SEMICOLON
        '''
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

    def p_expression_statement(self, p):
        '''
            expression_statement : expression SEMICOLON
        '''
        p[0] = p[1] + p[2]

    # expression
    def p_expression(self, p):
        '''
            expression : unary_expression
                    | assignment_expression
                    | logical_or_expression
                    | logical_and_expression
                    | equality_expression
                    | comparassion_expression
                    | additive_expression
                    | multiplicative_expression
                    | literal
                    | empty
        '''
        p[0] = p[1]

    # assignment expression
    def p_assignment_expression(self, p):
        '''
            assignment_expression : logical_or_expression ASSIGN assignment_expression
                                | logical_or_expression
                                | empty
        '''
        if p[2] == '=':
            p[0] = p[1] = p[3]
        else:
            p[0] = p[1]


   # logical or expression
    def p_logical_or_expression(self, p):
        '''
            logical_or_expression : logical_and_expression OR logical_or_expression
                                | logical_and_expression
        '''
        if p[2] == '||':
            p[0] = p[1] or p[3]
        else:
            p[0] = p[1]

    # logical and expression
    def p_logical_and_expression(self, p):
        '''
            logical_and_expression : equality_expression AND logical_and_expression
                                | equality_expression
        '''
        if p[2] == '&&':
            p[0] = p[1] and p[3]
        else:
            p[0] = p[1]

    # equality expression
    def p_equality_expression(self, p):
        '''
            equality_expression : comparassion_expression EQ comparassion_expression
                                | comparassion_expression NE comparassion_expression
                                | comparassion_expression
        '''
        if p[2] == '==':
            p[0] = p[1] == p[3]
        elif p[2] == '!=':
            p[0] = p[1] != p[3]
        else:
            p[0] = p[1]

    # comparassion expression
    def p_comparassion_expression(self, p):
        '''
            comparassion_expression : additive_expression LT additive_expression
                                    | additive_expression GT additive_expression
                                    | additive_expression LE additive_expression
                                    | additive_expression GE additive_expression
                                    | additive_expression
        '''
        if p[2] == '<':
            p[0] = p[1] < p[3]
        elif p[2] == '>':
            p[0] = p[1] > p[3]
        elif p[2] == '<=':
            p[0] = p[1] <= p[3]
        elif p[2] == '>=':
            p[0] = p[1] >= p[3]
        else:
            p[0] = p[1]

        

    # additive expression
    def p_additive_expression(self, p):
        '''
            additive_expression : additive_expression PLUS multiplicative_expression
                                | additive_expression MINUS multiplicative_expression
                                | multiplicative_expression
        '''
        # se p[2] for um operador aditivo, então p[0] é uma expressão aditiva
        if p[2] in '+':
            p[0] = p[1] + p[3]
        elif p[2] in '-':
            p[0] = p[1] - p[3]
        else:
            p[0] = p[1]
        

    # multiplicative expression
    def p_multiplicative_expression(self, p):
        '''
            multiplicative_expression : multiplicative_expression TIMES unary_expression
                                    | multiplicative_expression DIVIDE unary_expression
                                    | multiplicative_expression MOD unary_expression
                                    | unary_expression
        '''
        # se p[2] for um operador multiplicativo, então p[0] é uma expressão multiplicativa
        if p[2] in '*':
            p[0] = p[1] * p[3]
        elif p[2] in '/':
            p[0] = p[1] / p[3]
        elif p[2] in '%':
            p[0] = p[1] % p[3]
        else:
            p[0] = p[1]
        

    # unary expression
    def p_unary_expression(self, p):
        '''
            unary_expression : MINUS unary_expression
                            | NOT unary_expression
                            | primary_expression
        '''
        if p[1] == '-':
            p[0] = -p[2]
        elif p[1] == '!':
            p[0] = not p[2]
        else:
            p[0] = p[1]
        

    # primary expression
    def p_primary_expression(self, p):
        '''
            primary_expression : ID
                            | literal
                            | LEFT_PAREN expression RIGHT_PAREN
        '''
        if p == '(':
            p[0] = p[2]
        else:
            p[0] = p[1]
        

    # literal
    def p_literal(self, p):
        '''
            literal : INTEGER
                    | FLOAT
                    | DOUBLE
                    | BOOLEAN
                    | STRING
                    | CHAR
                    | NULL
        '''
        p[0] = p[1]

    # type
    def p_type(self, p):
        '''
            type : INT
                | BOOLEAN
                | STRING
                | FLOAT
                | DOUBLE
                | CHAR
                | VOID
                | ID
                | type LEFT_BRACKET RIGHT_BRACKET
        '''
        if len(p) > 2:
            p[0] = p[1] + '[]'
        else:
            p[0] = p[1]
        

    # Empty production
    def p_empty(self, p):
        'empty :'
        pass
    

    # Error rule for syntax errors
    def p_error(self, p):
        if p:
            # value and line number
            print("Syntax error at '%s' in line %d" % (p.value, p.lineno))
            exit()
        else:
            print("Syntax error at EOF")

    # Build the parser
    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data, debug=0):
        self.parser.parse(data, debug=debug)