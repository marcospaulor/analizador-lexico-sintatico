# This file contains the tokens for the lexer
# Path: tokens.py
# Compare this snippet from exemplo_scanner.py:

# Reserved words in Java
reserved = {
    'class': 'CLASS',
    'public': 'PUBLIC',
    'static': 'STATIC',
    'void': 'VOID',
    # 'main': 'MAIN',
    'String': 'STRING',
    'extends': 'EXTENDS',
    'return': 'RETURN',
    'int': 'INT',
    'boolean': 'BOOLEAN',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'System': 'SYSTEM',
    'out': 'OUT',
    'println': 'PRINTLN',
    'this': 'THIS',
    'new': 'NEW',
    'true': 'TRUE',
    'false': 'FALSE',
    'import': 'IMPORT'
}

# All tokens in Java
tokens = [
    'ID', 'INT_LITERAL', 'BOOLEAN_LITERAL', 'STRING_LITERAL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUAL', 'EQUALS', 'NOT_EQUALS', 'LESS_THAN', 'LESS_THAN_OR_EQUAL', 'GREATER_THAN', 'GREATER_THAN_OR_EQUAL',
    'AND', 'OR', 'NOT',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LSQUARE', 'RSQUARE',
    'FOR', 'PRIVATE','PROTECTED', 'COMMA', 'SEMICOLON', 'DOT', 'DOUBLE_QUOTE', 'QUOTE', 'MAIN'
    
] + list(reserved.values())
