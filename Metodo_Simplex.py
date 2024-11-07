import re
from sympy import symbols, simplify, sympify
from tabulate import tabulate

def Obterner_datos():
    x=False
    while x ==False:
        max_min = int(input('¿Quieres maximizar o minimizar la función objetivo? (1 = max/ 2 = min): '))
        if max_min == 1 or max_min == 2:
            x=True
        else:
            print()
            print('Valor incorrecto')
            print()
    
    
    funcion_ob = input('Ingrese la función Objetivo: ')
    cantidad_rest= int(input('Ingrese la cantidad de restricciones:'))
    restricciones=  []
    for i in range(cantidad_rest):
        resctriccion = input(f'Ingrese la restricción {i+1}: ')
        restricciones.append(resctriccion)
    """ print(funcion_ob)
    print(cantidad_rest)
    print(restricciones)
    print(max_min) """
    return funcion_ob,cantidad_rest, restricciones,max_min


def estandarizacion(funcion_ob,restricciones,max_min):
    
    restricciones_estandarizadas = []
    funcion_objetivo_extra = ""
    indice_S = 1 
    indice_A = 1 
    importante = []


    for restriccion in restricciones:
        if '>=' in restriccion:
            lado_izq, lado_der = restriccion.split('>=')
            lado_izq = f"{lado_izq.strip()} - S{indice_S} + A{indice_A}"
            lado_der = lado_der.strip()
            restriccion_estandarizada = f"{lado_izq} = {lado_der}"
            
            
            if max_min == 1: 
                funcion_objetivo_extra += f" + 0S{indice_S} - MA{indice_A}"
                importante.append(f"-MA{indice_A}")
            else:  
                funcion_objetivo_extra += f" + 0S{indice_S} + MA{indice_A}"
                importante.append(f"MA{indice_A}")
                
            indice_S += 1
            indice_A += 1

        elif '<=' in restriccion:
            lado_izq, lado_der = restriccion.split('<=')
            lado_izq = f"{lado_izq.strip()} + S{indice_S}"
            lado_der = lado_der.strip()
            restriccion_estandarizada = f"{lado_izq} = {lado_der}"
            
            
            funcion_objetivo_extra += f" + 0S{indice_S}"
            importante.append(f"0S{indice_S}")
            
            
            indice_S += 1

        elif '=' in restriccion:
            lado_izq, lado_der = restriccion.split('=')
            lado_izq = f"{lado_izq.strip()} + A{indice_A}"
            lado_der = lado_der.strip()
            restriccion_estandarizada = f"{lado_izq} = {lado_der}"
            
            
            if max_min == 1:  
                funcion_objetivo_extra += f" - MA{indice_A}"
                importante.append(f"-MA{indice_A}")
            else:  
                funcion_objetivo_extra += f" + MA{indice_A}"
                importante.append(f"MA{indice_A}")
                
            indice_A += 1

        restricciones_estandarizadas.append(restriccion_estandarizada)

   
    funcion_objetivo_estandarizada = funcion_ob + funcion_objetivo_extra

    print("\nFunción Objetivo Estandarizada:")
    print(funcion_objetivo_estandarizada) 
    print("\nRestricciones Estandarizadas:")
    for restriccion in restricciones_estandarizadas:
        print(restriccion)
    

    return funcion_objetivo_estandarizada, restricciones_estandarizadas,importante


def cantidad_variables(funcion_ob):
    if funcion_ob[0] not in ['+', '-']:
        funcion_ob = '+' + funcion_ob

    terminos = re.split(r'(?=\+|\-)', funcion_ob)

    variables = []

    for termino in terminos:
        encontrados = re.findall(r'[A-Za-z]\d+', termino)
        variables.extend(encontrados)

    cantidad_variables = len(variables)
    return cantidad_variables, variables

    
    

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
  

def Coeficientes_restri(cant_variables,variables,restricciones_estandarizadas):

    coeficientes = []

    for i in range(cant_variables):

        for restriccion in restricciones_estandarizadas:
            
            terminos = re.findall(r'([+-]?\d*)\s*'+re.escape(variables[i]), restriccion)

            if terminos:
                coeficiente = terminos[0]  
                if coeficiente == '' or coeficiente == '+':
                    coeficiente = 1  
                elif coeficiente == '-':
                    coeficiente = -1  
                else:
                    coeficiente = int(coeficiente)  
            else:
                coeficiente = 0  

    
            
            coeficientes.append(coeficiente)
            
    i=i+1

    #print(coeficientes)
    return coeficientes





def Coeficientes_FO(funcion_objetivo_estandarizada):
    
    if funcion_objetivo_estandarizada[0] not in ['+', '-']:
        funcion_objetivo_estandarizada = '+' + funcion_objetivo_estandarizada

    
    terminos = funcion_objetivo_estandarizada.replace(" ", "").replace("-", "+-").split("+")
    terminos = [t for t in terminos if t] 
    #print("Términos encontrados:", terminos)
    coeficientes = []

    for termino in terminos:
        if 'M' in termino or 'A' in termino:
            coef = "-M" if termino.startswith("-") else "M"
        else:
            coef_str = ""
            for char in termino:
                if char.isdigit() or char in "+-":  
                    coef_str += char
                else:
                    break
            
            coef = int(coef_str) if coef_str else 1

        
        coeficientes.append(coef)

    return coeficientes


M = symbols('M')

def ZJ(operaciones):
    expr = 0  

    for a, b in operaciones:
        if b == 'M':
            b = M  
        expr += a * b

    if isinstance(expr, (int, float)):
        return expr  
    elif all(term.has(M) for term in expr.as_ordered_terms()):  
        return simplify(expr)
    elif any(term.has(M) for term in expr.as_ordered_terms()):
        return expr
    else:
        return expr.evalf()


def operar(exp1, exp2):
    # Convierte los términos en expresiones simbólicas si son cadenas
    exp1 = sympify(exp1)
    exp2 = sympify(exp2)
    
    # Realizar la operación de resta entre las dos expresiones
    resultado = simplify(exp1 - exp2)
    return resultado


def llenar_tabla():
    funcion_ob,cantidad_rest,restricciones,max_min = Obterner_datos()
    funcion_objetivo_estandarizada, restricciones_estandarizadas, importante = estandarizacion(funcion_ob,restricciones,max_min)
    cant_variables,variables = cantidad_variables(funcion_objetivo_estandarizada) 
    coeficientes_rest =Coeficientes_restri(cant_variables, variables, restricciones_estandarizadas)
    matriz = modelo_tabla(cantidad_rest,cant_variables)
    coeficientes_FO = Coeficientes_FO(funcion_objetivo_estandarizada)

    #print(restricciones_estandarizadas)
    #print(funcion_objetivo_estandarizada)
    #print(variables)
    #print(coeficientes_rest)

    if max_min == 1 :
        matriz[0][0] = " + "
    else:
        matriz[0][0] = " - "

    indice = 0
    for i in range(cantidad_rest):

        matriz[i+2][0]= importante[i][0]
        matriz[i+2][1]= importante[i][-2:]
        matriz[i+2][2]= restricciones_estandarizadas[i].split('=')[-1].strip()
            
        
    for j in range(cant_variables):
        for i in range(cantidad_rest):
            matriz[i + 2][j + 3] = coeficientes_rest[indice]
        
            indice += 1 


    for i in range(cant_variables):
         matriz[0][i+3] = coeficientes_FO[i]
         matriz[1][i+3] = variables[i]
         i=i+1
    

    operacion = []
    r=0
    for j in range(cant_variables+1):
        #print(f"{j}:")
        for i in range(cantidad_rest):
            r=r+1
            a = matriz[i + 2][0] 
            b = matriz[i + 2][j+2]
            if a != 'M':
                a = int(a) 
            b = int(b) 
            operacion.append((b,a))
            #print(a,b)
            if r == cantidad_rest: 
                res = ZJ(operacion)
                #print(res)
                matriz [-2][j+2]=res
                operacion.clear()
                r=0

        
        
     
    for i in range(cant_variables):
        a = matriz[0][i+3]
        b = matriz[-2][i+3]
        res = operar(a,b)
        matriz[-1][i+3]= res
        #print(res)
        #print(a,b)

        
 

    
    anchos = [max(len(str(fila[i])) for fila in matriz) for i in range(len(matriz[0]))]


    print("")
    for fila in matriz:
        print(" | ".join(str(elem).ljust(anchos[i]) for i, elem in enumerate(fila)))
    print("")



    print("")
    print(tabulate(matriz, tablefmt="grid"))
    print("")

    sg = Siguente_tabla(matriz,max_min)





def Siguente_tabla(matriz,max_min):
    if max_min == 1:
        print("1")
    





if __name__ == '__main__':
    llenar_tabla()