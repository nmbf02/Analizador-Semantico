import ply.lex as lex

# Lista de tokens
tokens = [
    'ID', 'NUMBER', 'STRING', 'BOOL',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'EQUALS', 'EQ', 'NEQ', 'LT', 'GT', 'AND', 'OR',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COMMA'
]

# Palabras reservadas
reserved = {
    'int': 'INT',
    'string': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
    'true': 'TRUE',
    'false': 'FALSE',
    'return': 'RETURN'
}

tokens += list(reserved.values())

# Expresiones regulares
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_EQ      = r'=='
t_NEQ     = r'!='
t_LT      = r'<'
t_GT      = r'>'
t_AND     = r'&&'
t_OR      = r'\|\|'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

# Ignorar espacios y tabs
t_ignore  = ' \t'

# Tokens complejos
def t_BOOL(t):
    r'true|false'
    t.value = True if t.value == 'true' else False
    return t

def t_STRING(t):
    r'\".*?\"'
    t.value = t.value[1:-1]  # quitar comillas
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  # palabra reservada o ID
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_comment(t):
    r'\#.*'
    pass

def t_error(t):
    print(f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}")
    t.lexer.skip(1)

# Crear el lexer
lexer = lex.lex()
