
RESET = "\033[0m"
BOLD = "\033[1m"

BLACK   = "\033[30m"
RED     = "\033[31m"
GREEN   = "\033[32m"
YELLOW  = "\033[33m"
BLUE    = "\033[34m"
MAGENTA = "\033[35m"
CYAN    = "\033[36m"
WHITE   = "\033[37m"

ORANGE = "\033[38;5;208m"



BG_RED     = "\033[41m"
BG_GREEN   = "\033[42m"
BG_YELLOW  = "\033[43m"
BG_BLUE    = "\033[44m"

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicación(a,b):
    return a * b

def división (a,b):
    if b == 0:
        return(f"{RED}No se puede dividir por 0{RESET}")
    else: 
        return a/b
    
def potencia(a,b):
    return  a ** b 

def raíz_cuadrada(a):
    if a < 0:
        return f"{RED}No existe raiz real{RESET}"
    return a ** 0.5

def porcentaje(a,b):
    return a * b / 100

def módulo(a,b): 
    return a % b

def promedio(a,b):
    return (a + b) / 2

def calculadora():

    while True:
        print(f"{ORANGE}Bienvenido a la calculadora de Temu{RESET}")
        print(f"{WHITE}Seleccione a continuación cualquiera de las siguientes operaciones la que desea realizar{RESET}")
        print(f"{WHITE}'1'{RESET}" f"{CYAN} Para la Suma{RESET}")
        print(f"{WHITE}'2'{RESET}" f"{CYAN} Para la Resta{RESET}")
        print(f"{WHITE}'3'{RESET}" f"{CYAN} Para la Multiplicación{RESET}")
        print(f"{WHITE}'4'{RESET}" f"{CYAN} Para la División{RESET}")
        print(f"{WHITE}'5'{RESET}" f"{CYAN} Para las Potencias{RESET}")
        print(f"{WHITE}'6'{RESET}" f"{CYAN} Para las Raíces{RESET}")
        print(f"{WHITE}'7'{RESET}" f"{CYAN} Para el Porcentaje{RESET}")
        print(f"{WHITE}'8'{RESET}" f"{CYAN} Para el Módulo{RESET}")
        print(f"{WHITE}'9'{RESET}" f"{CYAN} Para el Promedio de dos números{RESET}")
        print(f"{WHITE}'0'{RESET}" f"{CYAN} Para{RESET}" f"{RED} apagar la calculadora{RESET}") 

        try:
            opción = int(input())
        except ValueError:
            print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
            continue

        if opción == 1:

            try:
                num1 = int(input("Escriba el primer número\n"))
                num2 = int(input("Escriba el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            
            valor_resultado = suma(num1,num2)
            print(f"El resultado de la suma es: {GREEN}{valor_resultado}{RESET}") 

            continue

        elif opción == 2:
            try:
                num1 = int(input("Escriba el primer número\n"))
                num2 = int(input("Escriba el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = resta(num1,num2)
            print(f"El resultado de la resta es: {GREEN}{valor_resultado}{RESET}")

            continue
        
        elif opción == 3:
            try:
                num1 = int(input("Escriba el primer número\n"))
                num2 = int(input("Escriba el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = multiplicación(num1,num2)
            print(f"El resultado de la multiplicación es: {GREEN}{valor_resultado}{RESET}")

            continue

        elif opción == 4:
            try:
                num1 = float(input("Escriba el primer número\n"))
                num2 = float(input("Escriba el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = división(num1,num2)
            print(f"El resultado de la división es: {GREEN}{valor_resultado}{RESET}")

            continue

        elif opción == 5:
            try:
                num1 = int(input("Escriba la base\n"))
                num2 = int(input("Escriba el exponente\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = potencia(num1,num2)
            print(f"El resultado de la potencia es: {GREEN}{valor_resultado}{RESET}")

            continue

        elif opción == 6:
            try:
                num1 = int(input("Escriba el número que desee sacarle su raíz cuadrada\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = raíz_cuadrada(num1)
            print(f"El resultado de la raíz cuadrada es: {GREEN}{valor_resultado}{RESET}")
            continue

        elif opción == 7:
            try:
                num1 = int(input("Inserte la cantidad\n"))
                num2 = int(input("Inserte el porcentaje deseado\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue

            valor_resultado = porcentaje(num1,num2)
            print(f"El resultado del porcentaje es: {GREEN}{valor_resultado}{RESET}")
            continue

        elif opción == 8:
            try:
                num1 = int(input("Inserte el primer número\n"))
                num2 = int(input("Inserte el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue
        
            valor_resultado = módulo(num1,num2)
            print(f"El resultado del módulo es: {GREEN}{valor_resultado}{RESET}")
            continue

        elif opción == 9:
            try:
                num1 = float(input("Escriba el primer número\n"))
                num2 = float(input("Escriba el segundo número\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}")
                continue
          
            valor_resultado = promedio(num1,num2)
            print(f"El resultado del promedio es: {GREEN}{valor_resultado}{RESET}")
            continue

        elif opción == 0:
            try:
                confirmación = str(input(f"{RED}¿Está seguro que desea apagar la calculadora?{RESET}\n" f"{WHITE}'1'{RESET}" f"{CYAN} Para confirmar{RESET}\n" f"{WHITE}'2'{RESET}" f"{CYAN} Para cancelar{RESET}\n"))
            except ValueError:
                print(f"{BG_RED}Caracteres inválidos{RESET}")
                continue

            if confirmación == "1":
                print(f"{GREEN}Calculadora apagada exitosamente{RESET}")
                break 
            elif confirmación == "2":

                print(f"{YELLOW}Cancelando apagado de la calculadora{RESET}")
                continue
            else:
                print(f"{BG_RED}Opción inválida, volviendo al menú principal{RESET}")
                continue

        else: 
            print(f"{BG_RED}Caracteres inválidos, volviendo al menú principal{RESET}") 
        

calculadora()

