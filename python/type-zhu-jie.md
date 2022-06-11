# type註解

## typing 模組&#x20;

typing 是 Python 3.5 以上內建的模組。

該模組並非用來規定 Python 程式必須使用什麼型別，而是透過型別註釋(type annotations)讓開發者或協作者可以更加瞭解某個變數的型別，也讓第三方的工具能夠實作型別檢查器(type checker)。

<mark style="color:red;">Python 內建的型別（例如： int, float, dict, list, …）可以直接使用型別註釋，但如果是較複雜的資料型別就需要 typing 模組的輔助</mark>。

p.s. Python 本身並不會強迫函式或者變數必須使用規定型別的變數。

```python
# 傳入與傳出的type是str, 但沒有強制性
# 標註的語法和rust類似
def get_value(json: str) -> str:
     x = parse(json)
     return x
```

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
