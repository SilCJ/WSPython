""" Gestión de torneo
Crear jugadores con {nombre, email, puntos ganados, raza y estatus}
Raza { Terran, Zerg, o Protoss}
Estado {Activo Inactivo}
Contador de partidas
Contador de puntos
Ganador 3 pts - Perdedor 1 pt
Partidas de manera aleatoria
Resultado de manera aleatoria
Exportar a archivos los registros de los jugadores con la cantidad de partidas y puntos ganados
"""
import json
from enum import Enum


class Raza(Enum):
    TERRAN = 1
    ZERG = 2
    PROTOSS = 3

class Estado(Enum):
    ACTIVO = 4
    INACTIVO = 5


class Jugador:
    def __init__(self, nombre: str, email: str, pts_ganados: int, raza: Raza, estado: Estado, **kwargs):
        self.__nombre = nombre
        self.__email = email
        self.__pts_ganados = 0
        self.__raza = raza
        self.__estado = estado

    def obtener_nombre(self):
        return self.__nombre

    def obtener_email(self):
        return self.__email

    def pts_ganados(self):
        return self.__pts_ganados

    def obtener_raza(self):
        return self.__raza

    def obtener_estado(self):
        return self.__estado

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f"(nombre={self.__nombre}, mail={self.__email}, pts_ganados={self.__pts_ganados}, raza={self.__raza}, estado{self.__estado})"


#ACCIONES DEL SISTEMA
def crear_jugador():
    imp_header("CREAR JUGADORES")
    nombre = input("Nombre: ")
    email = input("Email: ")
    raza = input("Raza: ")
    estado = input("Estado: ")
    jugador = Jugador(nombre, email, pts_ganados, Raza[raza], Estado[estado])
    JUGADORES.append(jugador)
    print(f"Jugador registrado: {jugador}")

def all_judagores():
    imp_header("LISTADO DE JUGADORES")
    with open ("jugadores.json")as file:
        data= json.load(file)
        print(data)

def contador_partidas (self):
    imp_header("HISTORIAL DE PARTIDAS")


def contador_puntos (self):
    imp_header("HISTORIAL DE PUNTOS")

def partidas_aleatorias(self):
    imp_header("JUGAR")
    nombre = input("Nombre del jugador: ")
    for Jugador in JUGADORES:
        if Jugador.obtener_estado() == estado:
            print(f"Puedes jugar: {jugador}")


def resultado(self):
    imp_header("RESULTADO")



def imp_header(header: str):
    print(f"{40 * '='} {header} {40 * '='}")

#CONTROL SISTEMA

JUGADORES = []
#Guardar información
with open("jugadores.json", "w") as file:
    json.dump(JUGADORES, file)


MENU = {
    "crear jugadores": crear_jugador,
    "listado de jugadores": all_judagores,
    "historial de partidas": contador_partidas,
    "historial de puntos": contador_puntos,
    "jugar": partidas_aleatorias,
    "resultado": resultado
}

OPTIONS = ' || '.join(MENU.keys())

while True:
    action = input(f"Elige una opción {OPTIONS}\n")
    if action in MENU.keys():
        MENU[action]()
    else:
        print(f"Accion not soportada: {action}")





