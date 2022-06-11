# type註解

## typing 模組&#x20;

typing 是 Python 3.5 以上內建的模組。

該模組並非用來規定 Python 程式必須使用什麼型別，而是透過型別註釋(type annotations)讓開發者或協作者可以更加瞭解某個變數的型別，也讓第三方的工具能夠實作型別檢查器(type checker)。

p.s. Python 本身並不會強迫函式或者變數必須使用規定型別的變數。

```python
# 傳入與傳出的type是str, 但沒有強制性
# 標註的語法和rust類似
def get_value(json: str) -> str:
     x = parse(json)
     return x
```

## 參考資料

* [module typing](https://docs.python.org/zh-tw/3/library/typing.html#module-typing)
