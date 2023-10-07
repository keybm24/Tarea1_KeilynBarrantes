# La tarea debe realizarse de manera individual. 
# Debe realizar una aplicación en el lenguaje de su preferencia, que realice las siguientes funciones (40%): 
# Suma. 
# Resta.
# Multiplicación. 
# División. 
# Verificación de número primo. 
# El programa se puede realizar con interfaz gráfica o en consola. (10%) 
# El código fuente debe ser Clean Code. (50%) 

import time

def sumar(a, b):
    resultado = a + b
    return resultado

def restar(a, b):
    resultado = a - b
    return resultado

def multiplicar(a, b):
    resultado = a * b
    return resultado

def dividir(a, b):
    if b == 0:
        return 'No es posible dividir por 0, intentelo nuevamente'
    else:
        resultado = a / b
        return resultado

def primo(a):
    if a <= 1:
        return 'El numero que ingreso No es un numero primo'
    elif a == 2:
        return 'El numero que ingreso Si es un numero primo'
    else:
        for i in range(2, a):
            if a % i == 0:
                return 'El numero que ingreso No es un numero primo'
        return 'El numero que ingreso Si es un numero primo'

def calculadora():
    
    opcion=0
    while opcion!=6:
        print(f'''
            Calculadora 
            
            1. Sumar
            2. Restar
            3. Multiplicar
            4. Dividir
            5. Verificar número primo
            6. Salir
        ''')
        opcion = int(input('Elige una opcion: '))

        if opcion == 1:
            a = int(input('Ingrese un numero: '))
            b = int(input('Ingrese otro numero: '))
            resultadoSuma = sumar(a, b)
            print('El resultado de la suma es:', resultadoSuma)
            time.sleep(2)
        elif opcion == 2:
            a = int(input('Ingrese un numero: '))
            b = int(input('Ingrese otro numero: '))
            resultadoResta = restar(a, b)
            print('El resultado de la resta es:', resultadoResta)
            time.sleep(2)
        elif opcion == 3:
            a = int(input('Ingrese un numero: '))
            b = int(input('Ingrese otro numero: '))
            resultadoMultiplicacion = multiplicar(a, b)
            print('El resultado de la multiplicacion es:', resultadoMultiplicacion)
            time.sleep(2)
        elif opcion == 4:
            a = int(input('Ingrese un numero: '))
            b = int(input('Ingrese otro numero: '))
            resultadoDivision = dividir(a, b)
            print('El resultado de la division es:', resultadoDivision)
            time.sleep(2)
        elif opcion == 5: 
            a = int(input('Ingrese un numero para saber si es primo o no: '))
            print(primo(a))
            time.sleep(2)
        elif opcion == 6:
            print('---- Fin del programa ----')
            print('---------- Adios ----------')
            break
        else:
            print('Opcion erronea, Intenta nuevamente')
    
calculadora()

