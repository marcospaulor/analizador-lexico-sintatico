# Parser is a syntactic analyzer, not a lexical analyzer. The lexical analyzer is Scanner.py. The lexical analyzer is the one that creates the tokens. The syntactic analyzer is the one that uses the tokens to create the parse tree. This parser is used to create the parse tree. The parse tree is the one that is used to create the abstract syntax tree. The abstract syntax tree is the one that is used to create the intermediate code. The intermediate code is the one that is used to create the assembly code. The assembly code is the one that is used to create the machine code. The machine code is the one that is used to create the executable file. The executable file is the one that is used to run the program.

import ply.yacc as yacc
import tokens as tk
import Scanner as sc

class Parser:
    def __init__(self, file):
        self.file = file
        self.tokens = tk.tokens
        self.reserved = tk.reserved
        self.scanner = sc.Scanner(self.file)
        self.parser = yacc.yacc(module=self)
        self.parser.parse(self.file)
        print("Parser initialized")

    def p_java_file(self, p):
        '''java_file : class_declaration'''
        print("java_file")

    def p_program(self, p):
        '''program : package_declaration import_declarations type_declarations'''
        print("program")
    
    def p_package_declaration(self, p):
        '''package_declaration : PACKAGE qualified_identifier SEMICOLON'''
        print("package_declaration")

    def p_qualified_identifier(self, p):
        '''qualified_identifier : IDENTIFIER
                                | qualified_identifier DOT IDENTIFIER'''
        print("qualified_identifier")

    def p_import_declarations(self, p):
        '''import_declarations : import_declaration
                               | import_declarations import_declaration'''
        print("import_declarations")

    def p_import_declaration(self, p):
        '''import_declaration : IMPORT qualified_identifier SEMICOLON'''
        print("import_declaration")

    def p_type_declarations(self, p):
        '''type_declarations : type_declaration
                             | type_declarations type_declaration'''
        print("type_declarations")

    def p_primitive_type(self, p):
        '''primitive_type : BOOLEAN
                          | CHAR
                          | BYTE
                          | SHORT
                          | INT
                          | LONG
                          | FLOAT
                          | DOUBLE'''
        print("primitive_type")

    def p_type_declaration(self, p):
        '''type_declaration : class_declaration
                            | interface_declaration'''
        print("type_declaration")

    def p_reference_type(self, p):
        '''reference_type : class_or_interface_type
                          | array_type'''
        print("reference_type")

    def p_class(self, p):
        '''class : CLASS'''
        print("class")

    def p_class_modifier(self, p):
        '''class_modifier : PUBLIC
                          | PROTECTED
                          | PRIVATE
                          | ABSTRACT
                          | STATIC
                          | FINAL
                          | STRICTFP'''
        print("class_modifier")

    def p_class_declaration(self, p):
        '''class_declaration : class_modifier CLASS IDENTIFIER class_body'''
        print("class_declaration")

    def p_class_type(self, p):
        '''class_type : class_or_interface_type'''
        print("class_type")

    def p_class_body(self, p):
        '''class_body : LEFT_BRACE class_body_declarations RIGHT_BRACE'''
        print("class_body")

    def p_class_body_declarations(self, p):
        '''class_body_declarations : class_body_declaration
                                   | class_body_declarations class_body_declaration'''
        print("class_body_declarations")

    def p_class_body_declaration(self, p):
        '''class_body_declaration : class_member_declaration
                                  | static_initializer
                                  | constructor_declaration'''
        print("class_body_declaration")

    def p_class_member_declaration(self, p):
        '''class_member_declaration : field_declaration
                                    | method_declaration'''
        print("class_member_declaration")

    def p_class_or_interface_type(self, p):
        '''class_or_interface_type : IDENTIFIER
                                   | class_or_interface_type DOT IDENTIFIER'''
        print("class_or_interface_type")

    def p_field_declaration(self, p):
        '''field_declaration : field_modifier TYPE variable_declarators SEMICOLON'''
        print("field_declaration")

    def p_field_modifier(self, p):
        '''field_modifier : PUBLIC
                          | PROTECTED
                          | PRIVATE
                          | STATIC
                          | FINAL
                          | TRANSIENT
                          | VOLATILE'''
        print("field_modifier")

    def p_variable_declarators(self, p):
        '''variable_declarators : variable_declarator
                                | variable_declarators COMMA variable_declarator'''
        print("variable_declarators")

    def p_variable_declarator(self, p):
        '''variable_declarator : IDENTIFIER
                               | IDENTIFIER ASSIGN variable_initializer'''
        print("variable_declarator")

    def p_variable_initializer(self, p):
        '''variable_initializer : expression
                                | array_initializer'''
        print("variable_initializer")

    def p_array_initializer(self, p):
        '''array_initializer : LEFT_BRACE variable_initializers RIGHT_BRACE'''
        print("array_initializer")

    def p_variable_initializers(self, p):
        '''variable_initializers : variable_initializer
                                 | variable_initializers COMMA variable_initializer'''
        print("variable_initializers")

    def p_method_declaration(self, p):
        '''method_declaration : method_header method_body'''
        print("method_declaration")

    def p_method_header(self, p):
        '''method_header : method_modifier TYPE IDENTIFIER formal_parameter_list method_throws'''
        print("method_header")

    def p_method_modifier(self, p):
        '''method_modifier : PUBLIC
                           | PROTECTED
                           | PRIVATE
                           | STATIC
                           | ABSTRACT
                           | FINAL
                           | SYNCHRONIZED
                           | NATIVE
                           | STRICTFP'''
        print("method_modifier")

    def p_formal_parameter_list(self, p):
        '''formal_parameter_list : LEFT_PAREN formal_parameters RIGHT_PAREN'''
        print("formal_parameter_list")

    def p_formal_parameters(self, p):
        '''formal_parameters : formal_parameter
                             | formal_parameters COMMA formal_parameter'''
        print("formal_parameters")

    def p_formal_parameter(self, p):
        '''formal_parameter : TYPE variable_declarator_id'''
        print("formal_parameter")

    def p_variable_declarator_id(self, p):
        '''variable_declarator_id : IDENTIFIER'''
        print("variable_declarator_id")

    def p_method_throws(self, p):
        '''method_throws : THROWS qualified_identifier_list
                         | empty'''
        print("method_throws")

    def p_qualified_identifier_list(self, p):
        '''qualified_identifier_list : qualified_identifier
                                     | qualified_identifier_list COMMA qualified_identifier'''
        print("qualified_identifier_list")

    def p_method_body(self, p):
        '''method_body : block
                       | SEMICOLON'''
        print("method_body")

    def p_static_initializer(self, p):
        '''static_initializer : STATIC block'''
        print("static_initializer")

    def p_constructor_declaration(self, p):
        '''constructor_declaration : constructor_header constructor_body'''
        print("constructor_declaration")

    def p_constructor_header(self, p):
        '''constructor_header : constructor_modifier IDENTIFIER formal_parameter_list constructor_throws'''
        print("constructor_header")

    def p_constructor_modifier(self, p):
        '''constructor_modifier : PUBLIC
                                | PROTECTED
                                | PRIVATE'''
        print("constructor_modifier")

    def p_constructor_throws(self, p):
        '''constructor_throws : THROWS qualified_identifier_list
                              | empty'''
        print("constructor_throws")

    def p_constructor_body(self, p):
        '''constructor_body : block'''
        print("constructor_body")

    def p_interface_declaration(self, p):
        '''interface_declaration : INTERFACE IDENTIFIER interface_body'''
        print("interface_declaration")

    def p_interface_body(self, p):
        '''interface_body : LEFT_BRACE interface_member_declarations RIGHT_BRACE'''
        print("interface_body")

    def p_interface_member_declarations(self, p):
        '''interface_member_declarations : interface_member_declaration
                                         | interface_member_declarations interface_member_declaration'''
        print("interface_member_declarations")

    def p_interface_member_declaration(self, p):
        '''interface_member_declaration : field_declaration
                                         | method_header SEMICOLON'''
        print("interface_member_declaration")

    def p_block(self, p):
        '''block : LEFT_BRACE block_statements RIGHT_BRACE'''
        print("block")

    def p_block_statements(self, p):
        '''block_statements : block_statement
                            | block_statements block_statement'''
        print("block_statements")

    def p_block_statement(self, p):
        '''block_statement : local_variable_declaration_statement
                           | statement'''
        print("block_statement")

    def p_local_variable_declaration_statement(self, p):
        '''local_variable_declaration_statement : local_variable_declaration SEMICOLON'''
        print("local_variable_declaration_statement")

    def p_local_variable_declaration(self, p):
        '''local_variable_declaration : TYPE variable_declarators'''
        print("local_variable_declaration")

    def p_statement(self, p):
        '''statement : statement_without_trailing_substatement
                     | labeled_statement
                     | if_then_statement
                     | if_then_else_statement
                     | while_statement
                     | for_statement'''
        print("statement")

    def p_statement_without_trailing_substatement(self, p):
        """
        statement_without_trailing_substatement : expression_statement
                                                | declaration_statement
                                                | empty_statement
                                                | labeled_statement
                                                | assert_statement
                                                | return_statement
                                                | throw_statement
                                                | break_statement
                                                | continue_statement
        """
        p[0] = p[1]
        print("statement_without_trailing_substatement")

    def p_expression_statement(self, p):
        '''expression_statement : statement_expression SEMICOLON'''
        print("expression_statement")

    def p_statement_expression(self, p):
        '''statement_expression : assignment
                                | pre_increment_expression
                                | pre_decrement_expression
                                | post_increment_expression
                                | post_decrement_expression
                                | method_invocation
                                | class_instance_creation_expression'''
        print("statement_expression")

    def p_declaration_statement(self, p):
        '''declaration_statement : local_variable_declaration'''
        print("declaration_statement")

    def p_empty_statement(self, p):
        '''empty_statement : SEMICOLON'''
        print("empty_statement")

    def p_labeled_statement(self, p):
        '''labeled_statement : IDENTIFIER COLON statement'''
        print("labeled_statement")

    def p_assert_statement(self, p):
        '''assert_statement : ASSERT expression SEMICOLON
                            | ASSERT expression COLON expression SEMICOLON'''
        print("assert_statement")

    def p_return_statement(self, p):
        '''return_statement : RETURN expression SEMICOLON
                            | RETURN SEMICOLON'''
        print("return_statement")

    def p_throw_statement(self, p):
        '''throw_statement : THROW expression SEMICOLON'''
        print("throw_statement")

    def p_break_statement(self, p):
        '''break_statement : BREAK IDENTIFIER SEMICOLON
                           | BREAK SEMICOLON'''
        print("break_statement")

    def p_continue_statement(self, p):
        '''continue_statement : CONTINUE IDENTIFIER SEMICOLON
                              | CONTINUE SEMICOLON'''
        print("continue_statement")

    def p_if_then_statement(self, p):
        '''if_then_statement : IF LEFT_PAREN expression RIGHT_PAREN statement'''
        print("if_then_statement")

    def p_if_then_else_statement(self, p):
        '''if_then_else_statement : IF LEFT_PAREN expression RIGHT_PAREN statement_no_short_if ELSE statement'''
        print("if_then_else_statement")

    def p_statement_no_short_if(self, p):
        '''statement_no_short_if : statement_without_trailing_substatement
                                 | if_then_else_statement_no_short_if'''
        print("statement_no_short_if")

    def p_if_then_else_statement_no_short_if(self, p):
        '''if_then_else_statement_no_short_if : IF LEFT_PAREN expression RIGHT_PAREN statement_no_short_if ELSE statement_no_short_if'''
        print("if_then_else_statement_no_short_if")

    def p_while_statement(self, p):
        '''while_statement : WHILE LEFT_PAREN expression RIGHT_PAREN statement'''
        print("while_statement")

    def p_for_statement(self, p):
        '''for_statement : basic_for_statement
                         | enhanced_for_statement'''
        print("for_statement")

    def p_basic_for_statement(self, p):
        '''basic_for_statement : FOR LEFT_PAREN for_init_opt SEMICOLON expression_opt SEMICOLON for_update_opt RIGHT_PAREN statement'''
        print("basic_for_statement")

    def p_for_init_opt(self, p):
        '''for_init_opt : for_init
                        | empty'''
        print("for_init_opt")

    def p_for_init(self, p):
        '''for_init : statement_expression_list
                    | local_variable_declaration'''
        print("for_init")

    def p_for_update_opt(self, p):
        '''for_update_opt : for_update
                          | empty'''
        print("for_update_opt")

    def p_for_update(self, p):
        '''for_update : statement_expression_list'''
        print("for_update")

    def p_statement_expression_list(self, p):
        '''statement_expression_list : statement_expression
                                     | statement_expression_list COMMA statement_expression'''
        print("statement_expression_list")

    def p_enhanced_for_statement(self, p):
        '''enhanced_for_statement : FOR LEFT_PAREN TYPE IDENTIFIER COLON expression RIGHT_PAREN statement'''
        print("enhanced_for_statement")

    def p_expression_opt(self, p):
        '''expression_opt : expression
                          | empty'''
        print("expression_opt")

    def p_constant_expression(self, p):
        '''constant_expression : expression'''
        print("constant_expression")
    
    def p_expression(self, p):
        '''expression : assignment
                      | conditional_expression'''
        print("expression")

    def p_assignment(self, p):
        '''assignment : left_hand_side assignment_operator expression'''
        print("assignment")

    def p_left_hand_side(self, p):
        '''left_hand_side : field_access
                          | array_access
                          | IDENTIFIER'''
        print("left_hand_side")

    def p_assignment_operator(self, p):
        '''assignment_operator : EQ_ASSIGN
                               | TIMES_ASSIGN
                               | DIVIDE_ASSIGN
                               | MOD_ASSIGN
                               | PLUS_ASSIGN
                               | MINUS_ASSIGN
                               | LEFT_SHIFT_ASSIGN
                               | RIGHT_SHIFT_ASSIGN
                               | UNSIGNED_RIGHT_SHIFT_ASSIGN
                               | AND_ASSIGN
                               | XOR_ASSIGN
                               | OR_ASSIGN'''
        print("assignment_operator")

    def p_conditional_expression(self, p):
        '''conditional_expression : conditional_or_expression
                                  | conditional_or_expression QUESTION_MARK expression COLON conditional_expression'''
        print("conditional_expression")

    def p_conditional_or_expression(self, p):
        '''conditional_or_expression : conditional_and_expression
                                     | conditional_or_expression OR conditional_and_expression'''
        print("conditional_or_expression")

    def p_conditional_and_expression(self, p):
        '''conditional_and_expression : inclusive_or_expression
                                      | conditional_and_expression AND inclusive_or_expression'''
        print("conditional_and_expression")

    def p_inclusive_or_expression(self, p):
        '''inclusive_or_expression : exclusive_or_expression
                                   | inclusive_or_expression OR exclusive_or_expression'''
        print("inclusive_or_expression")

    def p_exclusive_or_expression(self, p):
        '''exclusive_or_expression : and_expression
                                   | exclusive_or_expression XOR and_expression'''
        print("exclusive_or_expression")

    def p_and_expression(self, p):
        '''and_expression : equality_expression
                          | and_expression AND equality_expression'''
        print("and_expression")

    def p_equality_expression(self, p):
        '''equality_expression : relational_expression
                               | equality_expression EQ relational_expression
                               | equality_expression NE relational_expression'''
        print("equality_expression")

    def p_relational_expression(self, p):
        '''relational_expression : shift_expression
                                 | relational_expression LT shift_expression
                                 | relational_expression GT shift_expression
                                 | relational_expression LE shift_expression
                                 | relational_expression GE shift_expression
                                 | relational_expression INSTANCEOF reference_type'''
        print("relational_expression")

    def p_shift_expression(self, p):
        '''shift_expression : additive_expression
                            | shift_expression LEFT_SHIFT additive_expression
                            | shift_expression RIGHT_SHIFT additive_expression
                            | shift_expression UNSIGNED_RIGHT_SHIFT additive_expression'''
        print("shift_expression")

    def p_additive_expression(self, p):
        '''additive_expression : multiplicative_expression
                               | additive_expression PLUS multiplicative_expression
                               | additive_expression MINUS multiplicative_expression'''
        print("additive_expression")

    def p_multiplicative_expression(self, p):
        '''multiplicative_expression : unary_expression
                                     | multiplicative_expression TIMES unary_expression
                                     | multiplicative_expression DIVIDE unary_expression
                                     | multiplicative_expression MOD unary_expression'''
        print("multiplicative_expression")

    def p_unary_expression(self, p):
        '''unary_expression : pre_increment_expression
                            | pre_decrement_expression
                            | unary_expression_not_plus_minus'''
        print("unary_expression")

    def p_pre_increment_expression(self, p):
        '''pre_increment_expression : PLUS_PLUS unary_expression'''
        print("pre_increment_expression")

    def p_pre_decrement_expression(self, p):
        '''pre_decrement_expression : MINUS_MINUS unary_expression'''
        print("pre_decrement_expression")

    def p_unary_expression_not_plus_minus(self, p):
        '''unary_expression_not_plus_minus : postfix_expression
                                           | PLUS unary_expression
                                           | MINUS unary_expression
                                           | unary_expression_not_plus_minus_not_minus'''
        print("unary_expression_not_plus_minus")

    def p_unary_expression_not_plus_minus_not_minus(self, p):
        '''unary_expression_not_plus_minus_not_minus : TILDE unary_expression
                                                     | NOT unary_expression
                                                     | cast_expression'''
        print("unary_expression_not_plus_minus_not_minus")

    def p_postfix_expression(self, p):
        '''postfix_expression : primary
                              | primary LEFT_BRACKET expression RIGHT_BRACKET
                              | primary DOT IDENTIFIER
                              | primary LEFT_PAREN argument_list_opt RIGHT_PAREN
                              | post_increment_expression
                              | post_decrement_expression'''
        print("postfix_expression")

    def p_post_increment_expression(self, p):
        '''post_increment_expression : postfix_expression PLUS_PLUS'''
        print("post_increment_expression")

    def p_post_decrement_expression(self, p):
        '''post_decrement_expression : postfix_expression MINUS_MINUS'''
        print("post_decrement_expression")

    def p_primary(self, p):
        '''primary : primary_no_new_array
                   | array_creation_expression'''
        print("primary")

    def p_primary_no_new_array(self, p):
        '''primary_no_new_array : literal
                                | THIS
                                | LEFT_PAREN expression RIGHT_PAREN
                                | field_access
                                | method_invocation
                                | array_access
                                | class_instance_creation_expression'''
        print("primary_no_new_array")

    def p_array_type(self, p):
        '''array_type : primitive_type dims
                      | class_or_interface_type dims'''
        print("array_type")

    def p_class_instance_creation_expression(self, p):
        '''class_instance_creation_expression : NEW class_type LEFT_PAREN argument_list_opt RIGHT_PAREN
                                              | NEW class_type LEFT_PAREN argument_list_opt RIGHT_PAREN class_body'''
        print("class_instance_creation_expression")

    def p_argument_list_opt(self, p):
        '''argument_list_opt : argument_list
                             | empty'''
        print("argument_list_opt")

    def p_argument_list(self, p):
        '''argument_list : expression
                         | argument_list COMMA expression'''
        print("argument_list")

    def p_array_creation_expression(self, p):
        '''array_creation_expression : NEW primitive_type dims array_initializer
                                     | NEW class_or_interface_type dims array_initializer
                                     | NEW primitive_type dims
                                     | NEW class_or_interface_type dims'''
        print("array_creation_expression")

    def p_dims(self, p):
        '''dims : dim
                | dims dim'''
        print("dims")

    def p_dim(self, p):
        '''dim : LEFT_BRACKET RIGHT_BRACKET'''
        print("dim")

    def p_field_access(self, p):
        '''field_access : primary DOT IDENTIFIER
                        | SUPER DOT IDENTIFIER
                        | IDENTIFIER'''
        print("field_access")

    def p_method_invocation(self, p):
        '''method_invocation : name LEFT_PAREN argument_list_opt RIGHT_PAREN
                             | primary DOT IDENTIFIER LEFT_PAREN argument_list_opt RIGHT_PAREN
                             | SUPER DOT IDENTIFIER LEFT_PAREN argument_list_opt RIGHT_PAREN'''
        print("method_invocation")

    def p_array_access(self, p):
        '''array_access : name LEFT_BRACKET expression RIGHT_BRACKET
                        | primary_no_new_array LEFT_BRACKET expression RIGHT_BRACKET'''
        print("array_access")

    def p_name(self, p):
        '''name : IDENTIFIER
                | name DOT IDENTIFIER'''
        print("name")

    def p_cast_expression(self, p):
        '''cast_expression : LEFT_PAREN primitive_type dims RIGHT_PAREN unary_expression
                           | LEFT_PAREN reference_type RIGHT_PAREN unary_expression_not_plus_minus'''
        print("cast_expression")

    def p_literal(self, p):
        '''literal : INTEGER_LITERAL
                   | FLOATING_POINT_LITERAL
                   | BOOLEAN_LITERAL
                   | CHARACTER_LITERAL
                   | STRING_LITERAL
                   | NULL_LITERAL'''
        print("literal")

    def p_empty(self, p):
        'empty :'
        pass

    # def p_error(self, p):
    #     print("Syntax error in input!")

    def p_error(self, p):
        if p:
            print("Syntax error at '%s' at line %d" % (p.value, p.lineno))
        else:
            print("Syntax error at EOF")
            
    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)

    def parse(self, data, debug=0):
        self.parser.parse(data, debug=debug)




