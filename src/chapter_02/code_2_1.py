# 文字列
print("string")

# 数値
print(1)
print(3.14)

# None
print(None)

# 真偽値
print(True)
print(False)

# リスト(配列)
print([1, 2, 3])

# 辞書型(ディクショナリー)
print({"japan": "yen", "us": "dollar", "india": "rupee"})

# 集合型(セット)
print({"japan", "us", "india", "japan"})

# タプル
print(("japan", "us", "india"))

# 変数の宣言と代入
# 変数名は慣習として小文字のスネークケース
special_price = 200

# 2つの値を同時に代入
a, b = 1, 2,
print(a, b)

# タプルやリストも同時に代入
t = (100, 200, 300)
c, d, e = t
print(c, d, e)

l = [10, 20, 30]
f, g, h = l
print(f, g, h)

# 2つの変数に同じ値を代入
i = j = 5
print(i, j)

# 数値, 真偽値, None以外のオブジェクトに対してのメソッド呼び出し
l.append(40)
print(l)
