from lexer import lexer

# Código fuente de prueba
code = '''
int x;
string nombre;
x = 10 + 5 * 2;
nombre = "Nathaly";

if (x > 10) {
    print(nombre);
}
'''

# Enviar el código al lexer
lexer.input(code)

# Mostrar tokens uno por uno
print("🔍 Tokens encontrados:")
while True:
    tok = lexer.token()
    if not tok:
        break
    print(f"{tok.type}({tok.value}) en línea {tok.lineno}")
