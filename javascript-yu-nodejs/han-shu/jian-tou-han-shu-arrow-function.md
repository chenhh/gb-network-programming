# 箭頭函數(arrow function)

## 簡介

箭頭函式運算式（arrow function expression）擁有比函數運算式還簡短的語法。它沒有自己的 this、arguments、super、new.target 等語法。

## 基本語法

```javascript
(參數1, 參數2, …, 參數N) => { 陳述式; }

(參數1, 參數2, …, 參數N) => 表示式;
// 等相同(參數1, 參數2, …, 參數N) => { return 表示式; }

// 只有一個參數時,括號才能不加:
(單一參數) => { 陳述式; }
單一參數 => { 陳述式; }

//若無參數，就一定要加括號:
() => { statements }

// 用大括號將內容括起來，返回一個物件字面值表示法：
params => ({foo: bar})

// 支援其餘參數與預設參數
(param1, param2, ...rest) => { statements }
(param1 = defaultValue1, param2, …, paramN = defaultValueN) => {
statements }

// 也支援 parameter list 的解構
var f = ([a, b] = [1, 2], {x: c} = {x: a + b}) => a + b + c; f(); // 6
```

## this 不分家

在有箭頭函數之前，每個新函式是依據如何被呼叫來定義自己的 this 變數 例如:

* 在建構子時是一個新物件&#x20;
* 在呼叫嚴格模式函數時是 undefined 以
* 物件方法呼叫時則為基礎物件&#x20;
* 等等....

很容易出錯。

```javascript
function Person() {
  // Person() 建構式將 this 定義為它自己的一個實體
  this.age = 0;

  setInterval(function growUp() {
    // 在非嚴格模式下, growUp() 函式把 this 定義為全域物件
    // (因為那是 growUp()執行的所在)，
    // 與 Person() 建構式所定義的 this 有所不同
    this.age++;
  }, 1000);
}

var p = new Person();
```

在 ECMAScript 3/5 裡面，有關 this 的問題，可以透過指派 this 值給可以關閉的變數解決。或者透過 bind 函式來綁定 this 變數到指定函式（以上面為例，就是 growUp() 函式）。

<mark style="color:red;">箭頭函式並不擁有自己的 this 變數；使用的 this 值來自封閉的文本上下文</mark>，也就是說，箭頭函式遵循常規變量查找規則。因此，如果在當前範圍中搜索不到 this 變量時，他們最終會尋找其封閉範圍。

```javascript
function Person(){
  this.age = 0;

  setInterval(() => {
    this.age++; // |this| 適切的參考了Person建構式所建立的物件
  }, 1000);
}

var p = new Person();
```

### 將箭頭函式撰寫為方法

箭頭函式並沒有自己的 this，會指向window或undefined。

```javascript
'use strict';
var obj = {
  i: 10,
  b: () => console.log(this.i, this),
  c: function() {
    console.log(this.i, this);
  }
}
obj.b(); // 印出 undefined, Window {...} (or the global object)
obj.c(); // 印出 10, Object {...}
```

### 使用 new 運算子時會出錯

箭頭函式不可作為建構式使用；若使用於建構式，會在使用 new 時候拋出錯誤。

```javascript
var Foo = () => {};
var foo = new Foo(); // TypeError: Foo is not a constructor
```

### 箭頭函數沒有 prototype 屬性

```javascript
var Foo = () => {};
console.log(Foo.prototype); // undefined
```

### yield 關鍵字無法用於箭頭函式的 body

箭頭函式無法使用 generator。

## 回傳物件字面值

請注意只使用 params => {object:literal} 並不會按照期望般回傳物件字面值（object literal）。

```javascript
var func = () => { foo: 1 };               // Calling func() returns undefined!
var func = () => { foo: function() {} };   // SyntaxError: Unexpected token (
```

因為在大括弧（{}）裡面的文字會被解析為有序宣告（例如 foo 會被當作標記（label）、而不是物件的 key ）要記得把物件字面值包在圓括弧內。

```javascript
var func = () => ({foo: 1});
var func = () => ({ foo: function() {} }); 
```

## 由 call 與 apply 函式呼叫

由於箭頭函式並沒有自己的 this，所以透過 call() 或 apply() 呼叫箭頭函式只能傳入參數。thisArg 將會被忽略。

```javascript
var adder = {
  base : 1,
  add : function(a) {
    var f = v => v + this.base;
    return f(a);
  },
  addThruCall: function(a) {
    var f = v => v + this.base;
    var b = {
      base : 2
    };
    return f.call(b, a);
  }
};
console.log(adder.add(1));         // 顯示 2
console.log(adder.addThruCall(1)); // 依舊顯示 2
```

## 不綁定 arguments

箭頭函式並沒有自己的 arguments 物件。所以在此例中，arguments 只是參考到 enclosing 作用域裡面的相同變數：

```javascript
var arguments = [1, 2, 3];
var arr = () => arguments[0];

arr(); // 1

function foo(n) {
  var f = () => arguments[0] + n; // foo's implicit arguments binding. arguments[0] is n
  return f();
}

foo(1); // 2
```

大多時候，使用其餘參數 是取代 arguments 物件的較好方式。

```javascript
function foo(n) {
  var f = (...args) => args[0] + n;
  return f(10);
}

foo(1); // 11
```
