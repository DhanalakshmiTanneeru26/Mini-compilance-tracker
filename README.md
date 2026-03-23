# 🚀 Mini Compliance Tracker

A simple full-stack web application to manage compliance tasks for multiple clients.  
Built using Flask and SQLite, this app helps track tasks, deadlines, and completion status efficiently.

---

## 📌 Project Overview

This project simulates a real-world compliance management system used by finance or consulting firms.  
Users can manage multiple clients and track their compliance-related tasks such as tax filings, audits, and legal submissions.

---

## 📊 Features

### 👥 Client Management
- View all clients
- Search clients 🔍
- Sort clients (A–Z / Z–A)
- Clean card-based UI with icons

### 📋 Task Management
- View tasks for each client
- Add new compliance tasks
- Update task status (Pending → Completed)
- Delete tasks

### 🔍 Filters
- Filter tasks by:
  - Status (Pending / Completed)
  - Category (Tax / Legal / Audit)

### ⏰ Overdue Tracking
- Automatically highlights overdue tasks in red
- Helps identify missed deadlines quickly

### 📊 Dashboard
- Total tasks
- Pending tasks
- Completed tasks
- Overdue tasks

---


## 🛠️ Technologies Used

- **Backend:** Flask (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap
- **Icons:** Bootstrap Icons
- **Deployment:** Render
- **Version Control:** Git & GitHub
```

```
## 📂 Project Structure

```
mini-compliance-tracker/
│
├── app.py
|
├── init_db.py
|
├── database.db
|
├── requirements.txt
|
├── Procfile
│
├── static/
│ └── styles.css
│
└── templates/
|
├── base.html
|
├── index.html
|
├── tasks.html
|
└── dashboard.html
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/mini-compliance-tracker.git
cd mini-compliance-tracker
```


### 2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Initialize the database

```bash
python init_db.py
```

4. Run the application

```bash
python app.py
```

5. Open in browser

```bash
http://127.0.0.1:5000
```
# Mini-compilance-tracker
