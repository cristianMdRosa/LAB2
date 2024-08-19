class Articulo:
    def __init__(self, nombre, tipo, precio_compra, precio_venta):
        self.nombre = nombre
        self.tipo = tipo
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
    
    def mostrar_info(self):
        print(f"Artículo: {self.nombre}")
        print(f"Tipo: {self.tipo}")
        print(f"Precio de compra: ${self.precio_compra:.2f}")
        print(f"Precio de venta: ${self.precio_venta:.2f}")
        print("-" * 30)

def calcular_precio_venta(precio_compra):
    return precio_compra * 1.30

def registrar_articulos():
    articulos = []
    
  
    for _ in range(2):
        tipo_cuaderno = input("Ingrese el tipo de cuaderno (50 hojas o 100 hojas): ")
        precio_compra = float(input("Ingrese el precio de compra del cuaderno: "))
        precio_venta = calcular_precio_venta(precio_compra)
        cuaderno = Articulo("Cuaderno HOJITAS", tipo_cuaderno, precio_compra, precio_venta)
        articulos.append(cuaderno)
    

    for _ in range(2):
        tipo_lapiz = input("Ingrese el tipo de lápiz (grafito o colores): ")
        precio_compra = float(input("Ingrese el precio de compra del lápiz: "))
        precio_venta = calcular_precio_venta(precio_compra)
        lapiz = Articulo("Lápiz RAYAS", tipo_lapiz, precio_compra, precio_venta)
        articulos.append(lapiz)
    
    return articulos

def mostrar_articulos(articulos):
    print("\nArtículos registrados:")
    for articulo in articulos:
        articulo.mostrar_info()

articulos = registrar_articulos()
mostrar_articulos(articulos)
