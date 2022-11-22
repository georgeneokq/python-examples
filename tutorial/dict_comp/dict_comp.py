data = [
  'A: 10',
  'B: 22',
  'C: 6',
  'D: 39',
  'E: 8',
  'F: 11',
]

# 辞書型に変える
data = {value[0]:value[1] for value in [string.split(': ') for string in data]}
print(data)
