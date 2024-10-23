from tabla import modelo_tabla
import re

def Principal():
    funcion_objetivo = input('Ingrese la función objetivo: ')
    cantidad_variables = Calcular_cant_variables(funcion_objetivo)

    print(cantidad_variables)

    return cantidad_variables


def Calcular_cant_variables (funcion_objetivo):

    if funcion_objetivo[0] not in ['+', '-']:
        funcion_objetivo = '+' + funcion_objetivo

    terminos = re.split(r'(?=\+|\-)', funcion_objetivo)

    variables = set()

    for termino in terminos:
        encontrados = re.findall(r'[A-Za-z]\d+', termino)
        variables.update(encontrados)

    
    cantidad_variables = len(variables)

    return variables


    #max_min= int(input("¿Quieres maximizar o minimizar la función objetivo? ( 1 = max/ 2 = min): " ))
#funcion_objetivo = input('Ingrese la función objetivo: ')

    # Agregar un '+' al principio si no hay signo al inicio
if __name__ == '__main__':
    Principal()