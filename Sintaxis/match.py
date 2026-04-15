#evaluar expresión y comparar su valor contra varios casos
# match - Switch (para no usar tantos IF)

dia = 1
match dia:
    case 1:
        print("hoy es lunes")
    case 2:
        print("hoy es martes")
    case 3:
        print("hoy es Miercoles")
    case 4:
        print("hoy es Jueves")
    case 5:
        print("hoy es Viernes")
    case 6:
        print("hoy es Sabado")
    case _:
        print("no coincide con ningun dia")

    