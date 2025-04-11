#estaciones
mes = int(input("ingresa el numero del mes: "))
match mes:
    case 1 | 2 | 3 :
        print("la estacion es invierno")
    case 4 | 5 | 6 :
        print("la estacion es primavera")
    case 7 | 8 | 9 :
        print("la estacion es verano")
    case 10 | 11 | 12 :
        print("la estacion es otoño")
    case _:
        print("el numero del mes es invalido")