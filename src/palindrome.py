from re import sub

def is_palindrome(string: str) -> bool:
    # Usa la función sub (de sustituir) de la librería re para sustituir todos
    # los caracteres no alfanuméricos que se precisan en "a-zA-Z0-9"
    # El ^ le hace saber que tiene que sustituir todos los símbolos menos esos
    string = sub(r'[^a-zA-Z0-9]', '', string).lower()

    # Retorna la comparación de la string original y sí misma invertida
    # Para invertir la string se usa slicing con un step de -1
    # que hace que vaya del final al principio
    return string == string[::-1]


if __name__ == "__main__":
    string = input("Ingrese una palabra o frase: ")
    print(f"{string} es un palíndromo" if is_palindrome(string) else f"{string} no es un palíndromo")
