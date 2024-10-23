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