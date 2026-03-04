# Cajero Bancolombia

## ¿Qué es el código?

El siguiente código presenta un sistema simple, sencillo y fácil de entender sobre un cajero de la empresa **Bancolombia.** 

## ¿De qué trata el código? 

El cajero le permitirá al usuario **consultar su saldo**, **depositar y retirar dinero de su cuenta,** 
Y dependiendo de qué deseé, tendrá que **escoger un número del 1 al 3**

1.  Para consultar el saldo actual
```py
  opción = int(input("Seleccione una opción de las anteriores; 1, 2 o 3\n"))
    if opción == 1:
            print("Su saldo actual es:", saldo_inicial )
```

2.  Para depositar dinero de la cuenta
3.  Para retirar dinero de la misma

# El usuario podrá hacer todas las operaciones que desee

Al inicio del código, la computadora le dirá al usuario:

**¿Cuántas operaciones desea realizar?**

Y seguido de esto, el usuario podrá **insertar** la cantidad de veces que quiera hacer el proceso 

A continuación el código respectivo:

```py
operaciones = int(input("Cuántas operaciones desea realizar? \n"))

for i in range(operaciones):

    print("Página principal:")
    print("Opción 1 → Consultar saldo")
    print("Opción 2 → Retirar saldo")
    print("Opción 3 → Depositar saldo")

 ``` 

### Ordered

1. Item 1
2. Item 2
3. Item 3
    1. Item 3a
    2. Item 3b

## Images

![This is an alt text.](/image/Markdown-mark.svg "This is a sample image.")

## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).

## Blockquotes

> Markdown is a lightweight markup language with plain-text-formatting syntax, created in 2004 by John Gruber with Aaron Swartz.
>
>> Markdown is often used to format readme files, for writing messages in online discussion forums, and to create rich text using a plain text editor.

## Tables

| Left columns  | Right columns |
| ------------- |:-------------:|
| left foo      | right foo     |
| left bar      | right bar     |
| left baz      | right baz     |

## Blocks of code

```
let message = 'Hello world';
alert(message);
```

## Inline code

This web site is using `markedjs/marked`.
