# テスト自動化 まとめ

## テストコード

- pytestの基本
- FizzBuzzプログラムのテスト自動化

※Pythonの標準ライブラリにunittestがありますが、  
third partyライブラリのpytestの方が現場で利用されている認識です。  
より、pytestを用います。

* [test_code_3_1](./test_code_3_1.py)
* [test_fizz_buzz](./test_fizz_buzz.py)

## 参考

- https://docs.pytest.org/en/6.2.x/

## インストール例

```
$ pip install pytest
```

```
$ poetry add -D pytest
```

## 使い方

```
$ pytest test_code_3_1.py
$ pytest
$ pytest -v
```

