import requests
import sqlite3

conn = sqlite3.connect("user_preferences.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS preferences (
        user_id INTEGER,
        category TEXT,
        PRIMARY KEY (user_id, category),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
''')

conn.commit()

def register_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

def login_user(username, password):
    cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
    user_id = cursor.fetchone()
    return user_id[0] if user_id else None

def save_preference(user_id, category):
    cursor.execute("INSERT INTO preferences (user_id, category) VALUES (?, ?)", (user_id, category))
    conn.commit()

def get_user_preferences(user_id):
    cursor.execute("SELECT category FROM preferences WHERE user_id = ?", (user_id,))
    return cursor.fetchall()

def get_news_aggregator(category):
    api_key = "4da3790013d1488aa293dab74429ea81"
    endpoint = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={api_key}"
    response = requests.get(endpoint)
    data = response.json()
    return data

def display_news_aggregator(user_id):
    preferences = get_user_preferences(user_id)
    
    for category in preferences:
        print(f"Category: {category[0]}")
        news_data = get_news_aggregator(category[0])
        
        for article in news_data['articles']:
            title = article['title']
            description = article['description']
            print(f"Title: {title}\nDescription: {description}\n")

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

user_id = login_user(username_input, password_input)
if not user_id:
    register_user(username_input, password_input)
    user_id = login_user(username_input, password_input)

category_input = input("Enter your preferred news category: ")
save_preference(user_id, category_input)

display_news_aggregator(user_id)
conn.close()
