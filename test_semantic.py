from parser_module import parser
from semantic import SemanticAnalyzer, SemanticError
from pprint import pprint
import os

# ===============================
#      ANALIZADOR SEMÁNTICO
# ===============================

print("=" * 40)
print("  ANALIZADOR LÉXICO, SINTÁCTICO Y SEMÁNTICO")
print("=" * 40)
print()

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
#
# int x;
# x = sumar(5, 10);
# '''

# ----------------------------------------------

print(" Analizando sintaxis...\n")

try:
    ast = parser.parse(code)

    print(" Árbol de análisis sintáctico generado correctamente.\n")
    print(" AST generado:")
    print("-" * 40)
    pprint(ast, width=120)
    print("-" * 40)

    print("\n Ejecutando análisis semántico...\n")
    analyzer = SemanticAnalyzer()
    analyzer.analyze(ast)

    print(" Análisis semántico exitoso. No se encontraron errores.\n")

except SemanticError as e:
    print(" Error semántico:", e)

except Exception as ex:
    print(" Error general:", ex)

# Final
print("=" * 40)
print("  PROCESO FINALIZADO")
print("=" * 40)

input("\nPresiona Enter para salir...")
