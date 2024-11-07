from sympy import symbols, simplify

def modelo_tabla(numero_restricciones, numero_variables):
    

    filas = 4 + numero_restricciones
    columnas = 4 + numero_variables
    matriz = [[""] * columnas for _ in range(filas)]
    matriz[1][0]= 'Ci'
    matriz[1][1]= 'Vb'
    matriz[1][2]= 'Bi'
    matriz[0][2]= 'Cj'
    matriz[-1][1] = 'Cj-Zj' 
    matriz[1][-1] = 'Oi' 
    matriz[-2][1] = 'Zj'
    

    return matriz

""" matriz = modelo_tabla(numero_restricciones,numero_variables)
for fila in matriz:
    print(" | ".join(f"{str(elem):<5}" for elem in fila)) """

""" if __name__ == '__main__':
    modelo_tabla() """




""" 
# Definir la variable simbólica
M = symbols('M')

def operar(exp1, exp2):
    # Caso 1: Si exp1 es 0 y exp2 es -M, retornar M
    if exp1 == 0 and exp2 == -M:
        return M
    
    # Caso 2: Si exp1 es M y exp2 es M, retornar 0
    elif exp1 == M and exp2 == M:
        return 0
    
    # Caso 3: Si exp2 es 0, retornar exp1
    elif exp2 == 0:
        return exp1
    
    # Caso 4: Si exp1 es un número y exp2 es -65M, retornar la operación
    elif isinstance(exp1, (int, float)) and isinstance(exp2, (int, float)):
        return exp1 - exp2

    # En cualquier otro caso, retornar la operación de resta como string
    return f"{exp1}-{exp2}"

# Ejemplos de uso
print(operar(100, 45 * M))  # Debería mostrar: 100 - 65*M
print(operar(0, -M))        # Debería mostrar: M
print(operar(M, M))         # Debería mostrar: 0
print(operar(500, 0))       # Debería mostrar: 500
 """









from sympy import symbols, sympify

# Definir la variable simbólica
M = symbols('M')

def evaluar_fila_con_M(fila, valor_M):
    resultados = []
    for expr in fila:
        # Convertir cada elemento a expresión simbólica si es una cadena
        expr = sympify(expr)
        # Sustituir el valor de M y evaluar
        resultado = expr.subs(M, valor_M)
        resultados.append(resultado)
    return resultados

# Ejemplo de fila con expresiones
fila = ["100 - 65*M", "50 - 28*M", "210 - 90*M", "M", "0"]

# Evaluar la fila con M=50
valor_M = 50
resultados_evaluados = evaluar_fila_con_M(fila, valor_M)
print("Resultados:", resultados_evaluados)



















""" from sympy import symbols, simplify

# Definir la variable simbólica
M = symbols('M')

def operar(exp1, exp2):
    # Realizar la operación de resta entre las dos expresiones
    resultado = simplify(exp1 - exp2)
    return resultado

# Ejemplos de uso
expr1 = 100
expr2 = 65 * M
print(operar(expr1, expr2))  # Resultado esperado: 100 - 65*M

expr3 = 0
expr4 = "-M"
print(operar(expr3, expr4))  # Resultado esperado: M

expr5 = M
expr6 = M
print(operar(expr5, expr6))  # Resultado esperado: 0

expr7 = 500
expr8 = 0
print(operar(expr7, expr8))  # Resultado esperado: 500



 """



""" from sympy import symbols, simplify

# Define la variable simbólica
M = symbols('M')

def simplificar_expresion(terminos):
    # Construye la expresión a partir del arreglo de términos
    expr = 0  # Inicia la expresión en cero
    for a, b in terminos:
        # Convierte `b` en el símbolo `M` si es una cadena 'M'
        if b == 'M':
            b = M  # Asigna el símbolo M
        # Añade el término `a * b` a la expresión
        expr += a * b

    # Aplica la simplificación según las reglas
    if isinstance(expr, (int, float)):
        return expr  # Retorna el número directamente
    elif all(term.has(M) for term in expr.as_ordered_terms()):  
        # Simplificar términos con M si todos los términos lo tienen
        return simplify(expr)
    elif any(term.has(M) for term in expr.as_ordered_terms()):
        # Mantener la expresión sin simplificar si no todos los términos tienen M
        return expr
    else:
        # Simplificar si todos son numéricos
        return expr.evalf()

# Ejemplos de arreglos:
terminos1 = [(1000,'M'), ( 500,'M')]  # Equivalente a (5 * M) + (3 * M)
terminos2 = [(4, 'M'), (5, 1)]    # Equivalente a (4 * M) + 5
terminos3 = [(5, 0), (4, 1)]      # Equivalente a (5 * 0) + (4 * 1)

print(simplificar_expresion(terminos1))  # Debería mostrar 8*M
print(simplificar_expresion(terminos2))  # Debería mostrar 4*M + 5
print(simplificar_expresion(terminos3))  # Debería mostrar 4 """

































 



# Define la variable simbólica
""" M = symbols('M')

def simplificar_expresion(expr):
    # Verifica si la expresión es un número
    if isinstance(expr, (int, float)):
        return expr  # Retorna el número directamente
    elif all(term.has(M) for term in expr.as_ordered_terms()):  
        # Simplificar términos con M si todos los términos lo tienen
        return simplify(expr)
    elif any(term.has(M) for term in expr.as_ordered_terms()):
        # Mantener la expresión sin simplificar si no todos los términos tienen M
        return expr
    else:
        # Simplificar si todos son numéricos
        return expr.evalf()

# Ejemplos:
expr1 = 1000 * M + 500 * M
expr2 = 5 + (4 * M) 
expr3 = (5 * 0) + (4 * 1)

print(simplificar_expresion(expr1))  # Debería mostrar 8*M
print(simplificar_expresion(expr2))  # Debería mostrar 4*M + 5
print(simplificar_expresion(expr3))  # Debería mostrar 4 """
