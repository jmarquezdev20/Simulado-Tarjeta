class  Cliente:
    """
    Representa a un cliente con nombre y apellido.
    
    Atributos:
        nombre (str): Nombre del cliente.
        apellido (str): Apellido del cliente.
    """
    def __init__(self,nombre,apellido):
        """
        Inicializa un nuevo cliente con nombre y apellido.

        Parámetros:
            nombre (str): Nombre del cliente.
            apellido (str): Apellido del cliente.
        """
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_info(self):
        """
        Muestra la información del cliente en formato: "nombre apellido".
        """
        print(f"nombre: {self.nombre} {self.apellido}")