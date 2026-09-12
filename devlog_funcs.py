import dis
import sqlite3 
from datetime import datetime
import os

def clear_screen():
    if os.name == 'nt': 
        os.system('cls')
    else: 
        os.system('clear')

def initialize_database():
    conn = sqlite3.connect('devlog.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (title TEXT, content TEXT, timestamp DATETIME)''')
    conn.commit()
    conn.close()

def add_entry(title, content):
    now = datetime.now().strftime("%m/%d/%Y")
    conn = sqlite3.connect('devlog.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO entries (title, content, timestamp) VALUES (?, ?, ?)', (title, content, now))
    conn.commit()
    conn.close()

def list_entries():
    conn = sqlite3.connect('devlog.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM entries')
    entries = cursor.fetchall()
    for entry in entries:
        print(f'{entry[2]}: {entry[0]} - {entry[1]}')
        print()
    conn.close()

def remove_entry(title):
    conn = sqlite3.connect('devlog.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM entries WHERE title=?', (title,))
    conn.commit()
    conn.close()

