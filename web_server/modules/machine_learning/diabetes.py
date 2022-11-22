from joblib import load
from os import path

def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age):
  # モデルを読み込む
  current_dir = path.realpath(path.dirname(__file__))
  model_path = path.join(current_dir, 'models/random_forest_model.joblib')
  model = load(model_path)

  # モデルに入力データを評価させて、出力値を取得する
  values = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age]
  values = [float(value) for value in values]
  probability = model.predict_proba([values])[0, 1]  # 例: [80.1, 19.9]  <- 19.9を抽出

  return probability

def test():
  print(predict_diabetes(3, 120, 74, 30, 100, 32, 40))

if __name__ == '__main__':
  test()