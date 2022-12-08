"""
例: ' UNION SELECT username, password FROM users LIMIT 1 OFFSET 1 --
"""
from tkinter import Tk, ttk
from pathlib import Path
import sqlite3
import hashlib
from db.db_setup import database_setup

def main():
  connection = sqlite3.connect('db/application.db')

  database_setup(connection, reset=False)

  username, password = get_credentials()
  password = hashlib.md5(password.encode()).hexdigest()

  # 安全なやり方
  sql_statement_secure = "SELECT username, phone_number FROM users WHERE username=? AND password=?"
  cursor = connection.execute(sql_statement_secure, [username, password])

  # SQLインジェクションは可能
  sql_statement_vulnerable = f"SELECT username, phone_number FROM users WHERE username='{username}' AND password='{password}'"
  print(sql_statement_vulnerable)
  cursor = connection.execute(sql_statement_vulnerable)

  user = cursor.fetchone()

  cursor.close()
  connection.close()

  print(user)

# tkinterライブラリでフォームを作る
def get_credentials():
  FONT_SIZE=18
  SAVED_INPUTS_PATH = 'db/sql_injection_inputs.txt'

  credentials = {
    'username': '',
    'password': ''
  }
  
  Path(SAVED_INPUTS_PATH).touch(exist_ok=True)
  with open(SAVED_INPUTS_PATH, 'r') as f:
    for line in f.read().splitlines():
      key, value = line.split('=')
      credentials[key] = value

  def get_inputs():
    credentials['username'] = username_input.get()
    credentials['password'] = password_input.get()
    root.destroy()

  root = Tk()
  frame = ttk.Frame(root, padding=10)
  frame.grid()

  ttk.Label(frame, justify='left', text="Username", font=FONT_SIZE).grid(column=0, row=0)

  username_input = ttk.Entry(frame, width=75, font=FONT_SIZE)
  username_input.insert(0, credentials['username'])
  username_input.grid(column=0, row=1)

  ttk.Label(frame, text="Password", font=FONT_SIZE).grid(column=0, row=2)

  password_input = ttk.Entry(frame, width=75, font=FONT_SIZE)
  password_input.insert(0, credentials['password'])
  password_input.grid(column=0, row=3)

  button = ttk.Button(frame, text="Login", style="app.TButton", command=get_inputs)
  button.grid(column=0, row=4, pady=10)

  style = ttk.Style()
  style.configure('app.TButton', font=(None, FONT_SIZE))

  username_input.bind('<Return>', lambda _: button.invoke())
  password_input.bind('<Return>', lambda _: button.invoke())
  button.bind('<Return>', lambda _: button.invoke())
  
  username_input.focus()

  root.mainloop()

  # Save username and password into a file to remember user input
  with open(SAVED_INPUTS_PATH, 'w') as f:
    config = f"username={credentials['username']}\npassword={credentials['password']}"
    f.write(config)

  return credentials['username'], credentials['password']

if __name__ == '__main__':
  main()