import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Habilitar claves foráneas
    c.execute('PRAGMA foreign_keys = ON')

    # Crear tabla de puestos
    c.execute('''
        CREATE TABLE IF NOT EXISTS puestos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    ''')

    # Crear tabla de usuarios
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            puesto_id INTEGER,
            is_admin INTEGER DEFAULT 0,
            FOREIGN KEY(puesto_id) REFERENCES puestos(id)
        )
    ''')

    # Crear tabla de chat con clave foránea al id del usuario
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario_id INTEGER NOT NULL,
            mensaje TEXT NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES users(id)
        )
    ''')

    # Insertar puestos por defecto si no existen
    c.execute('SELECT COUNT(*) FROM puestos')
    if c.fetchone()[0] == 0:
        puestos_default = ['Desarrollador', 'Gerente', 'Diseñador', 'Administrador']
        for puesto in puestos_default:
            c.execute('INSERT INTO puestos (nombre) VALUES (?)', (puesto,))

    # Insertar usuarios por defecto si no existen
    c.execute('SELECT * FROM users WHERE username = ?', ('admin',))
    if not c.fetchone():
        c.execute('INSERT INTO users (username, password, puesto_id, is_admin) VALUES (?, ?, ?, ?)',
                  ('admin', 'admin123', 4, 1))

    users_default = [
        ('juan', 'juan_sjdnsdn', 1, 0),
        ('maria', 'maaariaaa!$', 2, 0),
        ('ana', 'anita62&/', 3, 0),
    ]

    for username, password, puesto_id, is_admin in users_default:
        c.execute('SELECT * FROM users WHERE username = ?', (username,))
        if not c.fetchone():
            c.execute('INSERT INTO users (username, password, puesto_id, is_admin) VALUES (?, ?, ?, ?)',
                      (username, password, puesto_id, is_admin))

    conn.commit()
    conn.close()
    print("[DB] Base de datos inicializada correctamente.")

if __name__ == '__main__':
    init_db()
