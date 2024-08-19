class Dispositivo:
    def __init__(self, tipo, marca, modelo, año, color, precio_compra):
        self.tipo = tipo  
        self.marca = marca 
        self.modelo = modelo
        self.año = año
        self.color = color
        self.precio_compra = precio_compra
        self.precio_venta = self.calcular_precio_venta()
    
    def calcular_precio_venta(self):
      
        return round(self.precio_compra * 1.7, 2)
    
    def mostrar_info(self):
       
        print("*******************************")
        print(f"Tipo: {self.tipo}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print("*******************************")

def registrar_dispositivos():
    cantidad_dispositivos = int(input("¿Cuántos dispositivos desea registrar? "))
    dispositivos = []

    for i in range(cantidad_dispositivos):
        print(f"\nRegistrar dispositivo {i + 1}:")
        tipo = input("Tipo de dispositivo (celular, tablet, portátil): ")
        marca = "PHR" 
        modelo = input("Modelo: ")
        año = input("Año: ")
        color = input("Color: ")
        precio_compra = float(input("Precio de compra: "))

        dispositivo = Dispositivo(tipo, marca, modelo, año, color, precio_compra)
        dispositivos.append(dispositivo)
    
    return dispositivos

def mostrar_dispositivos(dispositivos):
    for i, dispositivo in enumerate(dispositivos, start=1):
        print(f"\nDatos del dispositivo {i}:")
        dispositivo.mostrar_info()


dispositivos = registrar_dispositivos()
mostrar_dispositivos(dispositivos)
