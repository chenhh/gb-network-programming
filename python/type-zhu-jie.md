# type註解

## typing 模組&#x20;

[https://docs.python.org/zh-tw/3/library/typing.html](https://docs.python.org/zh-tw/3/library/typing.html)

Python 在 [PEP 484](https://peps.python.org/pep-0484/)中提出了 Type Hints（型別註解）。進一步強化了 Python 是一門強型別語言的特性，它在 Python3.5 中第一次被引入。使用 Type Hints 可以讓我們編寫出帶有型別的 Python 程式碼，看起來更加符合強型別語言風格。

該模組並非用來規定 Python 程式必須使用什麼型別，而是透過型別註釋(type annotations)讓開發者或協作者可以更加瞭解某個變數的型別，也讓第三方的工具能夠實作型別檢查器(type checker)。

## 基礎內建型別

<mark style="color:red;">Python 內建的型別（例如： int, float, dict, list, …）可以直接使用型別註釋，果是較複雜的資料型別就需要 typing 模組的輔助</mark>。

p.s. Python 本身並不會強迫函式或者變數必須使用規定型別的變數。

```python
# 傳入與傳出的type是str, 但沒有強制性
# 標註的語法和rust類似
def get_value(json: str = "my.json") -> str:
     x = parse(json)
     return x
```

### 自定義型別(class)

```python
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def student_to_string(s: Student) -> str:
    return f"student name: {s.name}, age: {s.age}."

student_to_string(Student("Tim", 18))
```

### 容器型別

當我們要給內建容器型別新增型別標注時，由於型別註解運算子 `[]` 在 Python 中代表切片操作，因此會引發語法錯誤。所以不能直接使用內建容器型別當作註解，需要從 typing 模組中匯入對應的容器型別註解（通常為內建型別的首字母大寫形式）。

```python
from typing import List, Tuple, Dict

l: List[int] = [1, 2, 3]

t: Tuple[str, ...] = ("a", "b")

d: Dict[str, int] = {
    "a": 1,
    "b": 2,
}
```

不過 [PEP 585](https://peps.python.org/pep-0585/)的出現解決了這個問題，我們可以直接使用 Python 的內建型別，而不會出現語法錯誤。

```python
l: list[int] = [1, 2, 3]

t: tuple[str, ...] = ("a", "b")

d: dict[str, int] = {
    "a": 1,
    "b": 2,
}
```

### 型別別名(type alias)

有些復雜的巢狀型別寫起來很長，如果出現重復，就會很痛苦，程式碼也會不夠整潔。此時可以通過給型別起別名的方式來解決，類似變數命名。

```python
Config = list[tuple[str, int], dict[str, str]]

config: Config = [
    ("127.0.0.1", 8080),
    {
        "MYSQL_DB": "db",
        "MYSQL_USER": "user",
        "MYSQL_PASS": "pass",
        "MYSQL_HOST": "127.0.0.1",
        "MYSQL_PORT": "3306",
    },
]

def start_server(config: Config) -> None:
    pass
```

### 可變引數

```python
def foo(*args: str, **kwargs: int) -> None:
    passpyth

foo("a", "b", 1, x=2, y="c")
```

## typing.Optional

Optional\[X] 等價於 X | None （或 Union\[X, None] ） 。

注意，可選類型與含預設值的可選參數不同。含預設值的可選參數不需要在類型註解上新增 Optional 限定符，因為它僅是可選的。

```python
def foo(arg: int = 0) -> None:
```

顯式應用 None 值時，不管該參數是否可選， Optional 都適用。

```python
def foo(arg: Optional[int] = None) -> None:
```

## typing.Union

一個函式或方法能夠接受多種型別時，可以利用 `typing.Union`。

```python
from typing import Union

# 輸入的型別可為int或str
def print_something(x: Union[int, str]):
    if isinstance(x, (int, str, )):
        print(f'Got {x}')
    else:
        raise TypeError('Only int & str are accepted')
```

## typing.Dict

可用 `typing.Dict` 為 key 與 value 標上型別，例如 Dict\[str, int] 代表一個字典的 key 是字串， value 則是整數。

```python
word_count_mapping: Dict[str, int] = {
    'zoo': 1,
    'zip': 2,
    'google': 10,
    'python': 12,
}
​
def update_count(mapping: Dict[str, int], key: str, count: int):
    mapping[key] = count
```

## typing.TypedDict

實務上也經常會為字典型的變數規定格式，例如以下的字典，該字典必須有 username 與 password 2 個 key 存在才行。

```python
from typing import TypedDict

class LoginDict(TypedDict):
    username: str
    password: str

login_dict: LoginDict = {
    'username': 'abc',
    'password': 'pass123456',
}

def valid_username_password(login_dict: LoginDict):
    passt
```

## typing.Iterable

Python 中所謂的 Iterable 指的是有實作 **iter**() 與 **next**() 的物件(object)，例如 str, dict, list, tuple 都是 Iterable ，所以都能夠透過 for 走訪，因此如果是可以接受 Iterable 的函式或方法，可以使用 typing.Iterable 進行標示。

```python
from typing import Iterable

def print_iterable(x: Iterable):
    for i in x:
        print(i)
```

## typing.Any

如果是不限定型別的情況下，可以使用 typing.Any ，譬如 print 其實就很適合可以使用 typing.Any。也可以用 object 代替 typing.Any ，因為在 Python 中所有的物件都繼承自 object。

```python
from typing import Any

def print_anything(*args: Any):
    print(*args)
    
def print_anything2(*args: object):
    print(*args)
```

## 型別檢查器(type checker)

型別註釋能夠提供團隊成員對於變數型別的瞭解，不過仍不能真正解決型別誤用的情況，畢竟 Python 的型別註釋也只是註釋，並無法偵測誤用/錯用型別的情況。

更積極的做法是透過型別檢查器(type checker)幫助我們偵測誤用/錯用型別的情況，例如 mypy 。

## 標註numpy類型

```python
import numpy as np
Float64Array = np.ndarray[Any, np.dtype[np.float64]]
Int64Array = np.ndarray[Any, np.dtype[np.int64]]
Int32Array = np.ndarray[Any, np.dtype[np.int32]]
IntArray = np.ndarray[Any, np.dtype[np.int_]]
BoolArray = np.ndarray[Any, np.dtype[np.bool_]]
AnyArray = np.ndarray[Any, Any]
Uint32Array = np.ndarray[Any, np.dtype[np.uint32]]

RNGType = Callable[[Union[int, Tuple[int, ...]]], Float64Array]
ArrayLike1D = Union[NDArray, Series]
ArrayLike2D = Union[NDArray, DataFrame]
ArrayLike = Union[NDArray, DataFrame, Series]
NDArrayOrFrame = TypeVar("NDArrayOrFrame", Float64Array, DataFrame)
AnyPandas = Union[Series, DataFrame]
DateLike = Union[str, dt.datetime, np.datetime64, Timestamp]
Label = Optional[Hashable]
FloatOrArray = TypeVar("FloatOrArray", float, np.ndarray)
UnitRootTrend = Literal["n", "c", "ct", "ctt"]
```

## 參考資料

* [module typing](https://docs.python.org/zh-tw/3/library/typing.html#module-typing)
* [\[林信良\] 思考Python的型態提示](https://www.ithome.com.tw/voice/104417), [Type Hints的野心](https://www.ithome.com.tw/voice/116983)
* [\[知乎\] Python Type Hints 從入門到實踐](https://zhuanlan.zhihu.com/p/424042902)
* [Type Hints 入門教程，讓程式碼更加規范整潔](https://zhuanlan.zhihu.com/p/519335398)

### 型別檢查器

* [mypy](https://mypy.readthedocs.io/en/stable/index.html)
* [\[google\] pytype](https://google.github.io/pytype/)
* [\[facebook\] pyre-check](https://github.com/facebook/pyre-check)
* [\[microsoft\] pyright](https://github.com/microsoft/pyright)
