# ガベージコレクション(GC)
# 使用されなくなったオブジェクトを回収し、自動的にメモリを解放
# 参考: https://docs.python.org/ja/3.9/library/gc.html

# import
# 標準ライブラリやpipでインストールしたThrid Partyなライブラリを読み込む
import datetime
from datetime import date

print(datetime.datetime.today())
print(date.today())

# 特殊な変数

# 現在のソースファイル名
print(__file__)

# 標準ライブラリ、pip(外部ライブラリ)
# 参考: https://docs.python.org/ja/3.9/library/index.html
