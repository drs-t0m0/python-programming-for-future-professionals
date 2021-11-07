from fractions import Fraction

# 正の整数
print(10)

# 小数
print(1.5)

# 負の整数
print(-3)

# 負の小数
print(-4.75)

# 四則計算等
print(10 + 20)
print(100 - 25)
print(12 * 5)
print(20 // 5)
print(20 / 5)

print(17 / 3)
print(17 // 3)

# 割り算の余り
print(17 % 3)

# 商と剰余
print(divmod(17, 3))

# べき乗
print(2 ** 3)
print(pow(2, 3))

# 変数の手前に-を付けると、数値の正と負を反転
n = 1
print(-n)

# 演算子による値の比較
print(1 < 2)
print(1 <= 2)
print(1 == 1)
print(1 != 2)

# 演算子の優先順位
# 以下の計算は(2 * 3) + (4 * 5) - (6 / 2)と同じ
print(2 * 3 + 4 * 5 - 6 // 2)

# 優先順位を変更
print(2 * (3 + 4) * (5 - 6) // 2)

# 変数に格納された数値の増減
n += 1
print(n)

n -= 1
print(n)

m = 2
m *= 3
print(m)

m //= 2
print(m)

m **= 2
print(m)

# 数値と文字列の変換
print(1 + int("10"))
print(1 + float("10"))

num = 3
print("Number is " + str(3))
print(f"Number is {3}")

# 丸め誤差に注意
print(0.1 * 3.0)

# 10進数以外の整数リテラル

# 2進数
print(0b11111111)

# 8進数
print(0o377)

# 16進数
print(0xff)

# ビット演算

# ビット反転
print(0b1010)
print(~0b1010)

# ビット積
print(0b1010 & 0b1100)

# ビット和
print(0b1010 | 0b1100)

# 排他的論理和
print(0b1010 ^ 0b1100)

# ビットシフト
print(0b1010 >> 1)
print(0b1010 << 1)

# 指数表現
print(2e-3)

# 有理数
print(Fraction(2, 3))
print(Fraction("2/3"))

# 複素数
c = 0.3 - 0.5j
print(c)
print(complex(0.3, 0.5))
