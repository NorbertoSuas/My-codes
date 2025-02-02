import random

class Heroe:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

    def atacar(self, objetivo):
        dano = max(0, self.ataque - objetivo.defensa)
        objetivo.salud -= dano
        return dano

    def mostrar_estado(self):
        print(f"{self.nombre}: Salud={self.salud} Ataque={self.ataque} Defensa={self.defensa}")

    def habilidad_especial(self, objetivo):
        pass

class Zeus(Heroe):
    def __init__(self):
        super().__init__("Zeus", salud=120, ataque=18, defensa=10)

    def habilidad_especial(self, objetivo):
        dano_adicional = random.randint(5, 10)
        dano_total = self.ataque + dano_adicional
        objetivo.salud -= dano_total
        print(f"{self.nombre} lanza un rayo divino y hace {dano_total} de daño adicional a {objetivo.nombre}!")

class Quetzalcoatl(Heroe):
    def __init__(self):
        super().__init__("Quetzalcoatl", salud=100, ataque=15, defensa=8)

    def habilidad_especial(self, objetivo):
        dano_adicional = random.randint(8, 12)
        dano_total = self.ataque + dano_adicional
        objetivo.salud -= dano_total
        print(f"{self.nombre} desata un vendaval de plumas y hace {dano_total} de daño adicional a {objetivo.nombre}!")

class Hades(Heroe):
    def __init__(self):
        super().__init__("Hades", salud=110, ataque=16, defensa=9)

    def habilidad_especial(self, objetivo):
        dano_adicional = random.randint(6, 15)
        dano_total = self.ataque + dano_adicional
        objetivo.salud -= dano_total
        print(f"{self.nombre} invoca almas del inframundo y hace {dano_total} de daño adicional a {objetivo.nombre}!")

def mostrar_oponentes_disponibles(heroe, oponentes):
    print("\nOponentes disponibles:")
    for i, oponente in enumerate(oponentes, start=1):
        print(f"{i}. {oponente.nombre}")

def mostrar_menu(heroe):
    print(f"\nMenú de opciones para {heroe.nombre}:")
    print("1. Atacar")
    print("2. Mostrar estado")
    print("3. Usar habilidad especial")
    print("4. Saltar al siguiente héroe")
    print("5. Salir del juego")

def seleccionar_oponente(oponentes):
    while True:
        try:
            opcion = int(input("Selecciona un oponente: "))
            if 1 <= opcion <= len(oponentes):
                return oponentes[opcion - 1]
            else:
                print("Opción no válida. Ingresa un número válido.")
        except ValueError:
            print("Por favor, ingresa un número.")

def seleccionar_opcion():
    while True:
        try:
            opcion = int(input("Selecciona una opción: "))
            if 1 <= opcion <= 5:
                return opcion
            else:
                print("Opción no válida. Ingresa un número entre 1 y 5.")
        except ValueError:
            print("Por favor, ingresa un número.")

def ejecutar_opcion(opcion, heroe, oponentes, indice_heroe_actual):
    if opcion == 1:
        oponente_seleccionado = seleccionar_oponente(oponentes)
        dano = heroe.atacar(oponente_seleccionado)
        print(f"{heroe.nombre} ataca a {oponente_seleccionado.nombre} y le hace {dano} de daño.")
    elif opcion == 2:
        heroe.mostrar_estado()
    elif opcion == 3 and hasattr(heroe, 'habilidad_especial'):
        oponente_seleccionado = seleccionar_oponente(oponentes)
        heroe.habilidad_especial(oponente_seleccionado)
        print(f"{heroe.nombre} ha usado su habilidad especial contra {oponente_seleccionado.nombre}!")
    elif opcion == 4:
        # Saltar al siguiente héroe
        indice_heroe_actual = (indice_heroe_actual + 1) % len(heroes)
        print(f"{heroe.nombre} ha saltado al siguiente héroe.")
    elif opcion == 5:
        print("Saliendo del juego.")
        exit()

    return indice_heroe_actual

if __name__ == "__main__":
    zeus = Zeus()
    quetzalcoatl = Quetzalcoatl()
    hades = Hades()

    heroes = [zeus, quetzalcoatl, hades]
    indice_heroe_actual = 0

    while sum(heroe.salud > 0 for heroe in heroes) > 1:
        heroe = heroes[indice_heroe_actual]

        if heroe.salud <= 0:
            # Saltar héroes derrotados
            indice_heroe_actual = (indice_heroe_actual + 1) % len(heroes)
            continue

        print(f"\n¡Es el turno de {heroe.nombre}!")

        oponentes = [otro_heroe for otro_heroe in heroes if otro_heroe != heroe and otro_heroe.salud > 0]

        mostrar_oponentes_disponibles(heroe, oponentes)
        mostrar_menu(heroe)
        opcion = seleccionar_opcion()

        # Ejecutar la opción y obtener el nuevo índice del héroe actual
        indice_heroe_actual = ejecutar_opcion(opcion, heroe, oponentes, indice_heroe_actual)

        # Cambiar al siguiente oponente
        oponentes = [otro_heroe for otro_heroe in oponentes if otro_heroe.salud > 0]

        if not oponentes:
            print(f"\n{heroe.nombre} ha derrotado a todos los oponentes.")
            continue

        # Si no se eligió la opción 2 (mostrar estado), pasar al siguiente héroe automáticamente
        if opcion != 2:
            indice_heroe_actual = (indice_heroe_actual + 1) % len(heroes)

    print("Juego terminado.")
