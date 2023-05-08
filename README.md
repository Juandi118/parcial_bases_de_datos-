# parcial_bases_de_datos-



Este es un proyecto en Python que permite leer archivos CSV y generar una base de datos SQLite a partir de ellos. Además, ofrece diversas funcionalidades para manipular la base de datos, como llenarla con datos predefinidos, unir tablas mediante join y leer su contenido.

## Requisitos
Para poder ejecutar este código, es necesario tener instalados los siguientes paquetes:

* pandas
* numpy
* matplotlib
* sympy
* sqlite3
## Funcionamiento
El código se compone de dos clases: Databasearchivos y Database. La primera se encarga de leer los archivos CSV y almacenarlos en una lista de pandas dataframes. La segunda se encarga de generar la base de datos y realizar las operaciones sobre ella.

## Clase DataFiles
La clase DataFiles representa un conjunto de archivos de datos y proporciona un método para leer y procesar cada uno de estos archivos. Aquí está una explicación paso a paso de lo que hace esta clase:

La clase tiene un constructor llamado __init__ que toma argumentos variables llamados filenames. Este constructor inicializa el objeto DataFiles con una lista de nombres de archivo.

La clase también tiene un método llamado read_files, que lee y procesa cada archivo en la lista de nombres de archivo.

Si la lista de nombres de archivo está vacía, el método imprime un mensaje de que no se ingresó ningún archivo y regresa.

Si los nombres de archivo no son absolutos (es decir, no incluyen la ruta completa), el método construye la ruta completa utilizando os.path.join y el directorio actual os.getcwd().

El método luego usa un bloque try-except para manejar el caso en que un archivo no se encuentra. Si el archivo se encuentra, se abre y se lee utilizando with open(filename) as f:.

Los datos del archivo se leen utilizando el método f.read(). El método luego imprime un mensaje de que el archivo se ha leído correctamente y los datos se procesan a continuación.

Si el archivo no se encuentra, el método imprime un mensaje de error.

## Clase Database

La clase Database permite generar, llenar, unir y leer bases de datos SQLite3. Los métodos y atributos de la clase se explican a continuación:

* init(self, filepaths): El método constructor de la clase. Toma como entrada una lista de filepaths y crea una conexión a una base de datos SQLite3 llamada "database.db". Si no se proporcionan filepaths, se genera una lista de archivos .txt en el directorio actual y se toman como filepaths. También inicializa el atributo cursor de la conexión a la base de datos.

* generate(self): Método que genera una tabla llamada "data" en la base de datos y llena la tabla con los datos de los archivos indicados en los filepaths proporcionados en la inicialización de la clase o en la lista generada si no se proporcionó ninguno.

* llenar(self): Método que genera dos tablas en la base de datos ("team" y "hero") y las llena con datos específicos. En la tabla "team" se crean dos filas, mientras que en la tabla "hero" se crean tres filas. Estos datos son meramente ejemplificativos y pueden ser cambiados en el código.

* join(self): Método que realiza una unión (join) entre las tablas "team" y "hero" y devuelve los resultados de la consulta. Este método utiliza la cláusula INNER JOIN para combinar ambas tablas.

* read(self): Método que lee y devuelve todos los datos de la tabla "data" de la base de datos.

* close(self): Método que cierra la conexión a la base de datos.

Además, la clase utiliza un decorador (decorador2) para imprimir mensajes de información en los métodos "generate", "llenar" y "join".

* regreLineal: calcula la regresión lineal de una lista de puntos (x, y). Primero, se definen los valores de x1 y y1. Luego, se calculan la suma de los valores de x1 y y1, la suma de los cuadrados de los valores de x1 y y1, y la suma de los productos de los valores de x1 y y1. Con estos valores, se calcula la pendiente m y la ordenada al origen b de la regresión lineal. Finalmente, se define la función de regresión lineal regrecionLineal.

* graficarRLineal: grafica la regresión lineal calculada por el método regreLineal. El método tiene dos argumentos opcionales: color1 y color2. Estos argumentos permiten personalizar el color de los puntos de datos y de la línea de regresión, respectivamente. Si se proporcionan valores inválidos para color1 o color2, se utiliza el color verde para los puntos de datos y el color azul para la línea de regresión. La función utiliza la biblioteca Matplotlib para crear el gráfico.

* graficarIntegralDerv: grafica la función dada, su derivada y su integral. La función recibe un argumento obligatorio funcion, que debe ser una expresión lambda que defina la función a graficar. También puede recibir un argumento opcional nombre, que se utiliza para etiquetar la función en la leyenda del gráfico. El método utiliza la biblioteca SymPy para calcular la derivada e integral de la función dada. La función utiliza la biblioteca Matplotlib para crear el gráfico.


## Función menu()
menuCarga(): muestra un menú que permite al usuario cargar archivos de texto en la base de datos utilizando la clase Database.

menuPrincipal(): muestra un menú que permite al usuario realizar diferentes acciones en la base de datos, como generar una base de datos, llenar la base de datos, unir tablas a partir de sus ID (join), leer la base de datos o visualizar los puntos 12 y 13 utilizando la clase Database.

menuPuntosGraficos(): muestra un menú que permite al usuario elegir entre visualizar los puntos 12 y 13 de la base de datos utilizando la regresión lineal y la gráfica correspondiente, o volver al menú principal.

main(): es el método principal que ejecuta la aplicación llamando a los métodos menuCarga() y menuPrincipal().
