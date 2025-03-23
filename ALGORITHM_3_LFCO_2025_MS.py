import time


def build_derivation_tree(string):
    derivation_steps = []
    remaining_string = string
    current_state = "S"  # Comienza desde el símbolo inicial S

    derivation_steps.append((current_state, remaining_string))

    while remaining_string:
        if remaining_string.startswith("a") and remaining_string.endswith("b"):
            # Regla de derivación: S → aSb
            current_state = current_state.replace("S", "aSb", 1)
            remaining_string = remaining_string[1:-1]  # Eliminar el primer y último carácter
            derivation_steps.append((current_state, remaining_string))
        else:
            break

    if not remaining_string:  # Si la cadena se ha procesado completamente
        current_state = current_state.replace("S", "ε")  # S → ε
        derivation_steps.append((current_state, "End"))
    else:
        print ("The string is not accepted by the CFG")
        time.sleep(1)

    return derivation_steps


if __name__ == "__main__":
    print("\n=== Building Derivation Trees ===\n")
    time.sleep(1.5)

    # Leer las cadenas desde strings.txt generadas por el Algoritmo 1
    with open("strings.txt", "r") as file:
        lines = file.readlines()

    strings = [line.strip() for line in lines if line.strip()]  # Eliminar líneas vacías

    # Filtrar cadenas válidas (esto ya se hizo en el Algoritmo 2)
    valid_strings = [s for s in strings if "a" in s and "b" in s]  # Ejemplo básico: cadenas con 'a' y 'b'

    for string in valid_strings:
        print(f"Derivation process for '{string}':")
        time.sleep(1)
        derivation_tree = build_derivation_tree(string)

        # Cabecera de la tabla
        print(f"{'Step':<5}{'Derivation':<30}{'Remaining String'}")
        print("=" * 60)
        time.sleep(1)

        # Mostrar cada paso del árbol de derivación
        for step_num, (derivation, remaining_string) in enumerate(derivation_tree, start=1):
            print(f"{step_num:<5}{derivation:<30}{remaining_string}")
            time.sleep(1)

        print("\n")  # Espacio para separar derivaciones de cadenas diferentes
        time.sleep(1)
    time.sleep(1)
    print("All derivation trees completed!\n")
    time.sleep(1)