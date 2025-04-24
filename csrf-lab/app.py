from flask import Flask, render_template, request, redirect, session, url_for, g, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'
DATABASE = 'database.db'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db:
        db.close()

@app.route('/')
def index():
    return redirect(url_for('dashboard')) if 'username' in session else redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    alert = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        puesto_id = request.form['puesto_id']

        if puesto_id == '4':
            alert = {'type': 'danger', 'message': 'No puedes registrar un usuario como Administrador.'}
            return render_template('register.html', alert=alert)

        db = get_db()
        try:
            db.execute('INSERT INTO users (username, password, puesto_id) VALUES (?, ?, ?)', 
                       (username, password, puesto_id))
            db.commit()
            alert = {'type': 'success', 'message': 'Usuario registrado exitosamente!'}
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            alert = {'type': 'danger', 'message': 'El usuario ya existe.'}
            return render_template('register.html', alert=alert)

    db = get_db()
    puestos = db.execute('SELECT * FROM puestos WHERE nombre != "Administrador"').fetchall()
    return render_template('register.html', puestos=puestos, alert=alert)



@app.route('/login', methods=['GET', 'POST'])
def login():
    alert = None

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password)).fetchone()
        if user:
            session['username'] = user['username']
            session['is_admin'] = bool(user['is_admin'])
            return redirect(url_for('dashboard'))
        else:
            alert = {'type': 'danger', 'message': 'Credenciales inválidas.'}
    return render_template('login.html', alert=alert)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    db = get_db()
    users = db.execute('''
        SELECT users.username, puestos.nombre AS puesto 
        FROM users
        JOIN puestos ON users.puesto_id = puestos.id
        ORDER BY users.id DESC
    ''').fetchall()

    is_admin = session.get('is_admin', False)
    
    return render_template('dashboard.html', users=users, is_admin=is_admin)


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if 'username' not in session:
        return redirect(url_for('login'))

    db = get_db()
    user = db.execute('SELECT id, puesto_id FROM users WHERE username = ?', (session['username'],)).fetchone()
    if not user:
        flash('Usuario no encontrado.', 'error')
        return redirect(url_for('logout'))

    # Obtener el puesto del usuario
    puesto = db.execute('SELECT nombre FROM puestos WHERE id = ?', (user['puesto_id'],)).fetchone()
    if puesto:
        user_role = puesto['nombre']

    if request.method == 'POST':
        mensaje = request.form['mensaje']
        fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db.execute('INSERT INTO chat (usuario_id, mensaje, fecha) VALUES (?, ?, ?)',
                   (user['id'], mensaje, fecha))
        db.commit()
        return redirect(url_for('chat'))

    mensajes = db.execute('''
        SELECT chat.mensaje, chat.fecha, users.username, puestos.nombre AS puesto
        FROM chat
        JOIN users ON chat.usuario_id = users.id
        JOIN puestos ON users.puesto_id = puestos.id
        ORDER BY chat.id ASC  -- ascendente
        LIMIT 20
    ''').fetchall()

    return render_template('chat.html', mensajes=mensajes, user_role=user_role)



@app.route('/settings')
def settings():
    if 'username' not in session:
        return redirect(url_for('login'))

    return render_template('settings.html')

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    if 'username' not in session:
        return 'No autenticado', 403
    new_password = request.form.get('new') if request.method == 'POST' else request.args.get('new')
    if not new_password:
        return 'Parámetro faltante', 400
    db = get_db()
    db.execute('UPDATE users SET password=? WHERE username=?', (new_password, session['username']))
    db.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
