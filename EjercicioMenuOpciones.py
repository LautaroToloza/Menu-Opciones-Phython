"""
Desarrolle un programa completo en Python, controlado por menú de opciones,
que incluya las siguientes opciones:
1.)    Ingrese en nombre de tres meses y además ingrese la cantidad de lluvia caída en cada mes.
Determine y muestre el nombre del mes mas seco (el de menor cantidad de lluvia).
Si esa cantidad de lluvia es menor o igual al 20mm,
indicar con un mensaje que dicho mes fue extremadamente seco.
2.)    Ingrese una secuencia n de números (n se carga también por teclado).
Determine el acumulado de los números pares que se cargaron, y el acumulado de los impares.
Por último, determine el porcentaje de cada acumulador sobre el total de los numeros ingresados
e informar con un mensaje si el porcentaje de pares es superior o no al de los impares.
3.)    Terminar el programa.
"""


def test():
    print("Bienvenido al Menú de opciones..", "\n1) Programa de cantidad de lluvia",
          "\n2) Programa de números pares e impares", "\n3) Salida del programa")

    op = int(input("\nIngrese su opción: "))
    while op != 3:
        if op == 1:
            print("\nBienvenido al programa de cantidad de lluvia!!")
            mes1 = input("Ingrese un mes: ")
            lluvia_m1 = int(input("Ingrese cuanta lluvia cayó en el mes de " + mes1 + ": "))
            mes2 = input("Ingrese otro mes: ")
            lluvia_m2 = int(input("Ingrese cuanta lluvia cayó en el mes de " + mes2 + ": "))
            mes3 = input("Ingrese otro mes: ")
            lluvia_m3 = int(input("Ingrese cuanta lluvia cayó en el mes de " + mes3 + ": "))
            if lluvia_m1 < lluvia_m2 and lluvia_m1 < lluvia_m3:
                print("El mes más seco fue: " + mes1)
                men, mes = lluvia_m1, mes1
            elif lluvia_m2 < lluvia_m3:
                print("El mes más seco fue: " + mes2)
                men, mes = lluvia_m2, mes2

            else:
                print("El mes más seco fue: " + mes3)
                men, mes = lluvia_m3, mes3
            if men <= 20:
                ok = True
                if ok:
                    print("El mes de " + mes + " fue extremadamente seco!!")

            print("\nMenú de opciones..", "\n1) Programa de cantidad de lluvia",
                  "\n2) Programa de números pares e impares", "\n3) Salida del programa")
            op = int(input("\nIngrese su opción: "))

        elif op == 2:
            print("\nBienvenido al programa de números pares e impares!!")
            n = int(input("Ingrese cuantos números quiere cargar: "))
            cont_par, cont_impar = 0, 0
            porc_par, porc_impar = 0, 0
            for i in range(n):
                num = int(input("Ingrese un número: "))
                if num % 2 == 0:
                    cont_par += 1
                else:
                    cont_impar += 1
            if n != 0:
                porc_par = (cont_par * 100) / n
                porc_par = round(porc_par, 2)
                porc_impar = (cont_impar * 100) / n
                porc_impar = round(porc_impar, 2)
            if porc_par > porc_impar:
                print("El porcentaje de los números pares es mayor al de los impares.")
            else:
                print("El porcentaje de los números pares es menor al de los impares.")
            print("\nMenú de opciones..", "\n1) Programa de cantidad de lluvia",
                  "\n2) Programa de números pares e impares", "\n3) Salida del programa")
            op = int(input("\nIngrese su opción: "))
        else:
            while op > 3 or op < 1:
                print("Ingreso una opción incorrecta.")
                print("\nMenú de opciones..", "\n1) Programa de cantidad de lluvia",
                      "\n2) Programa de números pares e impares", "\n3) Salida del programa")
                op = int(input("\nIngrese una opción correcta: "))

    print("\n\t\t------ Finalizo el programa, gracias por utilizar el programa con menú de opciones!! ------")


# Script Principal
test()
