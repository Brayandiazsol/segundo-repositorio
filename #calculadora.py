numeroUno = float(input("ingrese el primer número: "))
signo = input("ingrese el signo (+, -, *, /): ")
numeroDos = float(input("ingrese el segundo número: "))
resultado = None
match signo:
    case "+":
        resultado = numeroUno + numeroDos
    case "-":
        resultado = numeroUno - numeroDos
    case "*":
        resultado = numeroUno * numeroDos
    case "/":
        if numeroDos != 0:
            resultado = numeroUno / numeroDos
        else:
            print("no se puede dividir entre 0")
    case _:
        print("la operación es inválida")

if resultado is not None:
    print("el resultado es:", resultado)