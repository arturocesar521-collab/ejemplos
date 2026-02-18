saldo = 35
print("bienvenido a la maquina expendedora")

while True:
    print("Tu saldo es:", saldo)
    opcion = input("¿Quieres comprar una bebida por 20? (si/no): ")

    if opcion == "si":
        # LO QUE PASA INTERNAMENTE
        if saldo >= 20:
            saldo = saldo - 20
            print("Bebida entregada")
        else:
            print("no tienes suficiente saldo")
    else:
        print("gracias por comprar")

    break
