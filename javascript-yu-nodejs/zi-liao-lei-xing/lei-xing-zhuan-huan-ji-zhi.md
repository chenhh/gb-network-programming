# 類型轉換機制

## 概述

JS中有六種簡單數據類型：undefined、null、boolean、string、number、symbol，以及引用類型：object。但是我們在宣告的時候只有一種資料類型，只有到運行期間才會確定當前類型。

```javascript
// x的值在編譯階段是無法獲取的，只有等到程式運行時才能知道
let x = y ? 1 : a;
```

雖然變量的資料類型是不確定的，但是各種運算符對資料類型是有要求的，如果運運算元的類型與預期不符合，就會觸發類型轉換機制。

常見的類型轉換有：

* 強制轉換（顯示轉換）&#x20;
* 自動轉換（隱式轉換)

## 顯示轉換

顯示轉換，即我們很清楚可以看到這裡發生了類型的轉變，常見的方法有：

* Number()&#x20;
* parseInt()&#x20;
* String()&#x20;
* Boolean()

### Number()&#x20;

將任意類型的值轉化為數值，先給出類型轉換規則。

##

| 原始值       | 轉換值                                                    |
| --------- | ------------------------------------------------------ |
| undefined | NaN                                                    |
| null      | 0                                                      |
| true      | 1                                                      |
| false     | 0                                                      |
| string    | 根據語法與規則轉換，Number轉換的時候是很嚴格的，只要有一個字元無法轉成數值，整個字串就會被轉為NaN。 |
| symbol    | Throw a  typeerror exception                           |
| Object    | 先呼叫toPrimitive，再呼叫toNumber                             |

```javascript
Number(324) // 324

// 字串：如果可以被解析為數值，則轉換為相應的數值
Number('324') // 324

// 字串：如果不可以被解析為數值，返回 NaN
Number('324abc') // NaN

// 空字串轉為0
Number('') // 0

// 布林值：true 轉成 1，false 轉成 0
Number(true) // 1
Number(false) // 0

// undefined：轉成 NaN
Number(undefined) // NaN

// null：轉成0
Number(null) // 0

// 物件：通常轉換成NaN(除了只包含單個數值的陣列)
Number({a: 1}) // NaN
Number([1, 2, 3]) // NaN
Number([5]) // 5
```

### parseInt()

parseInt相比Number，就沒那麼嚴格了，parseInt函數逐個解析字元，遇到不能轉換的字元就停下來。

```javascript
parseInt('32a3') //32
```

### String()

可以將任意類型的值轉化成字串。

| 原始值       | 轉換值                         |
| --------- | --------------------------- |
| undefined | 'undefined'                 |
| boolean   | "true"或"false"              |
| Number    | 數字變為字串                      |
| String    | String                      |
| Symbol    | throw a TypeError exception |
| Object    | 先呼叫toPrimitive，再呼叫toNumber  |

```javascript
// 數值：轉為相應的字串
String(1) // "1"

//字串：轉換後還是原來的值
String("a") // "a"

//布林值：true轉為字串"true"，false轉為字串"false"
String(true) // "true"

//undefined：轉為字串"undefined"
String(undefined) // "undefined"

//null：轉為字串"null"
String(null) // "null"

//對象
String({a: 1}) // "[object Object]"
String([1, 2, 3]) // "1,2,3"
```

### Boolean()&#x20;

可以將任意類型的值轉為布林值，轉換規則如下：

| 資料類型      | 轉換為true的值  | 轉換為false的值 |
| --------- | ---------- | ---------- |
| Boolean   | true       | false      |
| String    | 非空字串       | ""(空字串)    |
| Number    | 非零數值(包括無窮) | 0, NaN     |
| Object    | 任意物件       | null       |
| Undefined | 不存在        | undefined  |

```javascript
Boolean(undefined) // false
Boolean(null) // false
Boolean(0) // false
Boolean(NaN) // false
Boolean('') // false
Boolean({}) // true
Boolean([]) // true
Boolean(new Boolean(false)) // true
```

## 隱式轉換

我們這裡可以歸納為兩種情況發生隱式轉換的場景：

* 比較運算（==、!=、>、<)，if、while需要布林值地方&#x20;
* 算術運算（+、-、\*、/、%）

除了上面的場景，還要求運算符兩邊的操作數不是同一類型。

### 自動轉換為布林值

在需要布林值的地方，就會將非布林值的參數自動轉為布林值，系統內部會調用Boolean函數。

可以得出個小結：

* undefined&#x20;
* null&#x20;
* false&#x20;
* \+0&#x20;
* \-0&#x20;
* NaN&#x20;
* ""&#x20;

除了上面幾種會被轉化成false，其他都換被轉化成true。

### 自動轉換成字串

遇到預期為字串的地方，就會將非字串的值自動轉為字串。具體規則是：先將復合類型的值轉為原始類型的值，再將原始類型的值轉為字串。常發生在+運算中，一旦存在字串，則會進行字串拼接操作。

```javascript
'5' + 1 // '51'
'5' + true // "5true"
'5' + false // "5false"
'5' + {} // "5[object Object]"
'5' + [] // "5"
'5' + function (){} // "5function (){}"
'5' + undefined // "5undefined"
'5' + null // "5null"
```

### 自動轉換成數值

除了+有可能把運運算元轉為字串，其他運算符都會把運運算元自動轉成數值。

```javascript
'5' - '2' // 3
'5' * '2' // 10
true - 1  // 0
false - 1 // -1
'1' - 1   // 0
'5' * []    // 0
false / '5' // 0
'abc' - 1   // NaN
null + 1 // 1
undefined + 1 // NaN
```

null轉為數值時，值為0 。undefined轉為數值時，值為NaN。
