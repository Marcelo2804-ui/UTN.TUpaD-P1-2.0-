🌍 Sistema de Gestión de Datos de Países
📖 Descripción del Proyecto
Sistema desarrollado en Python para gestionar y analizar información sobre países del mundo. Permite realizar búsquedas, filtrados, ordenamientos y cálculos estadísticos sobre un dataset que incluye datos de población, superficie y continente de 195 países.
Este proyecto fue desarrollado como Trabajo Práctico Integrador (TPI) de la materia Programación 1 de la Tecnicatura Universitaria en Programación.
________________________________________
👥 Integrantes del Equipo
•	[Nombre Integrante 1] - [Rol/Tareas realizadas]
•	[Nombre Integrante 2] - [Rol/Tareas realizadas]
________________________________________
✨ Funcionalidades
El sistema ofrece las siguientes capacidades:
🔍 Búsqueda
•	Buscar países por nombre (coincidencia parcial, no distingue mayúsculas/minúsculas)
•	Visualización detallada con datos de población, superficie, continente y densidad poblacional
🔎 Filtros
•	Por continente: Filtrar todos los países de un continente específico
•	Por población: Filtrar países dentro de un rango de población determinado
•	Por superficie: Filtrar países dentro de un rango de superficie (km²)
📊 Ordenamientos
•	Ordenar por nombre (alfabéticamente A-Z o Z-A)
•	Ordenar por población (ascendente o descendente)
•	Ordenar por superficie (ascendente o descendente)
•	Ordenar por densidad poblacional (habitantes por km²)
📈 Estadísticas
•	País con mayor población
•	País con menor población
•	Promedio de población mundial
•	Promedio de superficie
•	Cantidad de países por continente
•	Población y superficie total mundial
📋 Otras funcionalidades
•	Listar todos los continentes disponibles con cantidad de países
•	Cálculo automático de densidad poblacional
•	Manejo robusto de errores y validaciones
________________________________________
🛠️ Tecnologías Utilizadas
•	Lenguaje: Python 3.x
•	Módulos estándar: 
o	csv - Para lectura de archivos CSV
•	Estructuras de datos: Listas y diccionarios
•	Paradigma: Programación modular
________________________________________
📂 Estructura del Proyecto
proyecto-gestion-paises/
│
├── main.py                 # Código principal del sistema
├── paises.csv             # Dataset con información de 195 países
├── Marco_Teorico.docx     # Documento con fundamentos teóricos
├── README.md              # Este archivo
└── capturas/              # Carpeta con capturas de pantalla
    ├── menu_principal.png
    ├── busqueda.png
    ├── filtros.png
    ├── estadisticas.png
    └── ordenamiento.png
________________________________________
🚀 Instrucciones de Uso
Requisitos Previos
•	Python 3.6 o superior instalado en el sistema
•	Archivo paises.csv en el mismo directorio que main.py
Instalación y Ejecución
1.	Clonar el repositorio:
2.	git clone https://github.com/[tu-usuario]/gestion-paises-python.git
3.	cd gestion-paises-python
4.	Ejecutar el programa:
5.	python main.py
6.	Navegar por el menú: Siga las instrucciones en pantalla y seleccione las opciones numéricas del menú.
________________________________________
💡 Ejemplos de Uso
Ejemplo 1: Buscar un país
Seleccione una opción: 1
Ingrese el nombre del país a buscar: argentina

==========================================================
Se encontraron 1 resultado(s):
==========================================================

  País: Argentina
  Población: 45,376,763 habitantes
  Superficie: 2,780,400 km²
  Continente: América
  Densidad: 16.32 hab/km²
Ejemplo 2: Filtrar por continente
Seleccione una opción: 2

CONTINENTES DISPONIBLES:
  - África (54 países)
  - América (35 países)
  - Asia (49 países)
  - Europa (44 países)
  - Oceanía (14 países)

Ingrese el nombre del continente: Europa

==========================================================
Países de Europa: 44 encontrados
==========================================================
  - Albania
  - Alemania
  - Andorra
  ...
Ejemplo 3: Ver estadísticas generales
Seleccione una opción: 6

==========================================================
ESTADÍSTICAS GENERALES
==========================================================

Total de países: 195

--- POBLACIÓN ---
  Total mundial: 7,794,798,739 habitantes
  Promedio: 39,972,301 habitantes
  País más poblado: China (1,439,323,776)
  País menos poblado: Vaticano (801)

--- SUPERFICIE ---
  Total: 134,099,097 km²
  Promedio: 687,687 km²
  País más grande: Rusia (17,098,242 km²)
  País más pequeño: Vaticano (0 km²)

--- PAÍSES POR CONTINENTE ---
  África: 54 países
  América: 35 países
  Asia: 49 países
  Europa: 44 países
  Oceanía: 14 países
Ejemplo 4: Ordenar países por población
Seleccione una opción: 5

¿Por qué criterio desea ordenar?
1. Nombre
2. Población
3. Superficie
4. Densidad poblacional
Seleccione opción: 2

¿Orden ascendente o descendente?
1. Ascendente
2. Descendente
Seleccione opción: 2

==========================================================
Países ordenados por poblacion (descendente):
==========================================================
  1. China: 1,439,323,776 habitantes
  2. India: 1,380,004,385 habitantes
  3. Estados Unidos: 331,893,745 habitantes
  4. Indonesia: 273,523,615 habitantes
  5. Pakistán: 220,892,340 habitantes
  ...
________________________________________
🏗️ Arquitectura del Código
El código está organizado siguiendo el principio de modularización: cada función tiene una responsabilidad única y específica.
Módulos principales:
•	Carga de datos: cargar_datos()
•	Búsqueda: buscar_pais()
•	Filtros: filtrar_por_continente(), filtrar_por_poblacion(), filtrar_por_superficie()
•	Ordenamientos: ordenar_paises(), mostrar_ordenados()
•	Estadísticas: mostrar_estadisticas(), calcular_densidad()
•	Visualización: mostrar_pais(), mostrar_menu()
•	Control: main() - Función principal con bucle del menú
________________________________________
📊 Dataset
El archivo paises.csv contiene información de 195 países con los siguientes campos:
Campo	Tipo	Descripción
nombre	string	Nombre del país
poblacion	int	Población total
superficie	int	Superficie en km²
continente	string	Continente al que pertenece
Distribución por continente:
•	🌍 África: 54 países
•	🌎 América: 35 países
•	🌏 Asia: 49 países
•	🇪🇺 Europa: 44 países
•	🏝️ Oceanía: 14 países
________________________________________
🔧 Manejo de Errores
El sistema implementa validaciones y manejo de errores para:
•	✅ Archivo CSV no encontrado
•	✅ Datos con formato incorrecto en el CSV
•	✅ Entradas inválidas del usuario (números fuera de rango, texto en lugar de números)
•	✅ Rangos inválidos (mínimo mayor que máximo)
•	✅ Búsquedas sin resultados
•	✅ Opciones de menú inexistentes
________________________________________
📚 Conceptos Aplicados
Este proyecto implementa los siguientes conceptos de Programación 1:
•	Listas: Para almacenar colecciones de países
•	Diccionarios: Para modelar cada país con sus atributos
•	Funciones: Modularización y reutilización de código
•	Condicionales: Control de flujo y validaciones
•	Bucles: Iteración sobre datos y menú principal
•	Manejo de archivos: Lectura de CSV con el módulo csv
•	Manejo de excepciones: Try-except para errores
•	Ordenamiento: Uso de sorted() con función lambda
•	Estadísticas: Cálculos con sum(), max(), min(), len()
________________________________________
📄 Documentación Adicional
•	Marco Teórico: Ver archivo Marco_Teorico.docx para fundamentos teóricos detallados
•	Conclusiones: Ver archivo Conclusiones.docx con aprendizajes del proyecto
•	Video Tutorial: [Enlace al video en YouTube/Drive]
________________________________________
🎯 Criterios de Evaluación Cumplidos
Criterio	Estado
Funcionalidad completa (búsqueda, filtros, ordenamiento, estadísticas)	✅
Uso correcto de listas y diccionarios	✅
Código modularizado (una función = una responsabilidad)	✅
Manejo de errores con try-except	✅
Código comentado y legible	✅
Lectura robusta de archivos CSV	✅
Validaciones de entrada	✅
README completo y detallado	✅
Repositorio público en GitHub	✅
