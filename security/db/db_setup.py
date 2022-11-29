import sqlite3
import hashlib

def database_setup(connection: sqlite3.Connection, *, reset=False):
  # ユーザー名、パスワード、電話番号
  default_users: tuple[str,str,str] = [
    ('user1', 'BubblETea', '080135949320'),
    ('user2', 'abcdefg', '080135942015'),
    ('user3', '1234567811', '080444441786'),
  ]

  default_users = [(username, hashlib.md5(password.encode()).hexdigest(), phone_number) for (username, password, phone_number) in default_users]

  if reset:
    connection.execute('DROP TABLE IF EXISTS users')
    connection.execute('CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, phone_number TEXT)')
  else:
    connection.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, phone_number TEXT)')

  cursor = connection.execute('SELECT count(*) FROM users')
  num_records, = cursor.fetchone()

  if num_records == 0:
    for (username, password, phone_number) in default_users:
      connection.execute(f"INSERT INTO users(username, password, phone_number) VALUES (?, ?, ?)", [username, password, phone_number])
      print(f'Inserted: {username}')

  connection.commit()
