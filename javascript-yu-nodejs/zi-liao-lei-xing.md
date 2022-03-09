# 資料類型

簡介

在JavaScript中，我們可以分成兩種類型：

* 基本類型：in stack。
* 復雜類型：in heap。
* 兩種類型的區別是：存儲位置不同。

## 基本類型

基本類型主要為以下6種：

1. Number
2. String
3. Boolean
4. Undefined
5. null
6. symbol

### Number

數值最常見的整數類型格式則為十進制，還可以設置八進制（零開頭）、十六進制（0x開頭）。

```javascript
let intNum = 55 // 10進制的55
let num1 = 070 // 8進制的56
let hexNum1 = 0xA //16進制的10
```

浮點類型則在數值匯總必須包含小數點，還可通過科學計數法表示.&#x20;

```javascript
let floatNum1 = 1.1;
let floatNum2 = 0.1;
let floatNum3 = .1;     // 有效，但不推薦
let floatNum = 3.125e7; // 等於 31250000
```

在數值類型中，存在一個特殊數值NaN，意為“不是數值”，用於表示本來要返回數值的操作失敗了（而不是拋出錯誤）

```javascript
console.log(0/0);   // NaN
console.log(-0/+0); // NaN
```

### String

字串可以使用雙引號（"）、單引號（'）或反引號（\`）標示。

```javascript
let firstName = "John";
let lastName = 'Jacob';
let lastName = `Jingleheimerschmidt`
```

字串是不可變的，意思是一旦創建，它們的值就不能變了。

```javascript
let lang = "Java";
lang = lang + "Script";  // 先銷毀再創建
```

### Boolean

Boolean（布林值）類型有兩個字面值： true 和false。通過Boolean可以將其他類型的數據轉化成布林值。

| 資料類型      | 轉換為true之值  | 轉換為false之值 |
| --------- | ---------- | ---------- |
| String    | 非空字串       | ""         |
| Number    | 非零之值(包含無窮) | 0, NaN     |
| Object    | 任意物件       | null       |
| Undefined | 不存在        | undefined  |

### Undefined

Undefined 類型只有一個值，就是特殊值 undefined。當使用 var或 let聲明了變量但沒有初始化時，就相當於給變量賦予了 undefined值。

```javascript
let message;
console.log(message == undefined); // true
```

包含undefined 值的變量跟未定義變量是有區別的。

```javascript
let message; // 這個變量被聲明了，只是值為 undefined

console.log(message); // "undefined"
console.log(age);     // 沒有聲明過這個變量，報錯
```

### null

Null類型同樣只有一個值，即特殊值 null。邏輯上講， null 值表示一個空對象指標，這也是給typeof傳一個 null 會返回 "object" 的原因。

```javascript
let car = null;
console.log(typeof car); // "object"
```

undefined 值是由 null值衍生而來。

```javascript
console.log(null == undefined); // true
```

只要變量要儲存物件，而當時又沒有那個物件可儲存，就可用 null來填充該變量。

### Symbol

Symbol （符號）是原始值，且符號實例是唯一、不可變的。符號的用途是確保物件屬性使用唯一標識符，不會發生屬性沖突的危險。

```javascript
let genericSymbol = Symbol();
let otherGenericSymbol = Symbol();
console.log(genericSymbol == otherGenericSymbol); // false
typeof genericSymbol // 'symbol'

let fooSymbol = Symbol('foo');
let otherFooSymbol = Symbol('foo');
console.log(fooSymbol == otherFooSymbol); // false
```

##
