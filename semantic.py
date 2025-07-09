class SemanticError(Exception):
    pass

class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}  # nombre -> tipo
        self.functions = {}     # nombre -> (tipo_retorno, [parametros])
        self.current_function = None
        self.return_found = False

    def analyze(self, tree):
        if tree[0] != 'program':
            raise SemanticError("El AST no es un programa")
        self.visit_stmt_list(tree[1])

    def visit_stmt_list(self, stmts):
        for stmt in stmts:
            self.visit_stmt(stmt)

    def visit_stmt(self, stmt):
        if stmt[0] == 'var_decl':
            self.declare_var(stmt[1], stmt[2])
        elif stmt[0] == 'assign':
            self.visit_assign(stmt)
        elif stmt[0] == 'print':
            self.visit_expr(stmt[1])
        elif stmt[0] == 'if':
            self.visit_expr(stmt[1])
            self.visit_stmt_list(stmt[2][1])
        elif stmt[0] == 'if_else':
            self.visit_expr(stmt[1])
            self.visit_stmt_list(stmt[2][1])
            self.visit_stmt_list(stmt[3][1])
        elif stmt[0] == 'while':
            self.visit_expr(stmt[1])
            self.visit_stmt_list(stmt[2][1])
        elif stmt[0] == 'func_call':
            self.visit_func_call(stmt)
        elif stmt[0] == 'func_decl':
            self.declare_function(stmt)
        elif stmt[0] == 'return':
            if not self.current_function:
                raise SemanticError("Instrucción 'return' fuera de una función")

            tipo_esperado = self.current_function[1]
            tipo_real = self.visit_expr(stmt[1])
            self.return_found = True

            if tipo_esperado != tipo_real:
                raise SemanticError(
                    f"Tipo de retorno inválido en función '{self.current_function[0]}': "
                    f"se esperaba '{tipo_esperado}', se retornó '{tipo_real}'"
                )

    def declare_var(self, tipo, nombre):
        if nombre in self.symbol_table:
            raise SemanticError(f"Variable '{nombre}' ya declarada")
        self.symbol_table[nombre] = tipo

    def visit_assign(self, stmt):
        nombre = stmt[1]
        expr = stmt[2]
        if nombre not in self.symbol_table:
            raise SemanticError(f"Variable '{nombre}' no declarada antes de usarla")
        tipo_var = self.symbol_table[nombre]
        tipo_expr = self.visit_expr(expr)
        if tipo_var != tipo_expr:
            raise SemanticError(f"Incompatibilidad de tipos: {tipo_var} = {tipo_expr}")

    def visit_expr(self, expr):
        if expr[0] == 'binop':
            op = expr[1]
            left = self.visit_expr(expr[2])
            right = self.visit_expr(expr[3])
            if op in ['+', '-', '*', '/']:
                if left != 'int' or right != 'int':
                    raise SemanticError(f"Operación aritmética requiere enteros, pero recibió {left} y {right}")
                return 'int'
            elif op in ['==', '!=']:
                if left != right:
                    raise SemanticError(f"Comparación inválida entre {left} y {right}")
                return 'bool'
            elif op in ['<', '>']:
                if left != right:
                    raise SemanticError(f"Comparación inválida entre {left} y {right}")
                if left not in ['int', 'string']:
                    raise SemanticError(f"Comparación con operador '{op}' no soportada para tipo '{left}'")
                return 'bool'
            elif op in ['&&', '||']:
                if left != 'bool' or right != 'bool':
                    raise SemanticError(f"Operación lógica requiere booleanos, pero recibió {left} y {right}")
                return 'bool'

        elif expr[0] == 'const':
            val = expr[1]
            if isinstance(val, int):
                return 'int'
            elif isinstance(val, str):
                return 'string'
            elif isinstance(val, bool):
                return 'bool'
            elif isinstance(val, float):
                return 'float'
            else:
                if val in self.symbol_table:
                    return self.symbol_table[val]
                raise SemanticError(f"Uso de variable no declarada: {val}")

        elif expr[0] == 'func_call':
            return self.visit_func_call(expr)

        else:
            raise SemanticError("Expresión inválida")

    def declare_function(self, stmt):
        tipo_retorno = stmt[1]
        nombre = stmt[2]
        parametros = stmt[3]
        cuerpo = stmt[4]

        if nombre in self.functions:
            raise SemanticError(f"Función '{nombre}' ya fue declarada")

        self.functions[nombre] = (tipo_retorno, parametros)

        # Guardar estado anterior
        old_symbols = self.symbol_table.copy()
        old_function = self.current_function
        old_return_found = self.return_found

        # Nuevo scope de la función
        self.symbol_table = {}
        self.current_function = (nombre, tipo_retorno)
        self.return_found = False

        for tipo, nombre_param in parametros:
            self.symbol_table[nombre_param] = tipo

        self.visit_stmt_list(cuerpo[1])

        if tipo_retorno != 'void' and not self.return_found:
            raise SemanticError(f"La función '{nombre}' debe retornar un valor de tipo '{tipo_retorno}'")

        # Restaurar estado anterior
        self.symbol_table = old_symbols
        self.current_function = old_function
        self.return_found = old_return_found

    def visit_func_call(self, stmt):
        nombre_func = stmt[1]
        args = stmt[2]

        if nombre_func not in self.functions:
            raise SemanticError(f"Llamada a función '{nombre_func}' no definida")

        tipo_retorno, parametros = self.functions[nombre_func]

        if len(args) != len(parametros):
            raise SemanticError(
                f"La función '{nombre_func}' espera {len(parametros)} argumentos, pero se pasaron {len(args)}"
            )

        for i, (arg_expr, (param_tipo, param_nombre)) in enumerate(zip(args, parametros)):
            tipo_arg = self.visit_expr(arg_expr)
            if tipo_arg != param_tipo:
                raise SemanticError(
                    f"Tipo de argumento #{i+1} inválido en función '{nombre_func}': se esperaba '{param_tipo}', se recibió '{tipo_arg}'"
                )

        return tipo_retorno
