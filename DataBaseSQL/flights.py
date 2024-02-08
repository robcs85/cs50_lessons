import sqlite3
# criando conexao com banco
con = sqlite3.connect('voos.db')
# se não existe, crie banco
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS flights
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                origem TEXT NOT NULL,
                destino TEXT NOT NULL,
                tempo INTEGER NOT NULL)''')