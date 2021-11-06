# Pythonはシングルクォートとダブルクォートの違いは基本的にない(はず)です

# 改行文字
print("こんにちは\nさようなら")
print("こんにちは", "さようなら", sep="\n")

# sepはデフォルト空白
print("こんにちは", "さようなら")

# 改行文字の機能を打ち消したい場合
print("こんにちは\\nさようなら")

# 式展開(テンプレート文字列), フォーマット
name = "Alice"
age = 20
print(f"name: {name}, age: {age}")
print("name: {}, age: {}".format(name, age))
print("name: {0}, age: {1}".format(name, age))
print("name: {a}, age: {b}".format(a=name, b=age))

# 文字列の比較
print("python" == "python")
print("python" == "Python")
print("python" != "python")
print("python" != "Python")

# 文字列に対する辞書的な順序比較(ASCII)
print("a" < "b")
print("a" > "A")
print("abc" < "def")
print("abc" > "ab")
print("abc" < "abcd")
print("あいうえお" < "かきくけこ")

# ヒアドキュメント風 複数行にまたがって記述
print("""Line 1
Line 2""")

# フォーマットを指定して文字列を作成
print(f"{1.2:.3f}")

# その他、文字列作成のいろいろ

# 数値を文字列に変換
print(str(123))

# 配列を連結して1つの文字列
print("".join(["10", "20", "30"]))

# *演算子を使って文字列を繰り返す
print("Hi" * 10)

# Unicodeエスケープされた文字列・バイト列を変換
s = "あいう"
u = s.encode("unicode-escape")
print(u)

s_from_u = u.decode("unicode-escape")
print(s_from_u)
