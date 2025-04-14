from flask import Flask, render_template, request, redirect, session, url_for, g
import sqlite3

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Hacer que la cookie de sesión sea accesible desde JavaScript
app.config['SESSION_COOKIE_HTTPONLY'] = False

DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db:
        db.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
        db = get_db()
        db.execute('INSERT INTO messages (nombre, email, mensaje) VALUES (?, ?, ?)', (nombre, email, mensaje))
        db.commit()
        return render_template('index.html', enviado=True)

    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        if user:
            session['username'] = user['username']
            session['is_admin'] = bool(user['is_admin'])
            return redirect(url_for('admin_dashboard') if session['is_admin'] else url_for('index'))
        else:
            error = 'Usuario o contraseña incorrectos.'
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


@app.route('/admin')
def admin_dashboard():
    if not session.get('is_admin'):
        return 'Acceso no autorizado', 403
    return render_template('admin_dashboard.html')


@app.route('/admin/messages')
def admin_messages():
    if not session.get('is_admin'):
        return 'Acceso no autorizado', 403

    db = get_db()
    mensajes = db.execute('SELECT * FROM messages ORDER BY id DESC').fetchall()
    return render_template('admin_view.html', mensajes=mensajes)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
