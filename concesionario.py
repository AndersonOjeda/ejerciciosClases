class Cliente:
    def __init__(self, dni, nombre, direccion, telefono, codigo):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.codigo = codigo
        self.avalador = None
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def establecer_avalador(self, cliente):
        self.avalador = cliente

class Coche:
    def __init__(self, matricula, modelo, color, marca, garaje):
        self.matricula = matricula
        self.modelo = modelo
        self.color = color
        self.marca = marca
        self.garaje = garaje

class Reserva:
    def __init__(self, fecha_inicio, fecha_final, cliente, agencia):
        self.fecha_inicio = fecha_inicio
        self.fecha_final = fecha_final
        self.cliente = cliente
        self.agencia = agencia
        self.coches = []
        self.precio_total = 0
        self.entregado = False

    def agregar_coche(self, coche, precio_alquiler, litros_gasolina):
        self.coches.append((coche, precio_alquiler, litros_gasolina))
        self.precio_total += precio_alquiler

    def entregar(self):
        self.entregado = True

def main():
    # Crear algunos clientes, coches y reservas
    cliente1 = Cliente('12345678A', 'Juan', 'Calle Falsa 123', '600123456', 'C1')
    cliente2 = Cliente('87654321B', 'Ana', 'Avenida Siempre Viva 456', '600654321', 'C2')
    coche1 = Coche('1234ABC', 'Modelo 1', 'Azul', 'Marca 1', 'Garaje 1')
    reserva1 = Reserva('2023-09-21', '2023-09-28', cliente1, 'Agencia 1')
    reserva1.agregar_coche(coche1, 100, 50)
    cliente1.agregar_reserva(reserva1)
    cliente2.establecer_avalador(cliente1)

    # Mostrar los datos
    print(f'Cliente: {cliente1.nombre}, DNI: {cliente1.dni}, Codigo: {cliente1.codigo}, Reservas: {len(cliente1.reservas)}')
    print(f'Cliente: {cliente2.nombre}, DNI: {cliente2.dni}, Codigo: {cliente2.codigo}, Avalador: {cliente2.avalador.nombre}')

if __name__ == '__main__':
    main()
