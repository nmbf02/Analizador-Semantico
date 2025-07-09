from lexer import lexer
from parser_module import parser  # renombra tu archivo si es necesario
from semantic import SemanticAnalyzer, SemanticError
from pprint import pprint

# Código de entrada (puedes reemplazarlo por lectura desde archivo si quieres)
code = '''
int sumar(int a, int b) {
    return a + b;
}

int x;
x = sumar(5, 10);
'''

# ---------------------------
# FASE 1: Análisis léxico
# ---------------------------
print(" Tokens encontrados:")
lexer.input(code)
for tok in lexer:
    print(f"{tok.type}({tok.value}) en línea {tok.lineno}")

# ---------------------------
# FASE 2: Análisis sintáctico
# ---------------------------
print("\n Analizando sintaxis...")
ast = parser.parse(code)
print("Árbol de análisis sintáctico:")
pprint(ast)

# ---------------------------
# FASE 3: Análisis semántico
# ---------------------------
print("\n Analizando semántica...")
analyzer = SemanticAnalyzer()
try:
    analyzer.analyze(ast)
    print("Análisis semántico exitoso.")
except SemanticError as e:
    print(f"Error semántico: {e}")

input("\nPresiona Enter para salir...")
