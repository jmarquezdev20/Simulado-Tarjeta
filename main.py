from tarjeta import Tarjeta
from cliente import Cliente
"""
main.py

Este es el módulo principal del sistema de tarjetas. Permite al usuario interactuar con una tarjeta
realizando operaciones como consultar saldo, recargar, pagar, activar y desactivar la tarjeta.

Autor: Juan Manuel Marquez Jimenez
Fecha: 2025-04-25
"""
def main():
    """
    Función principal que ejecuta el menú interactivo para operar con una tarjeta.
    
    Crea un cliente y una tarjeta asociada, luego permite al usuario realizar operaciones
    como consultar saldo, recargar, pagar, ver historial y gestionar el estado de la tarjeta.
    """
    cliente1 = Cliente("Juan", "Perez")
    tarjeta1 = Tarjeta("Juan", "1234567890123456", 1000)
    
    while True:
        print("======MENU=======")
        print("1. Consultar saldo")
        print("2. recargar")
        print("3. pagar")
        print("4. mostrar info")
        print("5. desactivar tarjeta")
        print("6. activar tarjeta")
        print("0. salir")
        try:
            opciones= int(input("ingrese una opción: "))
        except ValueError:
            print("ingrese una opción valida")
            continue
        if opciones == 1:
            tarjeta1.consultar_saldo()
        elif opciones == 2:
            try:
                monto=float(input("ingrese el monto a recargar: "))
                tarjeta1.recargar(monto)
            except ValueError:
                print("ingrese un numero valido")
        elif opciones == 3:
            try:
                monto=float(input("ingrese el monto a pagar: "))
                tarjeta1.pagar(monto)
            except ValueError:
                print("ingrese un numero valido")
        elif opciones == 4:
            tarjeta1.mostrar_historial()
        elif opciones == 5:
            tarjeta1.desactivar()   
        elif opciones == 6:
            tarjeta1.activar()
        elif opciones == 0:
            print("gracias por usar el sistema")
            tarjeta1.guardar_historial()# Guardamos el historial al salir
            break
        else:
            print("ingrese una opcion valida")

if __name__ == "__main__":
    main()
