saldo_inicial = 1000

operaciones = int(input("Cuántas operaciones desea realizar? \n"))

for i in range(operaciones):

    print("Página principal:")
    print("Opción 1 → Consultar saldo")
    print("Opción 2 → Retirar saldo")
    print("Opción 3 → Depositar saldo")
    
    opción = int(input("Seleccione una opción de las anteriores; 1, 2 o 3\n"))
    if opción == 1:
            print("Su saldo actual es:", saldo_inicial )

    elif opción == 2:
        while True: 
            monto = float(input("Cuánto dinero desea retirar?\n"))

            if monto > saldo_inicial:
                print("No puede retirar más de su saldo actual")
                break
            elif monto < 0:
                    print ("Monto inválido") 
                    continue 
            else: 
                saldo_inicial = saldo_inicial - monto
                print("Saldo restante:", saldo_inicial)
                break 

    elif opción == 3:

        while True:

            monto_suma = float(input("cuánto dinero desea depositar?\n"))

            if monto_suma < 0:
                print("Monto inválido")
                continue
            elif monto_suma == 0:
                print("Monto inválido")
                break
            else:
                saldo_inicial = saldo_inicial + monto_suma 
                print("Saldo restante: ", saldo_inicial)
                break
    else:
         print("Opción inválida")
         
print("Gracias por usar el cajero automático de Bancolombia :)")