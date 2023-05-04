import os
import sqlite3

class Database:
    def __init__(self, *args):
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
        def __init__(self):
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
