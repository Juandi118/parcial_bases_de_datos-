# parcial_bases_de_datos-



Este es un proyecto en Python que permite leer archivos CSV y generar una base de datos SQLite a partir de ellos. Además, ofrece diversas funcionalidades para manipular la base de datos, como llenarla con datos predefinidos, unir tablas mediante join y leer su contenido.

## Requisitos
Para poder ejecutar este código, es necesario tener instalados los siguientes paquetes:

#000000 pandas
numpy
matplotlib
sympy
sqlite3
## Funcionamiento
El código se compone de dos clases: Databasearchivos y Database. La primera se encarga de leer los archivos CSV y almacenarlos en una lista de pandas dataframes. La segunda se encarga de generar la base de datos y realizar las operaciones sobre ella.

## Clase Databasearchivos
La clase Databasearchivos recibe una lista de rutas a archivos CSV. Si no se proporciona ninguna ruta, buscará en el directorio actual todos los archivos con extensión .csv. Luego, leerá cada archivo y almacenará su contenido en una lista de pandas dataframes.

## Métodos
La clase Databasearchivos cuenta con el siguiente método:

read_files(): Este método se encarga de leer cada archivo CSV almacenado en la lista de rutas proporcionada al instanciar la clase, y almacenar su contenido en una lista de pandas dataframes.
Clase Database
La clase Database se encarga de generar una base de datos SQLite a partir de los archivos CSV leídos por la clase Databasearchivos. Además, permite realizar diversas operaciones sobre la base de datos, como llenarla con datos predefinidos, unir tablas a partir de sus identificadores (join) y leer su contenido.

## Métodos
La clase Database cuenta con los siguientes métodos:

init(*args): Este método inicializa la clase. Si se proporciona una lista de rutas a archivos CSV, las almacena en una lista. Si no se proporciona ninguna ruta, buscará en el directorio actual todos los archivos con extensión .csv. Además, crea una conexión a la base de datos SQLite.
generate(): Este método se encarga de generar la base de datos SQLite. Crea una tabla llamada data con dos columnas (id y value) y lee el contenido de cada archivo CSV almacenado en la lista de rutas proporcionada al instanciar la clase. Luego, inserta cada línea de cada archivo en la tabla data.
llenar(): Este método se encarga de llenar la base de datos con datos predefinidos. Crea dos tablas (team y hero) y las llena con algunos datos de ejemplo.
join(): Este método se encarga de unir las tablas hero y team a partir de sus identificadores (join). Retorna una lista con los registros resultantes.
read(): Este método se encarga de leer el contenido de la tabla data. Retorna una lista con los registros resultantes.
close(): Este método se encarga de cerrar la conexión a la base de datos SQLite.
## Función menu()
La función menu() se encarga de mostrar un menú al usuario y procesar sus selecciones. Primero, crea una instancia de la clase Database. Luego, muestra el menú con las siguientes opciones:

1: Generar base de datos
2: Llenar base de datos con datos predefinidos
3: Realizar join de tablas
4: Leer contenido de tabla data
5: Salir del programa
Al seleccionar una opción, se ejecuta el método correspondiente de la clase Database
