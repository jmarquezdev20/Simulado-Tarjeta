from datetime import datetime
import json


class Tarjeta:
    """
    Representa una tarjeta de usuario con funcionalidades de recarga, pago y gestión de estado.

    Atributos:
        titular (str): Nombre del titular de la tarjeta.
        numero (str): Número único de la tarjeta.
        saldo (float): Saldo actual disponible en la tarjeta.
        estado (bool): Indica si la tarjeta está activa o desactivada.
        historial (list): Lista de movimientos realizados en la tarjeta.
    """
    def __init__(self,titular,numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo
        self.estado=True
        self.historial=[]

    def cargar_historial(self):
        try:
            with open("historial.json", "r") as archivo:
                self.historial = json.load(archivo)
        except FileNotFoundError:
            self.historial = []
    
    def agregar_historial(self,accion,monto):
        self.historial.append({"accion":accion,
                               "monto":monto,
                               "saldo_actual":self.saldo,
                               "fecha":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                               })   
        self.guardar_historial()
                               
    def guardar_historial(self):
        try:
            with open("historial.json", "w") as archivo:
                json.dump(self.historial, archivo, indent=4)  # Escribe el historial de forma legible
        except Exception as e:
            print(f"Error al guardar historial: {e}")
          
    def desactivar(self):
        #vercamos si la tarjeta esta activa antes de cualquier accion
        if self.estado:
            self.estado=False
            print("tarjeta desactivada")
            self.agregar_historial("desactivar",0)

    def activar(self):
        #vercamos si la tarjeta esta activa antes de cualquier accion
        if not self.estado:
            self.estado=True
            print("tarjeta activada")
            self.agregar_historial("activar",0)

    def consultar_saldo(self):
        """
        Muestra el saldo actual si la tarjeta está activa. También registra esta acción en el historial.
        Si la tarjeta está desactivada, se informa al usuario y se registra igualmente la acción.
        """
        #vercamos si la tarjeta esta activa antes de cualquier accion 
        if self.estado:
            print(f"saldo actual: {self.saldo}")
            self.agregar_historial("consultar saldo",self.saldo)
        else:
            print("tarjeta desactivada")
            self.agregar_historial("consultar saldo",0)


    def recargar(self,monto):
        """
        Recarga saldo a la tarjeta si está activa.

        Parámetros:
        monto (float): Cantidad de dinero a recargar. Debe ser mayor a 0.
    """  
        #vercamos si la tarjeta esta activa antes de cualquier transaccion
        if self.estado:
            if monto>0:
                self.saldo+=monto
                print(f"recargado {monto} pesos")
                self.agregar_historial("recargar",monto)
            else:
                print("el monto debe ser mayor que 0")
               
        else:
            print("tarjeta desactivada")
            
    
    def pagar(self,monto):
        """
        Realiza un pago si la tarjeta está activa y tiene saldo suficiente.

        Parámetros:
        monto (float): Monto a pagar. Debe ser mayor a 0.

    """
        #vercamos si la tarjeta esta activa antes de cualquier transaccion
        if not self.estado:
            print("tarjeta desactivada")
            return
        
        if monto <= 0:
            print("el monto debe ser mayor que 0")
            return
            
        if self.saldo>=monto:
            self.saldo-=monto
            print(f"pagado exitoso de {monto}. saldo actual: {self.saldo}")
            self.agregar_historial("pagar",monto)
        else:
            print("saldo insuficiente")
            self.agregar_historial("pago fallido (saldo insuficiente)",monto)

        
    def mostrar_historial(self):
        for accion in self.historial:
            print(f"accion: {accion['accion']}, monto: {accion['monto']}, saldo actual: {accion['saldo_actual']}, fecha: {accion['fecha']}")


