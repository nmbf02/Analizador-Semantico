from lexer import lexer

# Código de prueba
code = '''
int x;
string nombre;
x = 10 + 5 * 2;
nombre = "Nathaly";

if (x > 10) {
    print(nombre);
}
'''

lexer.input(code)

# Mostrar tokens uno por uno
print("Tokens encontrados:")
for tok in lexer:
    print(f"{tok.type}({tok.value}) en línea {tok.lineno}")
