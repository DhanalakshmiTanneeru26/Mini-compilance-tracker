from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)

# ---------- DATABASE PATH ----------
DB_PATH = os.path.join(os.getcwd(), "database.db")


# ---------- DATABASE CONNECTION FUNCTION ----------
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ---------- INIT DATABASE SAFELY ----------
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        country TEXT,
        entity_type TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        title TEXT,
        category TEXT,
        due_date TEXT,
        status TEXT
    )
    """)

    # Insert sample clients only if empty
    cursor.execute("SELECT COUNT(*) FROM clients")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO clients (company_name, country, entity_type) VALUES ('GreenField Pvt Ltd', 'India', 'Private Limited')")
        cursor.execute("INSERT INTO clients (company_name, country, entity_type) VALUES ('Skyline Industries', 'USA', 'LLC')")
        cursor.execute("INSERT INTO clients (company_name, country, entity_type) VALUES ('BlueWave Solutions', 'UK', 'Corporation')")

    conn.commit()
    conn.close()


# ---------- CALL INIT ALWAYS ----------
init_db()

# ---------- ROUTES ----------

# ---------- HOME ----------
@app.route('/')
def index():
    conn = get_db()
    cursor = conn.cursor()
    
    search = request.args.get('search', '')
    sort = request.args.get('sort', 'asc')

    query = "SELECT * FROM clients WHERE company_name LIKE ?"
    params = [f"%{search}%"]

    if sort == "desc":
        query += " ORDER BY company_name DESC"
    else:
        query += " ORDER BY company_name ASC"

    clients = conn.execute(query, params).fetchall()
    conn.close()

    return render_template('index.html', clients=clients, search=search, sort=sort)


# ---------- VIEW TASKS ----------
@app.route('/client/<int:client_id>')
def view_tasks(client_id):
    conn = get_db()

    status = request.args.get('status')
    category = request.args.get('category')

    query = "SELECT * FROM tasks WHERE client_id=?"
    params = [client_id]

    if status:
        query += " AND status=?"
        params.append(status)

    if category:
        query += " AND category=?"
        params.append(category)

    tasks = conn.execute(query, tuple(params)).fetchall()
    conn.close()

    today = datetime.today().date()

    return render_template('tasks.html', tasks=tasks, today=today, client_id=client_id)


# ---------- ADD TASK ----------
@app.route('/add_task', methods=['POST'])
def add_task():
    client_id = request.form.get('client_id')
    title = request.form.get('title')
    category = request.form.get('category')
    due_date = request.form.get('due_date')

    if not title or not due_date:
        return "Title and Due Date are required!"

    conn = get_db()

    conn.execute("""
        INSERT INTO tasks (client_id, title, category, due_date, status)
        VALUES (?, ?, ?, ?, ?)
    """, (client_id, title, category, due_date, 'Pending'))

    conn.commit()
    conn.close()

    return redirect(f'/client/{client_id}')


# ---------- UPDATE STATUS ----------
@app.route('/update_status/<int:task_id>')
def update_status(task_id):
    conn = get_db()

    conn.execute("UPDATE tasks SET status='Completed' WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

    return redirect(request.referrer or '/')


# ---------- DELETE TASK ----------
@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    conn = get_db()

    conn.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()

    return redirect(request.referrer or '/')


# ---------- DASHBOARD ----------
@app.route('/dashboard')
def dashboard():
    conn = get_db()

    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    today = datetime.today().date()

    total = len(tasks)
    completed = len([t for t in tasks if t['status'] == 'Completed'])
    pending = len([t for t in tasks if t['status'] == 'Pending'])
    overdue = len([
        t for t in tasks
        if t['status'] == 'Pending' and t['due_date'] < str(today)
    ])

    return render_template(
        'dashboard.html',
        total=total,
        completed=completed,
        pending=pending,
        overdue=overdue
    )


# ---------- RUN ----------
if __name__ == '__main__':
    app.run()