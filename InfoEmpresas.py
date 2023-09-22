
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo_bruto):
        super().__init__(nombre, edad)
        self.sueldo_bruto = sueldo_bruto

class Directivo(Empleado):
    def __init__(self, nombre, edad, sueldo_bruto, categoria):
        super().__init__(nombre, edad, sueldo_bruto)
        self.categoria = categoria
        self.subordinados = []

    def agregar_subordinado(self, empleado):
        self.subordinados.append(empleado)

class Cliente(Persona):
    def __init__(self, nombre, edad, telefono):
        super().__init__(nombre, edad)
        self.telefono = telefono

def mostrar_datos_persona(persona):
    print(f'Nombre: {persona.nombre}, Edad: {persona.edad}')

def mostrar_datos_empleado(empleado):
    mostrar_datos_persona(empleado)
    print(f'Sueldo Bruto: {empleado.sueldo_bruto}')

def mostrar_datos_directivo(directivo):
    mostrar_datos_empleado(directivo)
    print(f'Categoria: {directivo.categoria}')
    print('Subordinados:')
    for subordinado in directivo.subordinados:
        mostrar_datos_empleado(subordinado)

def mostrar_datos_cliente(cliente):
    mostrar_datos_persona(cliente)
    print(f'Telefono: {cliente.telefono}')

def main():
    # Crear algunos empleados, directivos y clientes
    empleado1 = Empleado('Juan', 30, 2000)
    directivo1 = Directivo('Ana', 40, 3000, 'Gerente')
    directivo1.agregar_subordinado(empleado1)
    cliente1 = Cliente('Carlos', 35, '300-123-4567')

    # Mostrar los datos
    print('Empleado:')
    mostrar_datos_empleado(empleado1)
    print('\nDirectivo:')
    mostrar_datos_directivo(directivo1)
    print('\nCliente:')
    mostrar_datos_cliente(cliente1)

if __name__ == '__main__':
    main()
