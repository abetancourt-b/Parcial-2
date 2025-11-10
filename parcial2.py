# Autor: Antonio Betancourt

# 1 Desarrolar un programa que determine si en una lista no existen elementos repetidos

def ejercicio1():
    lista = [0,1,2,3,4]
    for x in lista:
        print(f"el numero {x} se repite:", lista.count(x), "veces")
        if lista.count(x) == 1:
            print(f"Para el numero {x} no existen elementos repetidos\n")
        else:
            print(f"Para el numero {x} se repite mas de 1 vez\n")

ejercicio1()
# 2 Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o mas vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir "No existe".
def ejercicio2():
        
    lista = ["Antonio", "azul", "color", "nombre", "sol"]

    def contar_vocales(cadena):
        vocales = "aeiouAEIOU"
        cuenta = 0
        for letra in cadena:
            if letra in vocales:
                cuenta += 1
        return cuenta
    
    encontradas = [palabra for palabra in lista if contar_vocales(palabra) >= 2]

    print("Cadenas con dos o más vocales:")

    for palabra in encontradas:
        print(palabra)
    else:
        print("No existe")
    
ejercicio2()
# 3 Desarrollar un programa que dada 2 listas determine que elementos tiene la primera lista que no tenga la segunda lista.
def ejercicio3():
    lista1 = [0,2,4,6,8]
    lista2 = [0,1,2,3,4,5]
    for x in lista1:
        if x in lista2:
            print(f"El elemento {x} de la lista 1, se encuentra en la lista 2")
        else:
            print(f"El elemento {x} de la lista 1, no se encuentra en la lista 2")
ejercicio3()
# 4 Desarrolar un algoritmo que calcule el promedio de un arreglo de reales.
def ejercicio4():
    lista = [1,2,3,4,5,6,7] 
    lista[0] = 1.5
    lista[6] = 6.5
    
    numerador = sum(lista) # 1.5 + 2 + 3 + 4 + 5 + 6 + 6.5 = 8 + 9 + 5 + 6 = 14 + 8 + 6 = 22 + 6 = 28
    divisor = len(lista) # Largo del Conjunto: 7
    
    promedio = numerador/divisor
    print(f"El promedio del arreglo de los reales es: {promedio}") 
ejercicio4()