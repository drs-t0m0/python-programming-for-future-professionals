# 真偽値

# False, None, ""(空白), 0であれば偽
# それ以外はすべて真

print(False)
print(bool(None))
print(bool(""))
print(bool(0))

data = False
if data:
    print("True")
else:
    print("False")

# 論理演算子
t1 = True
t2 = True
f1 = False
f2 = False

print(t1 and t2)
print(t1 and f1)
print(t1 or f1)
print(f1 or f2)

# 下の式は同じ意味
print(t1 and t2 or f1 and f2)
print((t1 and t2) or (f1 and f2))
print(t1 and (t2 or f1) and f2)

# 反転
print(not t1)
print(not f1)
print(t1 and f1)
print(not (t1 and f1))

# if文
n = 11
if n > 10:
    print("10より大きい")
else:
    print("10以下")

country = "japan"

if country == "japan":
    print("こんにちは")
elif country == "us":
    print("Hello")
elif country == "italy":
    print("ciao")
else:
    print("???")

# 三項演算子
x = 101
message = "10より大きい" if n > 10 else "10以下"
print(message)
