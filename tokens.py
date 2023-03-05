# This file contains the tokens for the lexer
# Path: tokens.py
# Compare this snippet from exemplo_scanner.py:

# Reserved words in Java
reserved = {'boolean', 'class', 'else', 'extends', 'false', 'if', 'int', 'length', 'main', 'new', 'public', 'return', 'static', 'String', 'System.out.println', 'this', 'true', 'void', 'while'}


# All tokens in Java
tokens = [
    'ID', 'INT_LITERAL', 'BOOLEAN_LITERAL', 'STRING_LITERAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL', 'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQUARE', 'RSQUARE',
    'IF', 'ELSE', 'WHILE', 'FOR', 'RETURN',
    'PUBLIC', 'PRIVATE', 'STATIC', 'VOID', 'MAIN', 'CLASS', 'EXTENDS', 'THIS', 'NEW',
    'TRUE', 'FALSE'
] + list(reserved.values())

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
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_FOR = r'for'
t_RETURN = r'return'
t_PUBLIC = r'public'
t_PRIVATE = r'private'
t_STATIC = r'static'
t_VOID = r'void'
t_MAIN = r'main'
t_CLASS = r'class'
t_EXTENDS = r'extends'
t_THIS = r'this'
t_NEW = r'new'
t_TRUE = r'true'
t_FALSE = r'false'
