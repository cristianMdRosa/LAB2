class Bicicleta:
    def __init__(self, marca, modelo, año, tipo, tamaño, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo = tipo  
        self.tamaño = tamaño  
        self.color = color
        self.estado = "NO VENDIDO"
    
    def vender(self):
        self.estado = "VENDIDO"
    
    def mostrar_info(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Tipo: {self.tipo}")
        print(f"Tamaño: {self.tamaño}")
        print(f"Color: {self.color}")
        print(f"Estado: {self.estado}")

def registrar_bicicleta():
    print("Registro de Bicicleta")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    año = input("Año: ")
    tipo = input("Tipo (Montaña/Carretera/Híbrida): ")
    tamaño = input("Tamaño (pulgadas): ")
    color = input("Color: ")
    
    bicicleta = Bicicleta(marca, modelo, año, tipo, tamaño, color)
    bicicleta.vender()  
    bicicleta.mostrar_info()


registrar_bicicleta()
