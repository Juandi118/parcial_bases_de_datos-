import os
import pandas as pd
import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import argparse
import time
 
class DataFiles:
    def __init__(self, *filenames):
        self.filenames = filenames
 
    def read_files(self):
        if not self.filenames:
            print("No se ingresó ningún archivo.")
            return
 
        for filename in self.filenames:
            if not os.path.isabs(filename):
                filename = os.path.join(os.getcwd(), filename)
 
            try:
                with open(filename) as f:
                    data = f.read()
                    print(f"Archivo {filename} leído exitosamente.")
                    # procesar los datos aquí
            except FileNotFoundError:
                print(f"Error: el archivo {filename} no fue encontrado.")


#definimos los decoradores



#METODO DECORADOR PARA CALCULAR EL TIEMPO DE VISION DE LA GRAFICA
def decorador1(funcion):

    def tiempoCrear(self,**kwargs):

        print("SE INICIO LA VISUALIZACION DE LA GRAFICA".center(100,"#"))

        inicio = time.time()

        funcion(self,**kwargs)

        final = time.time()

        print("\n")
        print("LA GRAFICA SE HA CERRADO, TIEMPO TOTAL DE VIZUALIZACION: {} SEGUNDOS.".format(final-inicio))
        print("\n")
    
    return tiempoCrear




#Metodo decorador para avisar al usuario que entro a una opcion en la cual se modificara la base de datos.
def decorador2(funcion):

    def tiempoCrear(self):

        print("SE ESTA MODIFICANDO LA BASE DE DATOS")

        funcion(self)

        print("\n")
        print("PROCESO EN LA BASE DE DATOS FINALIZADO")
        print("\n")

    return tiempoCrear



#Construccion de la clase principal 
class Database:
    def __init__(self, filepaths):
        if filepaths:
            self.filepaths = filepaths
        else:
            self.filepaths = [os.path.join(os.getcwd(), f) for f in os.listdir() if os.path.isfile(f) and f.endswith(".txt")]
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    @decorador2 #uso del decorador 2 para brindar mensajes de informacion
    def generate(self):
        # Implementación de la generación de la base de datos
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")
 
        for filepath in self.filepaths:
            with open(filepath, "r") as f:
                data = f.read().strip().split("\n")
                data = [(i+1, d) for i, d in enumerate(data)]
                self.cursor.executemany("INSERT INTO data VALUES (?, ?)", data)
 
        self.db.commit()
        print("\n BASE DE DATOS GENERADA CORRECTAMENTE \n")

        


    @decorador2    #uso del decorador 2 para brindar mensajes de informacion
    def llenar(self):
        # Generar tabla team
        self.cursor.execute("CREATE TABLE IF NOT EXISTS team (id INTEGER PRIMARY KEY, name TEXT UNIQUE, headquarters TEXT)")
        self.cursor.execute("INSERT OR IGNORE INTO team (id, name, headquarters) VALUES (1, 'preventers', 'Sharp tower')")
        self.cursor.execute("INSERT OR IGNORE INTO team (id, name, headquarters) VALUES (2, 'z-force', 'Sister margaret’s bar')")
 
        # Generar tabla hero
        self.cursor.execute("CREATE TABLE IF NOT EXISTS hero (id INTEGER PRIMARY KEY, name TEXT, secret_name TEXT, age INTEGER, team_id INTEGER, FOREIGN KEY(team_id) REFERENCES team(id))")
        self.cursor.execute("INSERT OR IGNORE INTO hero (id, name, secret_name, age, team_id) VALUES (1, 'Deadond', 'Dive Wilson', NULL, 2)")
        self.cursor.execute("INSERT OR IGNORE INTO hero (id, name, secret_name, age, team_id) VALUES (2, 'Rusty man', 'Tommy Sharp', 48, 1)")
        self.cursor.execute("INSERT OR IGNORE INTO hero (id, name, secret_name, age, team_id) VALUES (3, 'Spider boy', 'Pedro parqueador', NULL, 1)")
 
        self.db.commit()
        print("\n BASE DE DATOS LLENADA CORRECTAMENTE.\n")

    @decorador2    #uso del decorador 2 para brindar mensajes de informacion
    def join(self):
        # Unir tabla team y hero
        self.cursor.execute("SELECT hero.id, hero.name, hero.secret_name, hero.age, team.name, team.headquarters FROM hero INNER JOIN team ON hero.team_id = team.id")
        print("\nSE HA REALIZADO EL JOIN CON EXITO\n")
        return self.cursor.fetchall()
 
    def read(self):
        # Implementación de la lectura de la base de datos
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()
 
    def close(self):
        # Cerrar la conexión a la base de datos
        self.db.close()
 
 
    #Metodo para calcular la regresion lineal.    
    def regreLineal(self):
 
        global x1
        global y1
        global xlist
        global ylist
        global regrecionLineal
        global m
        global b
        global r2
 
        x1 =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        y1= [0,1,2,6,7,8,4,9,14,6,17,19,11,19,13,10]
        n = len(x1)
 
        xlist = np.array(x1)
        ylist = np.array(y1)
        sumx = sum(x1)
        sumy = sum(y1)
 
        sumx2 = sum(xlist*xlist)
        sumy2 = sum(ylist*ylist)
        sumxy = sum(xlist*ylist)
 
        promx = sumx/n
        promy = sumy/n
        m = (sumx*sumy-n*sumxy)/(sumx**2 -n*sumx2)
        b = promy-m*promx
 
        regrecionLineal = m*xlist+b #puntos para graficar
 
     #   print(regrecionLineal) #verificar que se tenga todo
 
        sigmax = np.sqrt((sumx2/n) - promx**2)
        sigmay = np.sqrt((sumy2/n) - promy**2)
        sigmaxy = (sumxy/n) - (promx*promy)
        r2 = (sigmaxy/(sigmax*sigmay))**2
 
      #  print("el coeficiente de regrecion lineal es:  {}".format(r2))
 
    #Metodo para graficar la regresion lineal
    @decorador1 #decorador para la grafica      
    def graficarRLineal(self,**kwagrs):

        color1=0
        color2=0
        colores = ["b","g","w","r","c","m","y","k"]
        bandera =False



        #codigo para utilizar los kwargs
        if len(kwagrs) !=0:
            
            if "color1" in kwagrs.keys():

                print("llega hasta qui")

                aux = kwagrs.get("color1")
                
                if aux in colores:

                    print("entro a ver colores")
                    bandera = True
                    color1= kwagrs.get("color1")
                else:
                    color1="g"

            else:

                color1="g"
        
            
            if "color2" in kwagrs.keys():

                print("llega segunda opcion")

                aux = kwagrs.get("color2")
                
                if aux in colores:
                    bandera = True
                    color2= kwagrs.get("color2")
                else:
                    color2="b"
                    
            else:
                color2="b"
        
        else:
           
            bandera = True
            color1="g"
            color2="b"

        
        if bandera:
            plt.plot(xlist, ylist, 'o', label='datos',color=color1)
            plt.plot(xlist, m*xlist+b, color=color2, label="ajuste, f(x)= {}*x+{}".format(m,b))
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title("El coeficiente de regrecion lineal es: {}".format(r2))
            plt.grid()
            plt.legend()
            plt.show()
        else:

            print("VALOR INCORRECTO, VERIFIQUE LOS KWAGRS")
 
 
 
 
    #metodo para generar el grafico de la integral y la derivada de una funcion, la cual es una expresion lambda
    @decorador1 #decorador para la grafica
    def graficarIntegralDerv(self, **kwargs):

        fun = 0
        stringFun = 0
        bandera= False

        aux = kwargs.keys()

        if "funcion" in aux:
            fun = kwargs.get("funcion")
            if "nombre" in aux:
                stringFun = kwargs.get("nombre")
                bandera = True
        elif "nombre" in aux:
            fun = kwargs.get("nombre")
            if "funcion" in aux:
                stringFun = kwargs.get("funcion")
                bandera = True

        if bandera:         
            #primero calculamos la derivada
            X= sp.symbols('X')
    
            derivada =sp.diff(fun(X),X)
    
            integral = sp.integrate(fun(X),X)
    
        # print(derivada)
        #  print(integral)
    
    
            #graficar ambas funciones:
    
    
        
            rango = np.linspace(-15,15,100)  
           
           # print(type(rango[0]))
            #print(type(0.2525))
    
    
        #  print(derivada.evalf(subs={X: 1}))
    
            #calcular puntos para graficar la derivada
            dy = list(map(lambda x: derivada.evalf(subs={X: x}),rango))
    
            dy = list(map(lambda x: float(x),dy))
    
    
            #calcular puntos para graficar la funcion
            fy = list(map(lambda x: sp.Subs.subs(fun(X),X,x),rango))


            #print("this is sol {}".format(type(fy[0])))
    
            fy = list(map(lambda x: float(x),fy))
    
            rango = np.array(rango)
            fy = np.array(fy)
        # print("this is sol {}".format(sol))
            plt.plot(rango,fy,label='f(x): {}'.format(stringFun))
            plt.plot(rango,dy, label='derivada de f(x): {}'.format(derivada))
            plt.title("Derivada e Integral para la funcion: {}".format(stringFun))
            plt.fill_between(rango,fy, where =(-50<=rango)&(rango<=50),color='g',alpha=0.4,label='Integral de f(x): {}'.format(integral)) #relleno para mostrar graficamente la integral
            plt.grid()
            plt.legend()
            plt.show()
        else:
            print("\nNO SE PASARON LOS ARGUMENTOS SUFICIENTES, SE REQUIERE LA FUNCION Y UN NOMBRE (PUEDE SER LA FUNCION MISMA EN STRING)\n")
 
 
 
#Menu para cargar el archivo por ubicacion
def menuCarga():
 
  print("Ingrese la ubicación de los archivos (o presione Enter para usar la ruta actual):")
  ubicacion = input().strip()
 
  if ubicacion:
      archivos = input("Ingrese los nombres de los archivos separados por comas: ").split(",")
      df = DataFiles(*archivos)
  else:
      df = DataFiles()
 
  df.read_files()
 
 
#Metodo para escojer la funcion definida, la cual se utilizara para calcular su derivada e integral
#NOTA: EL SIGUIENTE METODO UTILIZA LA CLASE QUE HEMOS ESTADO CONSTRUYENDO  (Database) ANTERIORMENTE, NO CONFUNDIR CON METOODOS DE CLASE.    
def menuGrafico():
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse para leer archivos y generar una base de datos.")
    parser.add_argument("-f", "--files", nargs="*", help="Lista de archivos a procesar. Si no se especifica, se procesan todos los archivos TXT de la ruta actual.")
    args = parser.parse_args()
 
 
    X= sp.symbols('X')
    objclase = Database(args.files) #objeto de la clase Database
 
    a =lambda x: X**2 +3*X -4
 
    b = lambda x: sp.cos(x) - x**2
 
    c = lambda x: sp.sin(x)**2 - 2*sp.sin(x) + x
    while True:
            print("ESCOJA UNA FUNCION PARA GRAFICAR SU DERIVADA Y SU INTEGRAL".center(100,"-"))
 
            print("a. x^2 + 3*x -4 \n b. cos(x) - x*2 \n c. sin(x)*2 - 2*sin(x) + x\n d. Atras")
            ans = input("Escoje una opcion: " )
 
            if (ans =="a" or ans =="A"):
 
                objclase.graficarIntegralDerv(funcion= a,nombre="x^2 + 3*x -4")
                menuGrafico()
 
                break
            elif (ans =="b" or ans =="B"):
 
                objclase.graficarIntegralDerv(funcion= b,nombre="cos(x) - x**2")
                menuGrafico()
                break
            elif (ans =="c" or ans =="C"):
 
                objclase.graficarIntegralDerv(funcion=c,nombre="sin(x)**2 - 2*sin(x) + x")
                menuGrafico()
                break
            elif (ans =="d" or ans =="D"):
 
                menuPuntosGraficos()
                break
            else:
                print("OPCION ERRONEA, ESCOJA UNA OPCION CORRECTA")
 
 
 
#metodo main para visualizar las graficas del punto 11,12 y 13
#NOTA: EL SIGUIENTE METODO UTILIZA LA CLASE QUE HEMOS ESTADO CONSTRUYENDO  (Database) ANTERIORMENTE, NO CONFUNDIR CON METOODOS DE CLASE.
 
 
def menuPuntosGraficos():
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse para leer archivos y generar una base de datos.")
    parser.add_argument("-f", "--files", nargs="*", help="Lista de archivos a procesar. Si no se especifica, se procesan todos los archivos TXT de la ruta actual.")
    args = parser.parse_args()
 
    objclase = Database(args.files)
 
    while True:
 
        print("APP PARA VISUALIZAR LOS PUNTOS 12 Y 13".center(100,"*"))
        print("a. PUNTO 12\n b. PUNTO 13\n c. ATRAS. \n")
 
        ans = input("ESCOJA UNA OPCION: ")
 
 
        if (ans =="a" or ans =="A"):
 
            objclase.regreLineal()
            objclase.graficarRLineal(color1="k", color2="r")   #la funcion tiene kwargs de color y color2 por defecto estan en verde y azul
            menuPuntosGraficos()
            break
        elif (ans =="b" or ans =="B"):
 
            menuGrafico()
            break
 
        elif (ans =="c" or ans =="C"):
 
            menuPrincipal()
            break
 
        else:
            print("OPCION ERRONEA, ESCOJA UNA OPCION CORRECTA")
 
 
#Metodo para escoger la opcion que se desee realizar con la clase construida
#NOTA: EL SIGUIENTE METODO UTILIZA LA CLASE QUE HEMOS ESTADO CONSTRUYENDO  (Database) ANTERIORMENTE, NO CONFUNDIR CON METOODOS DE CLASE.
 
def menuPrincipal():
    parser = argparse.ArgumentParser(description="Ejemplo de uso de argparse para leer archivos y generar una base de datos.")
    parser.add_argument("-f", "--files", nargs="*", help="Lista de archivos a procesar. Si no se especifica, se procesan todos los archivos TXT de la ruta actual.")
    args = parser.parse_args()
 
 
    db = Database(args.files)
 
    # Ciclo para mostrar el menú y procesar la selección del usuario
    while True:
        print("APLICACION PARA LA CLASE DATABASE".center(100,"-"))
        print("¿Qué acción deseas realizar? \n 1. Generar base de datos \n 2. Llenar base de datos \n 3. unir tablas a partir de sus id (join)  \n 4. Leer base de datos \n" +
                " 5. visualizar puntos 12 y 13 \n 6. Salir.")
 
        # Pedir al usuario que seleccione una opción
       
 
        # Procesar la selección del usuario
        try:

            selection = int(input("Selecciona una opción: "))
 
            if selection == 1:
                db.generate()
              
            elif selection == 2:
                db.llenar()
               
            elif selection == 3:
                db.join()
              
            elif selection == 4:
                data = db.join()
                print("\nTABLAS UNIDAS: \n")
                for row in data:
                    print(row)
            elif selection == 5:
 
                menuPuntosGraficos()
                break
            elif selection == 6:
                db.close()
                print("¡Hasta luego!")
                break
 
            else:
                print("Opción inválida. Inténtalo de nuevo.")
        
        except ValueError:
           print("dijite solo numeros.")
        except Exception as e:
            print(f"Ha ocurrido un error: {str(e)}")
 
 
#Metodo main para correr el programa para visualizar los puntos 12 y 13
 
def main():
    menuCarga()
    menuPrincipal()
 
main()
