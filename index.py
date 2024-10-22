import numpy as np

def simplex(c, A, b, objective="max"):
    if objective == "min":
        c = -c

    num_constraints, num_vars = A.shape

    # Inicializamos el tableau
    tableau = np.hstack([A, np.eye(num_constraints), b.reshape(-1, 1)])
    tableau = np.vstack([np.hstack([c, np.zeros(num_constraints + 1)]), tableau])

    # Variables artificiales
    artificial_vars = np.zeros(num_constraints)
    for i in range(num_constraints):
        if b[i] < 0:
            tableau[i + 1] = -tableau[i + 1]  # Cambiar el signo si b[i] < 0
            artificial_vars[i] = 1  # Añadir variable artificial

    # Reconfigurar el objetivo para incluir las variables artificiales
    c_artificial = np.zeros(num_constraints)
    tableau[0, -1] += np.sum(artificial_vars) * 1000  # Penalizar las variables artificiales

    print("Tabla inicial:")
    print_tableau(tableau)

    while np.any(tableau[0, :-1] < 0):
        pivot_col = np.argmin(tableau[0, :-1])
        ratios = tableau[1:, -1] / tableau[1:, pivot_col]
        valid_ratios = np.where(tableau[1:, pivot_col] > 0, ratios, np.inf)
        pivot_row = np.argmin(valid_ratios) + 1

        if valid_ratios[pivot_row - 1] == np.inf:
            raise Exception("Problema no acotado")

        tableau[pivot_row] = tableau[pivot_row] / tableau[pivot_row, pivot_col]
        for i in range(len(tableau)):
            if i != pivot_row:
                tableau[i] -= tableau[i, pivot_col] * tableau[pivot_row]

        print("\nTabla después de pivoteo:")
        print_tableau(tableau)

    solution = np.zeros(num_vars)
    for i in range(num_vars):
        col = tableau[1:, i]
        if np.count_nonzero(col) == 1 and np.any(col == 1):
            solution[i] = tableau[1 + np.argmax(col), -1]

    optimal_value = tableau[0, -1]

    if objective == "min":
        optimal_value = -optimal_value

    return solution, optimal_value

def print_tableau(tableau):
    num_vars = tableau.shape[1] - 1
    num_rows = tableau.shape[0]

    headers = [f'x{i+1}' for i in range(num_vars)] + [f's{i+1}' for i in range(num_rows - 1)] + ['b']
    print(" | ".join(headers))

    for i in range(num_rows):
        row_name = f'F{i}' if i == 0 else f'x{i-1}' if i <= num_vars else f's{i - num_vars}'
        print(row_name + " | " + " | ".join(f"{val:8.2f}" for val in tableau[i]))

def main():
    print("¿Quieres maximizar o minimizar la función objetivo? (max/min)")
    objective = input().strip().lower()

    num_vars = int(input("Ingresa el número de variables en la función objetivo: "))
    
    c = np.array([float(x) for x in input(f"Ingresa los {num_vars} coeficientes de la función objetivo separados por espacios: ").split()])

    num_constraints = int(input("Ingresa el número de restricciones: "))

    A = []
    b = []
    for i in range(num_constraints):
        A.append([float(x) for x in input(f"Ingresa los {num_vars} coeficientes de la restricción {i+1} separados por espacios: ").split()])
        inequality = input("¿Es la restricción tipo menor o igual (<=) o mayor o igual (>=)? ")
        if inequality.strip() == ">=":
            A[-1] = [-a for a in A[-1]]  # Cambiar el signo de los coeficientes
            b.append(-float(input("Ingresa el valor del lado derecho de la restricción: ")))
        else:
            b.append(float(input("Ingresa el valor del lado derecho de la restricción: ")))

    A = np.array(A)
    b = np.array(b)

    solution, optimal_value = simplex(c, A, b, objective)

    print("\nValores óptimos de las variables:", solution)
    print(f"Valor óptimo de la función {'maximización' if objective == 'max' else 'minimización'}:", optimal_value)

if __name__ == "__main__":
    main()
