"""
https://docs.python.org/ja/3.9/glossary.html より

(スライス) 一般に シーケンス の一部を含むオブジェクト。
スライスは、添字表記 [] で与えられた複数の数の間にコロンを書くことで作られます。
例えば、 variable_name[1:3:5] です。
角括弧 (添字) 記号は slice オブジェクトを内部で利用しています。
"""

# １から２０を含めたリストを作成する
data = [num for num in range(1, 21)]
print(data)

# start:end:step
# リストの最初の要素から取りたい場合は、0を省けても結構。
print(data[:10])

# endはネガティブだった場合は、最後の要素から参照する。
print(data[0:-1])

# step - ループする度に要素を何個ずつ飛ぶかを指定する
print(data[::2])
print(data[1::2])

# stepで文字列を逆にすることもできます。
string = 'ramen'
print(string[::-1])
