from flask import Flask, send_file, render_template_string, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  file = request.args.get('file')
  print(request.args)

  if file is None:
    return redirect('/?file=')

  if file == '':
    return render_template_string('<b style="text-align:center">http://localhost:5000/?file=<ファイル名></b>')

  try:
    # パストラバーサル攻撃が可能
    return send_file(file, as_attachment=True)
  except:
    return render_template_string(f'<p style="text-align:center;font-size:1.2rem;margin-top:15px;">{file}は存在しません。</p>')

if __name__ == '__main__':
  app.run('127.0.0.1', 5000)