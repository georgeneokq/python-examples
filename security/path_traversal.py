from flask import Flask, send_file, render_template_string, request
from os import path, listdir

app = Flask(__name__)

DOWNLOADS_PATH = '.'

@app.route('/')
def index():
  file = request.args.get('file')
  print(request.args)

  # ダウンロード可能のファイル一覧を取得
  filenames = filter(lambda filename: path.isfile(path.join(DOWNLOADS_PATH, filename)), listdir(DOWNLOADS_PATH))

  if file is None or file == '':
    html = """
    <html>
      <head>
      </head>
      <body>
        <table>
          <tbody>
            {% for filename in filenames %}
            <tr>
              <td>
                <a href="/?file={{filename}}">
                  {{ filename }}
                </a>
              </td> 
            </tr>
            {% endfor %}
          </body>
        </table>
      </body>
    </html>
    """
    return render_template_string(html, filenames=filenames)

  try:
    # パストラバーサル攻撃が可能
    return send_file(path.join(DOWNLOADS_PATH, file), as_attachment=True)
  except:
    return render_template_string(f'<p style="text-align:center;font-size:1.2rem;margin-top:15px;">{file}は存在しません。</p>')

if __name__ == '__main__':
  app.run('127.0.0.1', 5000)