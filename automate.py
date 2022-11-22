"""
Chromeブラウザを自動化してWEBスクレイピングを行います。
本プログラムを実行する前にChromeをインストールしてください。
"""
from pathlib import Path
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

WEBSITE_URL = 'http://127.0.0.1:5000/diabetes'

test_diabetes_values_list = [
  [1, 90, 95, 15, 80, 33, 33],
  [2, 95, 87, 25, 76, 30, 30],
  [6, 69, 69, 18, 130, 36, 29],
  [8, 95, 120, 40, 97, 30.45, 40],
  [10, 74, 90, 22, 144, 32.2, 29],
]

test_diabetes_results = []

def main():
  # Tempディレクトリの存在を確認する
  Path('temp').mkdir(parents=True, exist_ok=True)

  # Seleniumでページを読み込む
  service = Service(executable_path=ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
  driver.maximize_window()

  # ページの読み込みが失敗した場合は終了する
  try:
    driver.get(WEBSITE_URL)
  except WebDriverException:
    print('The page could not be loaded.')
    return

  # ページ内の５つの入力欄を獲得する。
  input_elements = driver.find_elements(By.CSS_SELECTOR, 'input')

  # アサーションで入力欄の数を確認する
  assert len(input_elements) == 7

  # submitボタンを獲得する
  submit_button = driver.find_element(By.CSS_SELECTOR, 'button[type=submit]')

  # test_diabetes_values_listのデータを入力欄に打ち込む
  for diabetes_values in test_diabetes_values_list:
    for i, input_element in enumerate(input_elements):
      input_element.send_keys(str(diabetes_values[i]))
    submit_button.click()
    
    # ポップアップが表示するまで待つ。
    # ポップアップに表示されている糖尿病予測の確率を取得して、test_diabetes_results配列に入れる
    percentage_h2 = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.swal2-html-container > h2')))
    test_diabetes_results.append(percentage_h2.text)

    # ポップアップを閉じる
    popup_close_button = driver.find_element(By.CSS_SELECTOR, 'div.swal2-actions > button')
    popup_close_button.click()

    # 入力欄の値を削除する
    WebDriverWait(driver, 10).until_not(EC.staleness_of(input_elements[0]))
    for input_element in input_elements:
      input_element.clear()
    sleep(0.3)

  # 結果表示
  for i, result in enumerate(test_diabetes_results):
    print(f'{i + 1}人目: {result}')

if __name__ == '__main__':
  main()