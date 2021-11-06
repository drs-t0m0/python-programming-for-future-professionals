# Python 3.6から型ヒントが導入された。
# 方針としては型推論ベースで型を設定するような型ヒントが良いと考えています。


# メソッドの定義
# 戻り値
def add(a: int, b: int) -> int:
    return a + b


print(add(1, 2))


# メソッド名も変数名と同じ慣習として小文字のスネークケース
# 返り値を持たない
def say_hello() -> None:
    print("Hello World")


say_hello()


# デフォルト値付きの引数, キーワード引数
def greeting(country="japan") -> None:
    if country == "japan":
        print("こんにちは")
    elif country == "us":
        print("Hello")
    elif country == "italy":
        print("ciao")
    else:
        print("???")


greeting()
greeting("us")
greeting(country="italy")


# 可変長引数
def my_sum(*args):
    return sum(args)


print(my_sum(1, 2, 3, 4))
print(my_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# 複数のキーワード引数を辞書として受け取る
def func_kwargs(**kwargs):
    print(f"kwargs: {kwargs}")


func_kwargs(key1=1, key2=2, key3=3)
