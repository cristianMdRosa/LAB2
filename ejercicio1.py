class Perro:
    def __init__(self, nombre, edad, raza, peso, color, sexo):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.peso = peso
        self.color = color
        self.sexo = sexo
        self.estado = "NO ATENDIDO"
        self.tipo = "Perro Grande" if peso > 10 else "Perro Pequeño"
    
    def registrar(self):
        self.estado = "ATENDIDO"
    
    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Raza: {self.raza}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Sexo: {self.sexo}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

def registrar_perro():
    print("Registro de Perro")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    raza = input("Raza: ")
    peso = float(input("Peso (kg): "))
    color = input("Color: ")
    sexo = input("Sexo: ")
    
    perro = Perro(nombre, edad, raza, peso, color, sexo)
    perro.registrar()
    perro.mostrar_info()

# Llamada a la función para registrar un perro
registrar_perro()
