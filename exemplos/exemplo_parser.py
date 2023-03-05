import ply.yacc as yacc

# Importa os tokens do lexer
from exemplo_scanner import tokens

# Regra inicial
def p_program(p):
    '''program : CLASS IDENTIFIER LBRACE main RBRACE'''

# Regra para o método main
def p_main(p):
    '''main : PUBLIC STATIC VOID IDENTIFIER LPAREN STRING LBRACKET RBRACKET IDENTIFIER RPAREN LBRACE statements RBRACE'''

# Regra para uma lista de statements
def p_statements(p):
    '''statements : statement
                  | statements statement'''

# Regra para um statement
def p_statement(p):
    '''statement : expression_statement
                 | block'''

# Regra para um expression statement
def p_expression_statement(p):
    '''expression_statement : expression SEMICOLON'''

# Regra para um bloco de statements
def p_block(p):
    '''block : LBRACE statements RBRACE'''

# Regra para uma expressão
def p_expression(p):
    '''expression : IDENTIFIER ASSIGN expression
                  | IDENTIFIER'''

# Constrói o parser
parser = yacc.yacc()

# Teste do parser
data = '''
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }
}
'''

result = parser.parse(data)

if result is not None:
    print('Programa válido!')