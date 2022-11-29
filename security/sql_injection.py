"""
例: ' UNION SELECT username, password FROM users LIMIT 1 OFFSET 1 --
"""
import sqlite3
import hashlib
from db.db_setup import database_setup

def main():
  connection = sqlite3.connect('db/users.db')
  database_setup(connection, reset=False)

  username = input('ユーザー名：')
  password = input('パスワード：')
  password = hashlib.md5(password.encode()).hexdigest()

  # 安全なやり方
  sql_statement_secure = "SELECT username, phone_number FROM users WHERE username=? AND password=?"
  cursor = connection.execute(sql_statement_secure, [username, password])

  # SQLインジェクションは可能
  sql_statement_vulnerable = f"SELECT username, phone_number FROM users WHERE username='{username}' AND password='{password}'"
  print(sql_statement_vulnerable)
  cursor = connection.execute(sql_statement_vulnerable)

  user = cursor.fetchone()

  print(user)

if __name__ == '__main__':
  main()