import tkinter as tk
from tkinter import messagebox, scrolledtext
from lexer import lexer
from parser_module import parser
from semantic import SemanticAnalyzer, SemanticError
from pprint import pformat


# --- Código de prueba base ---
DEFAULT_CODE = '''
int sumar(int a, int b) {
    return a + b;
}

int x;
x = sumar(5, 10);
'''


def run_lexer(code):
    lexer.input(code)
    output = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        output.append(f"{tok.type}({tok.value}) en línea {tok.lineno}")
    return "\n".join(output)


def run_parser(code):
    try:
        ast = parser.parse(code)
        return pformat(ast, width=80)
    except Exception as e:
        return f"Error de análisis sintáctico: {e}"


def run_semantic(code):
    try:
        ast = parser.parse(code)
        analyzer = SemanticAnalyzer()
        analyzer.analyze(ast)
        return "✅ Análisis semántico exitoso.\n\nAST:\n" + pformat(ast, width=80)
    except SemanticError as e:
        return f"❌ Error semántico: {e}"
    except Exception as e:
        return f"❌ Error general: {e}"


def execute(mode):
    code = code_input.get("1.0", tk.END)
    if not code.strip():
        messagebox.showwarning("Advertencia", "El código está vacío.")
        return

    if mode == "lexer":
        result = run_lexer(code)
    elif mode == "parser":
        result = run_parser(code)
    elif mode == "semantic":
        result = run_semantic(code)
    else:
        result = "Modo no válido."

    output_display.delete("1.0", tk.END)
    output_display.insert(tk.END, result)


# --- GUI con tkinter ---
root = tk.Tk()
root.title("Analizador Semántico de Lenguaje")

# Entrada de código
tk.Label(root, text="Código fuente:").pack()
code_input = scrolledtext.ScrolledText(root, height=15, width=100)
code_input.insert(tk.END, DEFAULT_CODE)
code_input.pack()

# Botones
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

tk.Button(btn_frame, text="Analizar con Lexer", command=lambda: execute("lexer")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Ver AST (Parser)", command=lambda: execute("parser")).pack(side=tk.LEFT, padx=5)
tk.Button(btn_frame, text="Análisis Semántico", command=lambda: execute("semantic")).pack(side=tk.LEFT, padx=5)

# Salida
tk.Label(root, text="Salida:").pack()
output_display = scrolledtext.ScrolledText(root, height=15, width=100)
output_display.pack()

# Iniciar GUI
root.mainloop()
