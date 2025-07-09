import ply.yacc as yacc
from lexer import tokens

# -----------------------------
# Reglas de precedencia
# -----------------------------
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQ', 'NEQ'),
    ('left', 'LT', 'GT'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

# -----------------------------
# Reglas de la gramática
# -----------------------------

def p_program(p):
    '''program : stmt_list'''
    p[0] = ('program', p[1])

def p_stmt_list(p):
    '''stmt_list : stmt stmt_list
                 | empty'''
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []

def p_stmt(p):
    '''stmt : var_decl
            | assign_stmt
            | if_stmt
            | while_stmt
            | print_stmt
            | func_call
            | func_decl
            | return_stmt'''
    p[0] = p[1]

def p_var_decl(p):
    '''var_decl : INT ID SEMI
                | STRING_TYPE ID SEMI
                | BOOL_TYPE ID SEMI'''
    p[0] = ('var_decl', p[1], p[2])

def p_assign_stmt(p):
    '''assign_stmt : ID EQUALS expr SEMI'''
    p[0] = ('assign', p[1], p[3])

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expr RPAREN block
               | IF LPAREN expr RPAREN block ELSE block'''
    if len(p) == 6:
        p[0] = ('if', p[3], p[5], None)
    else:
        p[0] = ('if_else', p[3], p[5], p[7])

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN expr RPAREN block'''
    p[0] = ('while', p[3], p[5])

def p_print_stmt(p):
    '''print_stmt : PRINT LPAREN expr RPAREN SEMI'''
    p[0] = ('print', p[3])

def p_func_call(p):
    '''func_call : ID LPAREN args RPAREN SEMI'''
    p[0] = ('func_call', p[1], p[3])

def p_func_decl(p):
    '''func_decl : type ID LPAREN params RPAREN block'''
    p[0] = ('func_decl', p[1], p[2], p[4], p[6])

def p_return_stmt(p):
    '''return_stmt : RETURN expr SEMI'''
    p[0] = ('return', p[1])

def p_block(p):
    '''block : LBRACE stmt_list RBRACE'''
    p[0] = ('block', p[2])

def p_args(p):
    '''args : expr COMMA args
            | expr
            | empty'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_params(p):
    '''params : param COMMA params
              | param
              | empty'''
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2 and p[1] is not None:
        p[0] = [p[1]]
    else:
        p[0] = []

def p_param(p):
    '''param : type ID'''
    p[0] = (p[1], p[2])

def p_type(p):
    '''type : INT
            | STRING_TYPE
            | BOOL_TYPE'''
    p[0] = p[1]

def p_expr_binop(p):
    '''expr : expr PLUS expr
            | expr MINUS expr
            | expr TIMES expr
            | expr DIVIDE expr
            | expr EQ expr
            | expr NEQ expr
            | expr LT expr
            | expr GT expr
            | expr AND expr
            | expr OR expr'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_expr_group(p):
    '''expr : LPAREN expr RPAREN'''
    p[0] = p[2]

def p_expr_value(p):
    '''expr : NUMBER
            | STRING
            | TRUE
            | FALSE
            | ID'''
    p[0] = ('const', p[1])

def p_empty(p):
    '''empty :'''
    pass

def p_error(p):
    if p:
        print(f"Error de sintaxis en token '{p.value}' en la línea {p.lineno}")
    else:
        print("Error de sintaxis al final del archivo")

# Crear parser
parser = yacc.yacc()
