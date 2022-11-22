"""
List comprehensionを使った処理
"""
data = ['0', '512', '23', '1000', '100.5', '1']
print(data)

# 各要素を２倍にする
result = [str(float(string) * 2) for string in data]
print(result)
