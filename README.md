# Python Examples

You are currently reading the Japanese documentation.

For English-speaking developers, [view the English documentation](docs/README-en.md).

## 概要

別々の目的で作られたライブラリたちを合わせることですごいことができるっていう点を示すために、様々なライブラリを使ってPythonで面白いことを色々やって行きます。

- openpyxlライブラリでExcelファイルを操作する
- Flaskで簡易Webサーバーを立ち上げる
- SeleniumとBeautiful SoupでWebスクレイピングを行う
- numpy, pandas, sklearn, seaborn, matplotlibで機械学習を行って、機械学習モデルを作成する
- Seleniumでブラウザ操作の自動化

## インストレーション(Windows)

まずはPython3.9以降のバージョンをインストールしてください。

```
powershell
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

## チュートリアル

デモンストレーションに入る前に、`tutorial`ディレクトリの入ってあるいくつかのpythonの機能の紹介を見ることをおすすめします。

list_comp -> dict_comp -> slicing -> name の順で見てください。

## デモンストレーション

以下の指示はシェルのカレントディレクトリはプロジェクトルートだということを前提とする。

### Excelファイルを読み込む

```powershell
cd web_server/modules
python excel.py
```

### Webサーバーを立ち上げる

```powershell
cd web_server
python -m flask --debug run
```

### 静的サイトのWebスクレイピングを行う

以下のコマンドを実行する前にWebサーバーを起動してください。[Webサーバーを立ち上げる](#webサーバーを立ち上げる)を閲覧

```powershell
python scrape_static.py
```

### 動的サイトのWebスクレイピングを行う

以下のコマンドを実行する前にWebサーバーを起動してください。[Webサーバーを立ち上げる](#webサーバーを立ち上げる)を閲覧

```powershell
python scrape_dynamic.py
```

### 機械学習モデルを作成する

`machine_learning/train_diabetes.ipynb`を開く。ブラウザのJupyter Notebookではコード補完がないため、Visual Studio Codeで開くことを強くおすすめします。

ブラウザのJupyter Notebookで開きたい場合は以下のコマンドを実行してください。
```powershell
python -m notebook machine_learning/train_diabetes.ipynb
```

トレーニングデータセット`diabetes.csv`は`machine_learning/datasets`にあります。データセットの詳細は[ここから読めます](https://www.kaggle.com/datasets/mathchi/diabetes-data-set)。

### ブラウザの自動化

以下のコマンドを実行する前にWebサーバーを起動してください。[Webサーバーを立ち上げる](#webサーバーを立ち上げる)を閲覧

```powershell
python automate.py
```

### セキュリティ上問題

`security`ディレクトリには脆弱性が入ってるアプリケーションがいくつか入ってあります。

[sql_injection.py](security/sql_injection.py): SQLインジェクション攻撃

[path_traversal.py](security/path_traversal.py): パストラバーサル攻撃

[ssti.py](security/ssti.py): サーバーサイドテンプレートインジェクション攻撃