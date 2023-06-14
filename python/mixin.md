# mixin

## 簡介

多重繼承的能力，通常建議只用來實現 Mixin，也就是抽離可重用流程，必要時混入另一個類別。

Mixin 即 Mix-in，常被譯為“混入”，是一種程式設計模式，在 Python 等物件導向語言中，通常它是實現了某種功能單元的類，用於被其他子類繼承，將功能組合到子類中。

利用 Python 的多重繼承，子類可以繼承不同功能的 Mixin 類，按需動態組合使用。當多個類都實現了同一種功能時，這時應該考慮將該功能抽離成 Mixin 類。

Mixin 實質上是利用語言特性，可以把它看作一種特殊的多重繼承，所以它並不是 Python 獨享，只要支援多重繼承或者類似特性的都可以使用

為了程式碼的可讀性和可維護性，定義和使用 Mixin 類應該遵循幾個原則：

1. Mixin 實現的功能需要是通用的，並且是單一的，比如上例中兩個 Mixin 類都適用於大部分子類，每個 Mixin 只實現一種功能，可按需繼承。&#x20;
2. Mixin 只用於拓展子類的功能，不能影響子類的主要功能，子類也不能依賴 Mixin。。如果是依賴關係，則是真正的基類，不應該用 Mixin 命名。&#x20;
3. Mixin 類自身不能進行實例化，僅用於被子類繼承。

#### 範例

```python
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
# 我們可以通過呼叫實例屬性的方式來訪問
p = Person("小陳", "男", 18)
print(p.name)  # "小陳"
```

定義一個 Mixin 類：

```python
# 可以讓子類擁有像 dict 一樣呼叫屬性的功能
class MappingMixin:
    def __getitem__(self, key):
        return self.__dict__.get(key)

    def __setitem__(self, key, value):
        return self.__dict__.set(key, value)
        
# 將這個 Mixin 加入到 Person 類中
class Person(MappingMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        
# Person 擁有另一種呼叫屬性方式了
p = Person("小陳", "男", 18)
print(p['name'])  # "小陳"
print(p['age'])  # 18
```

再定義一個 Mixin 類，這個類實現了 **repr** 方法，能自動將屬性與值拼接成字：

```python
class ReprMixin:
    def __repr__(self):
        s = self.__class__.__name__ + '('
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                s += '{}={}, '.format(k, v)
        s = s.rstrip(', ') + ')'  # 將最後一個逗號和空格換成括號
        return s
        
# 多重繼承
class Person(MappingMixin, ReprMixin):
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

```
