```python
# database.py

import sqlite3

class Database:
    def __init__(self, db_name='questify.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        # Create tables if they don't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT,
                email TEXT,
                location TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS quests (
                id INTEGER PRIMARY KEY,
                quest_data TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS rewards (
                id INTEGER PRIMARY KEY,
                reward_data TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                content TEXT
            )
        """)

    def save_user_data(self, user_data):
        self.cursor.execute("""
            INSERT INTO users (username, password, email, location) VALUES (?, ?, ?, ?)
        """, (user_data['username'], user_data['password'], user_data['email'], user_data.get('location')))

        self.conn.commit()

    def get_user_data(self, username):
        self.cursor.execute("""
            SELECT * FROM users WHERE username = ?
        """, (username,))

        return self.cursor.fetchone()

    def save_quest_data(self, quest_data):
        self.cursor.execute("""
            INSERT INTO quests (quest_data) VALUES (?)
        """, (quest_data,))

        self.conn.commit()

    def get_quest_data(self, quest_id):
        self.cursor.execute("""
            SELECT * FROM quests WHERE id = ?
        """, (quest_id,))

        return self.cursor.fetchone()

    def delete_quest_data(self, quest_id):
        self.cursor.execute("""
            DELETE FROM quests WHERE id = ?
        """, (quest_id,))

        self.conn.commit()

    def save_reward_data(self, reward_data):
        self.cursor.execute("""
            INSERT INTO rewards (reward_data) VALUES (?)
        """, (reward_data,))

        self.conn.commit()

    def get_reward_data(self, reward_id):
        self.cursor.execute("""
            SELECT * FROM rewards WHERE id = ?
        """, (reward_id,))

        return self.cursor.fetchone()

    def delete_reward_data(self, reward_id):
        self.cursor.execute("""
            DELETE FROM rewards WHERE id = ?
        """, (reward_id,))

        self.conn.commit()

    def save_post_data(self, post_data):
        self.cursor.execute("""
            INSERT INTO posts (user_id, content) VALUES (?, ?)
        """, (post_data['user_id'], post_data['content']))

        self.conn.commit()

    def get_post_data(self, post_id):
        self.cursor.execute("""
            SELECT * FROM posts WHERE id = ?
        """, (post_id,))

        return self.cursor.fetchone()
```
