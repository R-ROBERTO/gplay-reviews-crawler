import sqlite3
from datetime import datetime

# Global connection and cursor
conn = None
cursor = None

def connect_db(db_path='reviews.db'):
    global conn, cursor
    if conn is None:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                reviewId TEXT PRIMARY KEY,
                userName TEXT,
                userImage TEXT,
                content TEXT,
                score INTEGER,
                thumbsUpCount INTEGER,
                reviewCreatedVersion TEXT,
                at TEXT,
                replyContent TEXT,
                repliedAt TEXT,
                appVersion TEXT
            )
        ''')
        conn.commit()

def insert_review(review):
    if conn is None or cursor is None:
        raise Exception("Database not connected. Call connect_db() first.")
    cursor.execute('''
        INSERT OR IGNORE INTO reviews VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        review['reviewId'],
        review['userName'],
        review['userImage'],
        review['content'],
        review['score'],
        review['thumbsUpCount'],
        review.get('reviewCreatedVersion'),
        review['at'].isoformat() if isinstance(review['at'], datetime) else review['at'],
        review['replyContent'],
        review['repliedAt'].isoformat() if isinstance(review['repliedAt'], datetime) else review['repliedAt'],
        review.get('appVersion')
    ))
    conn.commit()

def close_connection():
    global conn, cursor
    if conn:
        conn.close()
        conn = None
        cursor = None
