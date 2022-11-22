"""
Flaskでウェブサーバーを建てましょう！
"""
from flask import Flask, send_file, render_template, request
from modules.excel import get_food_info
from modules.machine_learning.diabetes import predict_diabetes

app = Flask(__name__, static_url_path='/')

""" Web """

@app.route('/')
def index():
  """ Display the overview page which shows links to the other pages """
  return render_template('index.html')

@app.route('/dynamic-page')
def index_page():
  return send_file('pages/dynamic.html')

@app.route('/static-page')
def render_page():
  food_info = get_food_info()
  return render_template('static.html', title='メニュー', shokuji=food_info)

@app.route('/diabetes')
def diabetes_page():
  return render_template('diabetes_predictor.html')

""" API """

@app.route('/api/shokuji')
def shokuji_api():
  food_info = get_food_info()
  print(food_info)
  title = 'メニュー'
  return {
    'title': title,
    'data': food_info
  }

@app.route('/api/diabetes', methods=['POST'])
def diabetes_api():
  pregnancies = request.form.get('pregnancies')
  glucose = request.form.get('glucose')
  blood_pressure = request.form.get('blood_pressure')
  skin_thickness = request.form.get('skin_thickness')
  insulin = request.form.get('insulin')
  bmi = request.form.get('bmi')
  age = request.form.get('age')
  probability = predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age)

  return {
    'probability': probability
  }

if __name__ == '__main__':
  app.run()