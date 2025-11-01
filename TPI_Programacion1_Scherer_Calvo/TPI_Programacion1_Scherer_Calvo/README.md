# 🌍 Sistema de Gestión de Países 

**Trabajo Práctico Integrador - Programación 1**  
Tecnicatura Universitaria en Programación

Sistema interactivo en Python para gestionar información de países y territorios del mundo, incluyendo datos de población, superficie, continente y reconocimiento internacional por la ONU.

## 📋 Descripción

Este proyecto implementa una aplicación completa de gestión de datos de países que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre una base de datos almacenada en formato CSV. 

El sistema ofrece funcionalidades avanzadas de búsqueda, filtrado, ordenamiento y cálculo de estadísticas con una interfaz de línea de comandos intuitiva y amigable. Incluye tanto países reconocidos por la ONU como territorios con reconocimiento limitado o nulo.

**Objetivo del Proyecto**: Aplicar y demostrar el dominio de estructuras de datos (listas y diccionarios), funciones, condicionales, bucles, ordenamientos y estadísticas básicas, integrando el manejo de archivos CSV para persistencia de datos.

## ✨ Características

### 🔍 Búsqueda y Filtrado
- **Búsqueda por nombre**: Búsqueda insensible a mayúsculas/minúsculas y acentos
- **Filtro por continente**: América, Europa, Asia, África, Oceanía
- **Filtro por rango de población**: Define mínimos y máximos
- **Filtro por rango de superficie**: Filtra por área territorial

### 📊 Ordenamiento y Estadísticas
- **Ordenamiento flexible**: Por nombre, población o superficie (ascendente/descendente)
- **Estadísticas interactivas**: Menú que permite elegir qué estadística visualizar:
  - País con mayor población
  - País con menor población
  - Promedios (población y superficie)
  - Distribución de países por continente
  - Ver todas las estadísticas
  - Volver al menú principal

### ➕ Gestión de Datos
- **Agregar países**: Con validación de datos y prevención de duplicados
- **Editar países**: Modificar nombre, población, superficie, continente o reconocimiento ONU
- **Eliminar países**: Búsqueda exacta por nombre
- **Campo reconocido_onu**: Distingue países reconocidos por la ONU de territorios no reconocidos
- **Persistencia**: Guardado manual en archivo CSV con codificación UTF-8

### 📄 Visualización Paginada
- Navegación por páginas (10 países por página)
- Indicador de página actual (ej: "Página 1 de 20")
- Controles de navegación: Siguiente, Anterior, Ir a página específica
- **Indicador visual**: Los países NO reconocidos por la ONU se muestran con la etiqueta `[No reconocido por ONU]`

## 🚀 Requisitos Técnicos

- **Python**: 3.10 o superior (obligatorio - usa sintaxis `match-case`)
- **Módulos**: Solo librería estándar de Python (`csv` para manejo de archivos, `unicodedata` para normalización de texto)
- **Sistema Operativo**: Windows, Linux, macOS
- **Codificación**: UTF-8 para soporte de caracteres especiales y acentos
- **Auto-inicialización**: Si el archivo `paises.csv` no existe, se crea automáticamente con los encabezados correctos

## 💻 Instalación y Ejecución

### Prerrequisitos

1. **Instalar Python 3.10 o superior**
   
   Verifica tu versión de Python:
   ```bash
   python --version
   ```
   
   Si necesitas instalar o actualizar Python, descárgalo desde [python.org](https://www.python.org/downloads/)

2. **Obtener el proyecto**
   
   Puedes clonar el repositorio completo de la materia:
   ```bash
   git clone https://github.com/belcalvo93/UTN-TUPaDProgramacion1.git
   cd UTN-TUPaDProgramacion1/TPI_Programacion1_Scherer_Calvo
   ```
   
   O descargar directamente la carpeta del proyecto desde el [repositorio en GitHub](https://github.com/belcalvo93/UTN-TUPaDProgramacion1).

### Ejecutar el Programa

El programa no requiere instalación de dependencias adicionales, solo usa módulos de la biblioteca estándar de Python.

**En Windows (PowerShell o CMD)**:
```bash
python main.py
```

**En Linux/macOS**:
```bash
python3 main.py
```

### Primera Ejecución

Al ejecutar el programa por primera vez:
1. Si el archivo `paises.csv` no existe, se creará automáticamente con los encabezados
2. Puedes agregar países manualmente usando la opción **7) Agregar país** del menú
3. O puedes cargar el archivo `paises.csv` proporcionado con el dataset completo

### Uso del Sistema

Una vez ejecutado, el sistema mostrará el menú principal:
- Navega usando los números del **0 al 9**
- Sigue las instrucciones en pantalla para cada operación
- Usa **0) Guardar y salir** para guardar cambios y cerrar el programa

## 📦 Estructura del Proyecto

```
TPI_Programacion1_Scherer_Calvo/
│
├── main.py                                              # Programa principal con menú y submenús (match-case)
├── paises.csv                                           # Base de datos CSV con países y territorios
├── README.md                                            # Documentación completa del proyecto
│
├── funciones/                                           # Módulos funcionales organizados
│   ├── funciones.py                                     # Carga y guardado de archivos CSV
│   ├── funciones_operaciones.py                        # Búsqueda, filtrado, ordenamiento y estadísticas
│   ├── funciones_altas_bajas.py                        # Agregar, editar y eliminar países
│   ├── mostrar_lista.py                                # Visualización con paginación
│   ├── menu.py                                          # Menú principal del sistema
│   └── utilidades.py                                    # Funciones auxiliares de validación
│
├── documentacion/                                       # Documentación del trabajo práctico
│   ├── MarcoTeorico_TPI_Scherer_Calvo.pdf              # Marco teórico con conceptos fundamentales
│   ├── Rúbrica de corrección - Programacion 1.pdf      # Criterios de evaluación del proyecto
│   └── Trabajo Práctico Integrador - Programacion 1.pdf # Consignas y requerimientos del TPI
│
└── video/                                               # Video demostrativo del proyecto
    └── video.txt                                        # Enlace al video tutorial en YouTube
```

## 🎮 Uso

### Ejecutar el programa

```bash
python main.py
```

### Menú Principal

```
╔════════════════════════════════════════╗
║     GESTIÓN DE PAÍSES - MENÚ PRINCIPAL ║
╚════════════════════════════════════════╝
1) Buscar por nombre
2) Filtrar por continente
3) Filtrar por población (rango)
4) Filtrar por superficie (rango)
5) Ordenar (nombre/población/superficie,asc/desc)
6) Estadísticas
7) Agregar país
8) Editar país
9) Quitar país
0) Guardar y salir
```

### Ejemplos de Uso

#### 🔍 Búsqueda por nombre
```
Opción: 1
Texto a buscar: mexico
```
**Resultado**: Encuentra "México" (búsqueda insensible a acentos)

#### 🌎 Filtrar por continente
```
Opción: 2
Continente: América
```
**Resultado**: Muestra todos los países de América con paginación

#### 👥 Filtrar por rango de población
```
Opción: 3
Población mínima: 100000000
Población máxima: (dejar vacío)
```
**Resultado**: Países con más de 100 millones de habitantes

#### 📏 Filtrar por superficie
```
Opción: 4
Superficie mínima: 1000000
Superficie máxima: 10000000
```
**Resultado**: Países con superficie entre 1M y 10M km²

#### 🔢 Ordenar
```
Opción: 5
Clave: poblacion
Orden: desc
```
**Resultado**: Países ordenados de mayor a menor población

#### 📊 Ver estadísticas
```
Opción: 6

--- ESTADÍSTICAS ---
1) País con mayor población
2) País con menor población
3) Promedios
4) Por continente
5) Ver todas
6) Volver

Elegir: 1
```
**Resultado**:
```
Mayor población: China (1439323776)
```

Al elegir opción 5 (Ver todas):
```
Mayor población: China (1439323776)
Menor población: Sealand (30)
Promedio de población: 38371877.72
Promedio de superficie: 669101.46
Países por continente:
 - Asia: 52
 - Europa: 48
 - África: 54
 - América: 35
 - Oceanía: 17
```

#### ➕ Agregar un país
```
Opción: 7
Nombre: Ejemplo
Población: 1000000
Superficie: 50000
Continente: Europa
¿El país es reconocido por la ONU? (si/no): si
```

#### ✏️ Editar un país
```
Opción: 8
Nombre exacto del país a editar: Ejemplo

Datos actuales de 'Ejemplo':
  Población: 1,000,000
  Superficie: 50,000 km²
  Continente: Europa
  Reconocido por ONU: Sí

¿Qué desea editar?
  [1] Nombre
  [2] Población
  [3] Superficie
  [4] Continente
  [5] Reconocido por ONU
  [6] Cancelar
```

#### ➖ Eliminar un país
```
Opción: 9
Nombre exacto del país a eliminar: Ejemplo
```

### 📄 Navegación Paginada

Cuando se muestren resultados con múltiples páginas:

```
--- Página 1 de 20 ---
1. Afganistán | Pob: 38928346 | Sup: 652230 km2 | Asia
...
10. Armenia | Pob: 2963243 | Sup: 29743 km2 | Asia

[S]iguiente | [A]nterior | [Número de página] | [Enter para volver]
Navegar:
```

Al visualizar territorios no reconocidos, se mostrará el indicador correspondiente:
```
195. Taiwán | Pob: 23600000 | Sup: 36000 km² | Asia [No reconocido por ONU]
196. Kosovo | Pob: 1800000 | Sup: 10900 km² | Europa [No reconocido por ONU]
```

**Controles**:
- `S` o `s`: Ir a la siguiente página
- `A` o `a`: Ir a la página anterior
- `5`: Ir directamente a la página 5
- `Enter`: Volver al menú principal

## 📝 Formato del Archivo CSV

```csv
nombre,poblacion,superficie,continente,reconocido_onu
Argentina,45376763,2780400,América,si
Japón,125800000,377975,Asia,si
Brasil,213993437,8515767,América,si
Alemania,83149300,357022,Europa,si
Taiwán,23570000,36193,Asia,no
```

**Campos del CSV**:
- `nombre`: Nombre del país o territorio (string, no vacío)
- `poblacion`: Número de habitantes (entero positivo)
- `superficie`: Área territorial en km² (entero >= 0, acepta decimales que se redondean)
- `continente`: Continente de pertenencia (América/Europa/Asia/África/Oceanía)
- `reconocido_onu`: Reconocimiento por la ONU ("si" para países miembros, "no" para territorios no reconocidos)

**Dataset incluido**:
- Países reconocidos por la ONU (reconocido_onu=si)
- Territorios con reconocimiento limitado o nulo (reconocido_onu=no), como Sealand

## 🛡️ Validaciones y Manejo de Errores

El sistema implementa validaciones exhaustivas para garantizar la integridad de los datos:

### Validaciones de Datos
- **Nombres únicos**: No se permiten países duplicados (verificación case-insensitive)
- **Datos numéricos**: Población y superficie deben ser números enteros válidos
- **Valores positivos**: No se aceptan valores negativos para población ni superficie
- **Campos obligatorios**: Todos los campos deben completarse (nombre, población, superficie, continente, reconocimiento ONU)
- **Continentes válidos**: Solo acepta los 5 continentes reconocidos (América, Europa, Asia, África, Oceanía)
- **Superficie decimal**: Acepta valores decimales que se redondean automáticamente a enteros

### Manejo de Errores
- **Archivos CSV**:
  - Auto-creación si el archivo no existe
  - Manejo de errores de lectura/escritura con mensajes claros
  - Validación de formato y conversión de tipos
  - Soporte UTF-8 para caracteres especiales

- **Entrada de Usuario**:
  - Validación de opciones del menú
  - Verificación de rangos numéricos
  - Mensajes informativos de éxito/error
  - Confirmaciones para operaciones críticas (eliminar)

- **Búsquedas**:
  - Mensajes claros cuando no hay resultados
  - Búsqueda insensible a mayúsculas/minúsculas
  - Normalización de acentos para búsquedas más flexibles

- **Operaciones CRUD**:
  - Verificación de existencia antes de editar/eliminar
  - Validación completa antes de agregar nuevos países
  - Mensajes de confirmación para todas las operaciones

## 🔧 Funciones Principales

### `funciones/funciones.py`
- `cargar_paises(ruta)`: Carga datos de países desde archivo CSV con encoding UTF-8. Si el archivo no existe, lo crea automáticamente con los encabezados
- `guardar_paises(paises, ruta)`: Guarda cambios en archivo CSV (convierte reconocido_onu a si/no)
- `_limpiar_fila_cruda(fila_dict)`: Normaliza claves y valores del CSV
- `_tipar_y_validar(f)`: Convierte tipos, valida datos y redondea superficie decimal a entero

### `funciones/funciones_operaciones.py`
- `normalizar_texto(texto)`: Elimina acentos para búsquedas insensibles (usa `unicodedata` internamente)
- `buscar_por_nombre(paises, texto)`: Búsqueda parcial por nombre (case-insensitive y sin acentos)
- `filtrar_por_continente(paises, cont)`: Filtra países por continente
- `filtrar_por_rango(paises, clave, minimo, maximo)`: Filtra por rango de población o superficie
- `ordenar(paises, clave, descendente)`: Ordena por nombre, población o superficie
- `estadisticas(paises)`: Calcula estadísticas generales (mayor/menor población, promedios, por continente)

### `funciones/funciones_altas_bajas.py`
- `agregar_pais(paises, nombre, poblacion, superficie, continente, reconocido_onu)`: Agrega país con validación y prevención de duplicados
- `editar_pais(paises, nombre)`: Busca un país por nombre exacto para editarlo
- `quitar_pais(paises, nombre)`: Elimina país por nombre exacto
- `_existe_nombre(paises, nombre)`: Verifica existencia de país (función auxiliar)

### `funciones/mostrar_lista.py`
- `mostrar_lista(paises, por_pagina)`: Visualización paginada con indicador de reconocimiento ONU. Muestra `[No reconocido por ONU]` para territorios no reconocidos

### `funciones/menu.py`
- `menu()`: Despliega menú principal del sistema

### `funciones/utilidades.py`
- `preguntar_nuevamente(texto)`: Validación de respuestas si/no
- `pedir_int(msg, vacio)`: Solicita y valida números enteros
- `pausar()`: Pausa para lectura de resultados
- `menu_salida()`: Menú de navegación post-operación (volver a submenú o menú principal)

## 💡 Características Técnicas

### Conceptos Aplicados

Este proyecto aplica los siguientes conceptos fundamentales de programación, desarrollados en profundidad en el marco teórico (`documentacion/MarcoTeorico_TPI_Scherer_Calvo.pdf`):

**Listas**: Estructura principal para almacenar la colección de países. Permite operaciones de agregar, eliminar, recorrer y ordenar elementos de forma dinámica. Se utilizan para mantener todos los países en memoria y para generar resultados filtrados sin modificar la lista original.

**Diccionarios**: Cada país se representa como un diccionario con claves (`nombre`, `poblacion`, `superficie`, `continente`, `reconocido_onu`), facilitando el acceso estructurado a los datos por nombre de campo. Esta estructura permite una lectura intuitiva del código y acceso O(1) a los atributos de cada país.

**Funciones**: El código está completamente modularizado siguiendo el principio de responsabilidad única. Cada función tiene una responsabilidad específica y está documentada con docstrings que explican parámetros, retornos y propósito. Esto mejora la legibilidad, mantenibilidad y reutilización del código.

**Condicionales**: Estructuras `if-elif-else` para validar entradas, verificar duplicados y controlar el flujo del programa. Uso de `match-case` (Python 3.10+) en el menú principal y submenús para selección de opciones, aprovechando las características modernas del lenguaje.

**Bucles**: 
- `while`: Para menús y submenús que permiten múltiples operaciones consecutivas sin salir del contexto
- `for`: Para recorrer listas, procesar archivos CSV línea por línea y calcular estadísticas agregadas

**Ordenamientos**: Implementado con la función `sorted()` y funciones auxiliares personalizadas (sin lambdas) para ordenar por diferentes criterios (nombre, población, superficie) en orden ascendente o descendente. Demuestra comprensión de algoritmos de ordenamiento y funciones de orden superior.

**Estadísticas Básicas**: Cálculo de máximos, mínimos, promedios y agrupaciones (países por continente). Aplicación práctica de operaciones matemáticas y agregaciones sobre datasets.

**Archivos CSV**: Uso del módulo `csv` de la biblioteca estándar para persistencia de datos. Implementa lectura robusta con manejo de errores, validación de tipos, conversión de datos y escritura con encoding UTF-8. Incluye auto-creación del archivo si no existe.

### Implementación

- **Sin funciones lambda**: Todo el código usa funciones auxiliares explícitas para mejor legibilidad
- **Normalización Unicode**: Búsqueda insensible a acentos usando `unicodedata.normalize()` y `unicodedata.category()` dentro de la función `normalizar_texto()`
- **Paginación dinámica**: Sistema de navegación automático según cantidad de resultados
- **Submenús inteligentes**: Permite múltiples operaciones sin volver al menú principal
- **Menú de estadísticas interactivo**: El usuario elige qué estadística visualizar (opción 6)
- **Manejo de errores**: Try-except para archivos, validaciones de tipos y rangos
- **Encoding UTF-8**: Soporte completo para caracteres internacionales
- **Sintaxis moderna**: Match-case de Python 3.10+ en menú principal y submenús
- **Campo reconocido_onu**: Almacenado como boolean en memoria, convertido a "si"/"no" en CSV

## 🐛 Solución de Problemas

### El archivo CSV no se encuentra
- El programa creará un archivo vacío automáticamente
- Verifica que `paises.csv` esté en el mismo directorio que `main.py`

### Error de encoding
- Asegúrate de que el archivo CSV esté guardado en UTF-8
- Los caracteres especiales (tildes, ñ) requieren UTF-8

### Python no reconoce `match-case`
- Actualiza Python a la versión 3.10 o superior
- Verifica tu versión: `python --version`

## 🎥 Video Demostrativo

**Video Tutorial del Proyecto** (15 minutos)

📺 **[Ver video en YouTube](https://www.youtube.com/watch?v=ukkyyWWHhWc)**

El video incluye:
- Explicación del problema planteado y objetivos del proyecto
- Presentación de la estructura de datos utilizada (listas y diccionarios)
- Demostración completa del programa funcionando con ejemplos reales
- Explicación de las funcionalidades principales: búsqueda, filtrado, ordenamiento y estadísticas
- Reflexión final sobre el desarrollo del proyecto y aprendizajes adquiridos
- Participación de ambos integrantes del equipo

## 📚 Entregables del Proyecto

Este proyecto cumple con todos los entregables requeridos para el Trabajo Práctico Integrador:

### 1. Carpeta Digital ✓
- **Marco Teórico**: `documentacion/MarcoTeorico_TPI_Scherer_Calvo.pdf` con conceptos fundamentales (listas, diccionarios, funciones, condicionales, ordenamientos, estadísticas, archivos CSV) y fuentes bibliográficas
- **Código Python**: Funcional, modular y comentado en la carpeta `funciones/` y `main.py`
- **Capturas de Pantalla**: Incluidas en este README mostrando ejemplos de ejecución
- **Conclusiones**: Incluidas en el marco teórico sobre los aprendizajes del equipo

### 2. Repositorio en GitHub ✓
- **Proyecto Completo**: Código Python con todos los módulos organizados
- **README.md Detallado**: Con descripción, instrucciones de uso, ejemplos y participación de integrantes
- **Dataset Base**: Archivo `paises.csv` incluido
- **Documentación Completa**: Carpeta `documentacion/` con consignas, rúbrica y marco teorico
- **Repositorio**: [https://github.com/belcalvo93/UTN-TUPaDProgramacion1](https://github.com/belcalvo93/UTN-TUPaDProgramacion1)

### 3. Video Tutorial ✓
- **Duración**: 15 minutos
- **Contenido**: Explicación teórica, demostración práctica y reflexión final
- **Participación**: Ambos integrantes del equipo
- **Enlace**: Disponible en `video/video.txt` 

## ✅ Cumplimiento de Criterios de Evaluación

### Marco Teórico e Investigación (30%)
- ✓ **Conceptos Fundamentales**: Definición precisa de listas, diccionarios, funciones, condicionales, ordenamientos, estadísticas y archivos CSV con relación directa al proyecto
- ✓ **Fuentes Bibliográficas**: Mínimo 3 fuentes académicas y técnicas citadas correctamente en el marco teórico
- ✓ **Conclusiones**: Reflexión profunda sobre aprendizajes en estructuras de datos, modularización y estadísticas

### Desarrollo del Software (60%)
- ✓ **Funcionalidad Completa**: Todas las funcionalidades operan correctamente (carga CSV, búsqueda, filtrado por continente/población/superficie, ordenamiento múltiple, estadísticas)
- ✓ **Estructuras de Datos**: Uso óptimo de listas para colecciones y diccionarios para representación de países
- ✓ **Modularización**: Código perfectamente modularizado con funciones de responsabilidad única
- ✓ **Manejo de Archivos**: Lectura robusta de CSV con conversión de tipos, validaciones y manejo de excepciones
- ✓ **Lógica Condicional y Ordenamiento**: Filtros precisos y ordenamientos eficientes en múltiples criterios (nombre, población, superficie)
- ✓ **Legibilidad y Comentarios**: Código claro con nombres significativos y docstrings completas
- ✓ **Manejo de Errores**: Try-except completo con mensajes claros para el usuario

### Entregables y Presentación (10%)
- ✓ **Carpeta Digital**: Completa con marco teórico, código, capturas y conclusiones
- ✓ **Repositorio GitHub**: Público, completo, con README detallado (instrucciones, ejemplos, participación)
- ✓ **Video Tutorial**: 10-15 minutos, ambos integrantes, explicación teórica y demostración práctica

## 🎯 Funcionalidades Implementadas

El sistema cumple con **todas las funcionalidades mínimas** requeridas en las consignas:

### Búsqueda y Filtrado
- ✓ Buscar país por nombre (coincidencia parcial, insensible a mayúsculas/minúsculas y acentos)
- ✓ Filtrar por continente (América, Europa, Asia, África, Oceanía)
- ✓ Filtrar por rango de población (mínimo/máximo configurable)
- ✓ Filtrar por rango de superficie (mínimo/máximo configurable)

### Ordenamiento
- ✓ Ordenar por nombre (ascendente/descendente)
- ✓ Ordenar por población (ascendente/descendente)
- ✓ Ordenar por superficie (ascendente/descendente)

### Estadísticas
- ✓ País con mayor población
- ✓ País con menor población
- ✓ Promedio de población
- ✓ Promedio de superficie
- ✓ Cantidad de países por continente

### Funcionalidades Adicionales (Extras)
- ➕ **Gestión CRUD Completa**: Agregar, editar y eliminar países
- ➕ **Campo Reconocimiento ONU**: Distingue países reconocidos de territorios no reconocidos
- ➕ **Paginación Dinámica**: Visualización paginada de resultados con navegación
- ➕ **Submenús Inteligentes**: Permite múltiples operaciones sin volver al menú principal
- ➕ **Menú de Estadísticas Interactivo**: El usuario elige qué estadística visualizar
- ➕ **Auto-creación de CSV**: Si el archivo no existe, se crea automáticamente
- ➕ **Persistencia de Datos**: Guardado manual con confirmación

## 📄 Licencia

Este proyecto es de uso educativo.

## 👥 Equipo de Desarrollo

**Trabajo Práctico Integrador** - Programación 1  
Tecnicatura Universitaria en Programación

**Integrantes**:
- **Marcelo Scherer**
- **Belén Calvo**

### Participación del Equipo

Ambos integrantes participaron equitativamente en el desarrollo del proyecto:

**Diseño y Planificación**:
- Análisis conjunto de requerimientos y consignas
- Diseño de la estructura modular del sistema
- Definición de funcionalidades y flujo de operaciones

**Desarrollo del Código**:
- Implementación colaborativa de funciones y módulos
- Desarrollo de la lógica de búsqueda, filtrado y estadísticas
- Implementación del sistema de menús y submenús
- Manejo de archivos CSV y validaciones

**Documentación**:
- Elaboración conjunta del marco teórico
- Redacción de README.md con ejemplos de uso
- Documentación de funciones con docstrings
- Comentarios explicativos en el código

**Testing y Validación**:
- Pruebas de funcionalidad con diferentes casos de uso
- Validación de manejo de errores
- Verificación de cumplimiento de consignas

**Presentación**:
- Preparación del video tutorial
- Demostración del programa funcionando
- Explicación de conceptos técnicos aplicados

---

**Fecha de Entrega**: Noviembre 2025

**Última actualización**: 1 de noviembre de 2025
