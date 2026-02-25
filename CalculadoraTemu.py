def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicación(a,b):
    return a * b

def división (a,b):
    if b == 0:
        return("No se puede dividir por 0")
    else: 
        return a/b
    
def potencia(a,b):
    return  a ** b 

def raíz_cuadrada(a):
    if a < 0:
        return "No existe raiz real"
    return a ** 0.5

def porcentaje(a,b):
    return a * b / 100

def módulo(a,b): 
    return a % b

def promedio(a,b):
    return (a + b) / 2

def calculadora():

    while True:
        print("Bienvenido a la calculadora de Temu")
        print("Seleccione a continuación cualquiera de las siguientes operaciones la que desea realizar")
        print("'1' para la Suma")
        print("'2' para la Resta")
        print("'3' para la Multiplicación")
        print("'4' para la División")
        print("'5' para las Potencias")
        print("'6' para las Raíces")
        print("'7' para el Porcentaje")
        print("'8' Para el Módulo")
        print("'9' para el Promedio de dos números")
        print("'0' Para apagar la calculadora") 

        opción = int(input())

        if opción == 1:

            num1 = int(input("Escriba el primer número\n"))
            num2 = int(input("Escriba el segundo número\n"))

            valor_resultado = suma(num1,num2)
            print(valor_resultado)

            continue

        elif opción == 2:

            num1 = int(input("Escriba el primer número\n"))
            num2= int(input("Escriba el segundo número\n"))

            valor_resultado = resta(num1,num2)
            print(valor_resultado)

            continue
        
        elif opción == 3:
            
            num1 = int(input("Escriba el primer número\n"))
            num2 = int(input("Escriba el segundo número\n"))

            valor_resultado = multiplicación(num1,num2)
            print(valor_resultado)

            continue

        elif opción == 4:

            num1 = int(input("Escriba el primer número\n"))
            num2 = int(input("Escriba el segundo número\n"))

            valor_resultado = división(num1,num2)
            print(valor_resultado)

            continue

        elif opción == 5:

            num1 = int(input("Escriba la base\n"))
            num2 = int(input("EScriba el exponente\n"))
            
            valor_resultado = potencia(num1,num2)
            print(valor_resultado)

            continue

        elif opción == 6:
            
            num1 = int(input("Escriba el número que desee sacarle su raíz cuadrada\n"))
            
            valor_resultado = raíz_cuadrada(num1)
            print(valor_resultado)
            continue

        elif opción == 7:

            num1 = int(input("Inserte la cantidad\n"))
            num2 = int(input("Inserte el porcentaje deseado\n"))

            valor_resultado = porcentaje(num1,num2)
            print(valor_resultado)
            continue

        elif opción == 8:
            num1 = int(input("Inserte el primer número\n"))
            num2 = int(input("Inserte el segundo número\n"))

            valor_resultado = módulo(num1,num2)
            print(valor_resultado)
            continue

        elif opción == 9:
            num1 = int(input("Escriba el primer número\n"))
            num2 = int(input("Escriba el segundo número\n"))
            

            valor_resultado = promedio(num1,num2)
            print(valor_resultado)
            continue

        elif opción == 0:
            print("Calculadora apagada")
            break 

        else: 
            print("Caracteres inválidos")
        

calculadora()

