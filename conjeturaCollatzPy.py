# python 3.6.2

#    Nombre del archivo: conjeturaCollatz.py
#    Autor: Fernando Aguilar Serment
#    E-mail: gnu.fer@gmail.com

#    Descripcion:          ------------------------------------------------------------------------

#    Conjetura de Collatz

#    Toma un entero positivo cualquiera. Si es par, dividelo entre dos; si es impar, multiplicalo
#    por tres y sumale 1. Repite el proceso con cada uno de los resultados que vas obteniendo.
#    Sea cual sea el numero entero positivo con el que hayas comenzado, al final siempre terminaras
#    con la secuencia 4,2,1, y no saldras de ese bucle.

#    Fuente: http://gaussianos.com/la-conjetura-de-collatz/

# ------------------------------------------------------------------------------

# variable llamada 'cont' que llevara una cuenta del numero de operaciones realizadas
cont = 1

# Definimos una funcion solo para regresar el valor par
def par(n):
    return int(n / 2)

# Definimos una funcion solo para regresar el valor impar
def impar(n):
    return int((n*3) + 1)

# Definimos una variable llamada 'num' para
# manipular la secuencia de numeros a calcular
num = int(input("Ingresa un numero entero positivo: "))

# La siguiente instruccion imprimira dos columnas,
# La columna izquierda muestra el numero de operaciones realizadas,
# y la columna derecha muestra los numeros resultantes de la secuencia
print("#","Secuencia")

# Usamos un ciclo while para realizar las repeticiones
# mientras el numero ingresado sea mayor a 1
while(num > 1):
    # Primero verificamos que el numero 'num' ingresado sea par, a traves de la operacion modulo,
    # Si 'num' es par llama la funcion par(), si es impar llama a la funcion impar()
    if(num % 2 == 0):
        num = par(num)
    else:
        num = impar(num)

    # Luego, imprime en la columna izquierda el valor del contador,
    # y a la derecha el valor del numero par o impar
    print(cont,num)

    # Terminara el ciclo cuando 'num' sea igual a 1
    if(num == 1):
        break
    # Contador usado para mostrar el numero de operaciones
    cont = cont + 1
