

""" def Principal():
    funcion_objetivo = input('Ingrese la función objetivo: ')
    cantida_restricciones = int(input('Ingrese la cantidad de restricciones: '))
    cantidad_variables = Calcular_cant_variables(funcion_objetivo)
    matriz = modelo_tabla(cantida_restricciones,cantidad_variables)
    resultaods = Extraer_coeficientes(funcion_objetivo,cantidad_variables)
    print(resultaods)
     fila in matriz:
        print(" | ".join(f"{str(elem):<5}" for elem in fila)) 



def Calcular_cant_variables (funcion_objetivo):

    if funcion_objetivo[0] not in ['+', '-']:
        funcion_objetivo = '+' + funcion_objetivo

    terminos = re.split(r'(?=\+|\-)', funcion_objetivo)

    variables = set()

    for termino in terminos:
        encontrados = re.findall(r'[A-Za-z]\d+', termino)
        variables.update(encontrados)

    
    cantidad_variables = len(variables)

    return cantidad_variables


    #max_min= int(input("¿Quieres maximizar o minimizar la función objetivo? ( 1 = max/ 2 = min): " ))
#funcion_objetivo = input('Ingrese la función objetivo: ')

    # Agregar un '+' al principio si no hay signo al inicio


def prueba():
    num_restricciones = int(input("Ingrese el número de restricciones: "))

    # Inicializar una lista para almacenar las restricciones
    restricciones = []

    # Bucle para pedir cada restricción
    for i in range(num_restricciones):
        restriccion = input(f"Ingrese la restricción {i + 1}: ")
        restricciones.append(restriccion)

    # Mostrar las restricciones ingresadas
    print("Las restricciones ingresadas son:")
    for i, restriccion in enumerate(restricciones, start=1):
        print(f"Restricción {i}: {restriccion}")
    
        
def Extraer_coeficientes(funcion, cantidad_variables):
    # Inicializar los coeficientes de cada variable
    coeficientes = [0] * cantidad_variables
    terminos = re.split(r'(?=\+|\-)', funcion)

    for termino in terminos:
        # Detectar si el término contiene una variable con S o M
        match = re.match(r'([+-]?\d*\.?\d*)([A-Za-z]\d*)(S|M)?', termino.strip())
        if match:
            coef, var, tipo_var = match.groups()
            indice = int(var[1:]) - 1  # Convertir X1, X2, s1, s2, etc., en índices

            # Asumir coeficiente de 1 o -1 si no está explícito
            if coef in ['', '+']:
                coef = 1
            elif coef == '-':
                coef = -1
            else:
                coef = float(coef)

            # Priorizar M sobre S en la tabla
            if tipo_var == 'M':
                coef = coef * -1  # Negativo para representar el coeficiente de M
            elif tipo_var == 'S' and coeficientes[indice] == 0:
                coef = coef * 1  # Mantiene positivo para S

            coeficientes[indice] = float(coef)

    return coeficientes

if __name__ == '__main__':
    Principal()

 

 """



from tabla import modelo_tabla
import re

def Principal():
    # Ingresar la función objetivo
    funcion_objetivo = input('Ingrese la función objetivo: ')
    
    # Ingresar la cantidad de restricciones
    cantidad_restricciones = int(input('Ingrese la cantidad de restricciones: '))
    
    # Calcular el número de variables
    cantidad_variables = Calcular_cant_variables(funcion_objetivo)
    
    # Crear la matriz inicial de la tabla simplex
    matriz = modelo_tabla(cantidad_restricciones, cantidad_variables)
    
    # Llenar la matriz con las restricciones ingresadas por el usuario
    restricciones = Pedir_restricciones(cantidad_restricciones, cantidad_variables)
    
    # Asignar restricciones a la tabla (se asume que van en las filas 2 en adelante)
    for i, restriccion in enumerate(restricciones, start=2):
        matriz[i][3:3+cantidad_variables] = restriccion[:-1]  # Coeficientes de las variables
        matriz[i][2] = restriccion[-1]  # El término independiente (b)
    
    # Mostrar la tabla inicial
    for fila in matriz:
        print(" | ".join(f"{str(elem):<5}" for elem in fila))

def Calcular_cant_variables(funcion_objetivo):
    # Agregar un '+' al principio si no hay signo al inicio
    if funcion_objetivo[0] not in ['+', '-']:
        funcion_objetivo = '+' + funcion_objetivo

    # Separar los términos con signos de + o -
    terminos = re.split(r'(?=\+|\-)', funcion_objetivo)

    variables = set()

    # Buscar variables en cada término
    for termino in terminos:
        encontrados = re.findall(r'[A-Za-z]\d+', termino)
        variables.update(encontrados)
    
    cantidad_variables = len(variables)
    return cantidad_variables

def Pedir_restricciones(num_restricciones, num_variables):
    restricciones = []

    for i in range(num_restricciones):
        restriccion = []
        print(f"Ingrese los coeficientes de la restricción {i + 1}:")
        
        # Pedir los coeficientes de cada variable
        for j in range(num_variables):
            coef = float(input(f"Coeficiente de la variable X{j + 1}: "))
            restriccion.append(coef)
        
        # Pedir el término independiente (b)
        termino_independiente = float(input(f"Ingrese el término independiente (b) de la restricción {i + 1}: "))
        restriccion.append(termino_independiente)
        
        restricciones.append(restriccion)
    
    return restricciones

if __name__ == '__main__':
    Principal()
