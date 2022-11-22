"""
if __name__ == '__main__'

__name__とは、pythonファイルの実行方法による変わる変数です。
シェルからpython program.pyで実行してした場合は、__name__の値は "__main__" となります。
ほかのファイルからロードされた場合(importで)は、__name__の値は本ファイル名となります。
"""

def func():
  pass

print(__name__)

if __name__ == '__main__':
  print(__name__)
