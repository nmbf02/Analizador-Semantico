from parser_module import parser
from pprint import pprint

# Código fuente de ejemplo
code = '''
int x;
string nombre;
x = 10 + 5 * 2;
nombre = "Nathaly";

if (x > 10) {
    print(nombre);
} else {
    print("Pequeño");
}

while (x > 0) {
    x = x - 1;
}
'''

# Parsear el código y generar el AST
result = parser.parse(code)

# Mostrar el árbol de análisis sintáctico (AST)
print("Árbol de análisis sintáctico:")
pprint(result, width=120)
