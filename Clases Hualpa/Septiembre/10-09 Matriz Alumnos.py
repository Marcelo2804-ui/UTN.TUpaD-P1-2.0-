import random

alumnos = [
    "Lautaro Agustín Aguero",
    "Mateo Alejo Algañaraz",
    "Yoselie Aquino",
    "Santiago Facundo Barretto",
    "Ayrton Calderon",
    "María Belén Calvo García",
    "Nicolas Exequiel Carchano",
    "Sergio Joaquin Chiarello Ghilardi",
    "Santino Cárdenas Valls",
    "Octavio Agustin Fiore Montivero",
    "Bruno Fiouchetta",
    "Braian Leandro Flores Marin",
    "Agustina Luz Fontagnol",
    "Maximo Mateo Franco",
    "Facundo Adrian Gomez Romero",
    "Marcelo Hernán Gonzalez",
    "Genaro Guillot",
    "Camilo Javier Illanes Donoso",
    "Matias Nicolas Limina Nuñez",
    "Federico Alejandro Lopez",
    "Jeremías Daniel Luzuriaga",
    "Santino Mantineo",
    "Ezequiel Menéndez",
    "Nicolás Monjelardi",
    "Joel Nicolas Moreno",
    "Nicolás Uriel Moron Gutierrez",
    "Joaquín Morán",
    "Santino Naldini Sosa",
    "Andres Victor Novello",
    "Joseph Oliveros",
    "Santiago Javier Ontivero Parlade",
    "Roberto Paul Paiva",
    "Matías Pereyra",
    "Gianella Sol Peña",
    "Leonel Lautaro Ponce De Leon Martinez",
    "Cristian Nestor Rodriguez Martinez",
    "Ignacio Martín Rodríguez",
    "Rafael Ignacio Ruiz Guiñazú Puebla",
    "Florencia Santos",
    "Marcelo Scherer Huf",
    "Martina Guadalupe Suarez",
    "Elias Emanuel Tello",
    "Agustina Luz Fontagnol"
]

# Mezclar aleatoriamente los alumnos
random.shuffle(alumnos)

# Crear equipos de 4
equipos = [alumnos[i:i+4] for i in range(0, len(alumnos), 4)] # crea sublistas de 4 alumnos cada una 

# Mostrar los equipos
for index, equipo in enumerate(equipos): # enumera los alumnos
    print(f"\nEquipo {index + 1}:")
    for alumno in equipo:
        print(f" - {alumno}")
