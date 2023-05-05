import os
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

class Database:
    def init(self, *args):
        if args:
            self.filepaths = args
        else:
            self.filepaths = [os.path.join(os.getcwd(), f) for f in os.listdir() if os.path.isfile(f)]
        self.db = sqlite3.connect("database.db")
        self.cursor = self.db.cursor()

    def generate(self):
        # Implementación de la generación de la base de datos
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)")

        for filepath in self.filepaths:
            with open(filepath, "r") as f:
                data = f.read().strip().split("\n")
                data = [(i+1, d) for i, d in enumerate(data)]
                self.cursor.executemany("INSERT INTO data VALUES (?, ?)", data)

        self.db.commit()

    def read(self):
        # Implementación de la lectura de la base de datos
        self.cursor.execute("SELECT * FROM data")
        return self.cursor.fetchall()

    def close(self):
        # Cerrar la conexión a la base de datos
        self.db.close()
        def init(self):
            self.db = sqlite3.connect("database.db")
            self.cursor = self.db.cursor()

    def generate(self):
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

    def join(self):
        # Unir tabla team y hero
        self.cursor.execute("SELECT hero.id, hero.name, hero.secret_name, hero.age, team.name, team.headquarters FROM hero INNER JOIN team ON hero.team_id = team.id")
        return self.cursor.fetchall()

    def close(self):
        # Cerrar la conexión a la base de datos
        self.db.close()
    
    def regreLineal(self):

        global x1
        global y1
        global xlist
        global ylist
        global regrecionLineal
        global m
        global b
        global r2

        x1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        y1= [1,2,2,4,5,4,6,4,6,7,9,10,11,12,10]
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
        
        print(regrecionLineal) #verificar que se tenga todo

        sigmax = np.sqrt((sumx2/n) - promx**2)
        sigmay = np.sqrt((sumy2/n) - promy**2)
        sigmaxy = (sumxy/n) - (promx*promy)
        r2 = (sigmaxy/(sigmax*sigmay))**2

        print("el coeficiente de regrecion lineal es:  {}".format(r2))
    
    def graficarRLineal(self):

        plt.plot(xlist, ylist, 'o', label='datos')
        plt.plot(xlist, m*x+b, label='ajuste')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("El coeficiente de regrecion lineal es: {}".format(r2))
        plt.grid()
        plt.legend()
        plt.show()

   



    def graficarIntegralDerv(self, fun):

        #primero calculamos la derivada
        X= sp.symbols('X')
        
        derivada =sp.diff(fun(X),X)

        integral = sp.integrate(fun(X),X)

        print(derivada)
        print(integral)


#metodo main para visualizar las graficas del punto 13
def main():

    X= sp.symbols('X')
    objclase = Database()

    a =lambda x: X**2 +3*X -4

    b = lambda x: sp.cos(x) - x**2

    c = lambda x: sp.sin(x)**2 - 2*sp.sin(x) + x


    while True:
        print("ESCOJA UNA FUNCION PARA GRAFICAR SU DERIVADA Y SU INTEGRAL".center(50,"*"))
 
        print("a. x^2 + 3*x -4 \n b. x^2 + 3*x -4 \n c. x^2 + 3*x -4")
        ans = input("Escoje una opcion: " )

        if (ans =="a"):

            objclase.graficarIntegralDerv(a)
            break
        elif (ans == 'b'):

            objclase.graficarIntegralDerv(b)
            break
        elif (ans == 'c'):

            objclase.graficarIntegralDerv(c)
            break
        else:
            print("OPCION ERRONEA, ESCOJA UNA OPCION CORRECTA EN MINUSCULAS")

main()