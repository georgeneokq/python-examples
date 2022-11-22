"""
numpyライブラリのndarrayとは、N-Dimension Arrayの略です。
1D,2D,3D配列を作って、容易く操作することができます。
普通のリストは、角カッコの中に数字を一つしか入れませんが、ndarrayの場合はコンマで軸ごとに要素を取れます。
例：
data = [[0, 1], [2, 3]]

上の2D配列から２の数字を取り出したい。普通のリストだったらこう：data[1][0]
numpyのndarrayの場合はこう：data[1, 0]
"""
import numpy as np

data = np.array([[0, 1], [2, 3]])

print(data[1][0])  # 普通のリストの場合
print(data[1,0])  # ndarrayの場合
print('')


"""
二次元配列の操作を試しましょう。
"""
ndarray = np.array([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15]
])


"""
1, 2, 3, 4, 5
"""
print(ndarray[0])
print('')


"""
1, 2, 3, 4, 5
6, 7, 8, 9, 10
"""
print(ndarray[:2])
print('')


"""
1 2 3 4
6 7 8 9
"""
print(ndarray[:2,:4])
print('')


"""
1
6
11
"""
print(ndarray[:,:1])
print('')
