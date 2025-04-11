#dias de la semana
dia = int(input("escriba el numero del dia de la semana: "))
match dia:
    case 1:
        print("lunes")
    case 2:
        print("martes")
    case 3:
        print("miercoles")
    case 4:
        print("jueves")
    case 5:
        print("vienes")
    case 6:
        print("sabado")
    case 7:
        print("domingo")
    case _:
        print("ese numero es invalido")