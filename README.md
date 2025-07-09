# Analizador Semántico en Python con PLY

Este proyecto es un analizador léxico, sintáctico y semántico construido con Python usando la librería [PLY](https://www.dabeaz.com/ply/) (Python Lex-Yacc). Adicionalmente, incluye una versión con interfaz gráfica (GUI) para facilitar su uso.

---

## Estructura del Proyecto

```

Analizador-Semantico/
├── build/                   # Carpeta generada por PyInstaller
├── dist/                    # Carpeta donde se genera el ejecutable .exe
├── venv/                    # Entorno virtual (opcional)
├── lexer.py                 # Analizador léxico (tokens con PLY)
├── parser\_module.py         # Analizador sintáctico (gramática + AST)
├── semantic.py              # Analizador semántico
├── main.py                  # Consola principal del analizador
├── main\_gui.py              # Interfaz gráfica con menú interactivo
├── test\_lexer.py            # Pruebas para el lexer
├── test\_parser.py           # Pruebas para el parser
├── test\_semantic.py         # Pruebas para el análisis semántico
├── \*.spec                   # Archivos generados por PyInstaller
├── parsetab.py              # Archivo generado automáticamente por yacc
├── parser.out               # Tabla de parsing generada por PLY
└── README.md                # Este archivo

````

---

## Requisitos

- Python 3.7 o superior
- pip
- PLY

Instala las dependencias:

```bash
pip install ply
````

---

## Cómo ejecutar

### Consola principal

```bash
python main.py
```

### Interfaz gráfica (menú con opciones)

```bash
python main_gui.py
```

---

## Archivos de prueba

* `test_lexer.py`: Prueba de tokens y reconocimiento léxico.
* `test_parser.py`: Muestra el AST generado desde código de prueba.
* `test_semantic.py`: Ejecuta el análisis completo (léxico + sintaxis + semántico).

Puedes ejecutar cualquiera con:

```bash
python nombre_del_archivo.py
```

---

## Cómo generar el `.exe`

1. Instala `pyinstaller`:

```bash
pip install pyinstaller
```

2. Para crear el ejecutable de la consola principal:

```bash
pyinstaller --onefile main.py
```

3. Para la interfaz gráfica:

```bash
pyinstaller --noconsole --onefile main_gui.py
```

El archivo `.exe` estará dentro de la carpeta `dist/`.

---

## Ejemplos de código compatibles

```c
int x;
x = 10 + 5;

string nombre = "Nathaly";

if (x > 10) {
    print(nombre);
} else {
    print("Pequeño");
}
```

También se soportan funciones:

```c
int sumar(int a, int b) {
    return a + b;
}

int resultado;
resultado = sumar(5, 10);
```

---

## Autor

- Nathaly Michel Berroa Fermín
- Proyecto académico de Compiladores – UTESA
- Desarrollado con Python y PLY
