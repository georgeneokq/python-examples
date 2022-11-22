"""
本プログラムを実行する前に、WEBサーバーを起動してください。 (cd web_server; python -m flask --debug run)
本プログラムは、WEBスクレイピングを行ってExcelファイルに保存する

References:
Scraping from dynamic websites using selenium:
https://www.geeksforgeeks.org/scrape-content-from-dynamic-websites/

Set up selenium driver:
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#2-driver-management-software
"""
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from openpyxl.styles import Alignment
from time import time
from pathlib import Path

WEBSITE_URL = 'http://127.0.0.1:5000/static-page'

def main():
  # Tempディレクトリの存在を確認する
  Path('temp').mkdir(parents=True, exist_ok=True)

  # Excelファイルに入れたいデータをWEBスクレイピングで獲得する
  data = scrape(use_selenium=False)
  headers = list(data[0].keys())
  values_list = [list(item.values()) for item in data]

  # Excelシートを作成する
  wb = Workbook()

  # デフォルトのシートを取得する
  sheet = wb.active

  # シートの名前を変更する
  sheet.title = '食事データ'

  # データを入れる
  sheet.append(headers)
  for values in values_list:
    sheet.append(values)

  # 折り返し改行を設定する
  for row in sheet.iter_rows():
    for cell in row:
      cell.alignment = Alignment(wrap_text=True)

  # Excelファイルを保存する
  wb.save(f'temp/shokuji_scrape_{time()}.xlsx')

def scrape(use_selenium=True) -> list[dict]:
  """
  WEBスクレイピングを行ってデータを獲得する

  Args:
    use_selenium  WEBページのデータが動的で読み込まれる場合は、この引数をTrueに設定必要があります。
  """
  html_content = ''

  if use_selenium:
    # Seleniumでページ実際に読み込んでからHTMLを読み込む
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(WEBSITE_URL)
    html_content = driver.page_source
  else:
    # そのままのHTMLを読み込む
    html_content = requests.get(WEBSITE_URL).text
  
  # 手に入れたサイトのHTMLを解析して情報を抽出する
  soup = BeautifulSoup(html_content, features='html.parser')
  headers = [th.string for th in soup.find_all('th')]
  data = [td.string for td in soup.find_all('td')]

  # データを辞書型として返す
  items = []
  for data_index in range(0, len(data), len(headers)):
      item = { headers[header_index]: data[data_index + header_index] for header_index in range(len(headers))}
      items.append(item)

  return items

if __name__ == '__main__':
  main()
