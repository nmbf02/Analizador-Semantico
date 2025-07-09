from parser_module import parser
from semantic import SemanticAnalyzer, SemanticError
from pprint import pprint

# Puedes comentar/descomentar el bloque que quieras probar:

# --- Ejemplo con int y string ---
# code = '''
# int x;
# string nombre;
# x = 10 + 5;
# nombre = "Nathaly";
#
# if (x > 5) {
#     print(nombre);
# } else {
#     print("Hola");
# }
#
# while (x > 0) {
#     x = x - 1;
# }
# '''

# --- Ejemplo con comparación entre strings ---
code = '''
string a;
string b;
a = "Nathaly";
b = "Zuleyka";

if (a < b) {
    print("Sí, a va antes alfabéticamente");
}
'''

# --- Ejemplo con error semántico ---
# code = '''
# int edad;
# edad = "veinte";  # Error: asignar string a int
# '''

# --- Ejemplo con función válida ---
# code = '''
# int sumar(int a, int b) {
#     return a + b;
# }

# int x;
# x = sumar(5, 10);
# '''

# ----------------------------------------------

print("Analizando sintaxis...")

try:
    ast = parser.parse(code)
    print("Árbol de análisis sintáctico generado correctamente.")
    print("AST generado:")
    pprint(ast, width=120)

    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)
    print("Análisis semántico exitoso.")

except SemanticError as e:
    print("Error semántico:", e)
except Exception as ex:
    print("Error general:", ex)

input("\nPresiona Enter para salir...")
