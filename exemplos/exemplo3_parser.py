# This file analyze a .java file and create a parse tree.

import ply.yacc as yacc
import tokens as tk
import Scanner as sc

class Parser:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.parser = yacc.yacc(module=self)
        self.parser.parse(self.file)

    def p_java_file(self, p):
        '''
            java_file : class_list
        '''
        p[0] = p[1]

    def p_class_list(self, p):
        '''
            class_list : class_list class
                        | class
        '''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_class(self, p):
        '''
            class : class_access_modifier class_type IDENTIFIER block
                    
        '''
        p[0] = {'type': 'class', 'name': p[2], 'body': p[4]}

    def p_class_access_modifier(self, p):
        '''
            class_access_modifier : PUBLIC
                                | PRIVATE
                                | PROTECTED
                                | empty
                                | class_access_modifier STATIC
        '''
        p[0] = p[1]

    def p_identifier(self, p):
        '''
            identifier : IDENTIFIER
        '''
        p[0] = p[1]

    def p_class_type(self, p):
        '''
            class_type : CLASS
                        | INTERFACE
        '''
        p[0] = p[1]

    def p_primitive_type(self, p):
        '''
            primitive_type : INT
                            | FLOAT
                            | DOUBLE
                            | BOOLEAN
                            | CHAR
                            | STRING
                            | VOID
                            | BYTE
                            | SHORT
                            | LONG
                            | identifier
        '''
        p[0] = p[1]
    
    def p_type(self, p):
        '''
            type : primitive_type
                | IDENTIFIER
        '''
        p[0] = p[1]

    def p_class_body(self, p):
        '''
            class_body : class_body class_member
                        | class_member
        '''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    def p_class_member(self, p):
        '''
            class_member : field
                        | method
        '''
        p[0] = p[1]

    def p_field(self, p):
        '''
            field : type IDENTIFIER SEMICOLON
        '''
        p[0] = {'type': 'field', 'name': p[2], 'datatype': p[1]}

    def p_method(self, p):
        '''
            method : type IDENTIFIER LEFT_PAREN parameter_list RIGHT_PAREN block
        '''
        p[0] = {'type': 'method', 'name': p[2], 'datatype': p[1], 'parameters': p[4], 'body': p[6]}


    def p_parameter_list(self, p):
        '''
            parameter_list : parameter_list COMMA parameter
                            | parameter
                            | empty
        '''
        if len(p) == 4:
            p[0] = p[1] + p[3]
        else:
            p[0] = p[1]

    def p_parameter(self, p):
        '''
            parameter : type IDENTIFIER
        '''
        p[0] = {'type': 'parameter', 'name': p[2], 'datatype': p[1]}

    def p_block(self, p):
        '''
            block : LEFT_BRACE block_body RIGHT_BRACE
        '''
        p[0] = p[2]

    def p_block_body(self, p):
        '''
            block_body : block_body statement
                        | class
                        | method
                        | field
                        | statement
                        | empty
        '''
        if len(p) == 3:
            p[0] = p[1] + p[2]
        else:
            p[0] = p[1]

    
        
    def p_statement(self, p):
        '''
            statement : local_variable_declaration_statement
                        | statement_expression
                        | if_statement
                        | while_statement
                        | return_statement
                        | class
                        | block
        '''
        p[0] = p[1]

    def p_local_variable_declaration_statement(self, p):
        '''
            local_variable_declaration_statement : VAR type IDENTIFIER SEMICOLON
                                                 | type IDENTIFIER SEMICOLON
        '''
        p[0] = {'type': 'local_variable_declaration', 'name': p[3], 'datatype': p[2]}

    def p_statement_expression(self, p):
        '''
            statement_expression : expression SEMICOLON
        '''
        p[0] = {'type': 'statement_expression', 'expression': p[1]}

    def p_if_statement(self, p):
        '''
            if_statement : IF LEFT_PAREN expression RIGHT_PAREN statement
        '''
        p[0] = {'type': 'if_statement', 'condition': p[3], 'body': p[5]}

    def p_while_statement(self, p):
        '''
            while_statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement
        '''
        p[0] = {'type': 'while_statement', 'condition': p[3], 'body': p[5]}

    def p_return_statement(self, p):
        '''
            return_statement : RETURN expression SEMICOLON
        '''
        p[0] = {'type': 'return_statement', 'expression': p[2]}

    def p_expression(self, p):
        '''
            expression : expression PLUS term
                        | expression MINUS term
                        | term
        '''
        if len(p) == 4:
            p[0] = {'type': 'expression', 'left': p[1], 'operator': p[2], 'right': p[3]}
        else:
            p[0] = p[1]

    def p_term(self, p):
        '''
            term : term TIMES factor
                | term DIVIDE factor
                | factor
        '''
        if len(p) == 4:
            p[0] = {'type': 'term', 'left': p[1], 'operator': p[2], 'right': p[3]}
        else:
            p[0] = p[1]
        
    def p_factor(self, p):
        '''
            factor : LEFT_PAREN expression RIGHT_PAREN
                    | IDENTIFIER
                    | INTEGER
        '''
        if len(p) == 4:
            p[0] = p[2]
        else:
            p[0] = p[1]

    def p_empty(self, p):
        '''
            empty :
        '''
        p[0] = []

    def p_error(self, p):
        if p:
            print("Syntax error at '%s'" % p.value)
        else:
            print("Syntax error at EOF")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data, debug=0):
        self.parser.parse(data, debug=debug)

        
        
