# 資料類型

簡介

在JavaScript中，我們可以分成兩種類型：

* 基本類型：(copy/call by value)。
* 復雜類型：(copy/call by reference)。
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

#### Number.MIN\_SAFE\_INTEGER／Number.MAX\_SAFE\_INTEGER

為了方便，不需再經過數學運算取得，在Number物件中新增安全最大正整數與安全最小負整數的靜態屬性，分別為正負2的53次方減1。

```javascript
Number.MAX_SAFE_INTEGER // 9007199254740991
Number.MIN_SAFE_INTEGER // -9007199254740991
```

#### Number.NaN

在ES5以前就有全域的屬性可以取得。不過在ES2015後擴充成為Number物件裡的靜態屬性。

#### Number.isSafeInteger(value)

判斷數值是否為落在安全整數範圍內的整數，回傳結果為布林值。

```javascript
Number.isSafeInteger(Number.MAX_SAFE_INTEGER) // true
Number.isSafeInteger(Number.MAX_SAFE_INTEGER+1) // false
```

#### Number.isInteger(value)

判斷數值是否為整數，回傳結果為布林值。

```javascript
Number.isInteger(25) //true
Number.isInteger(-88) //true
Number.isInteger(0) //true
Number.isInteger(3.14) //false
Number.isInteger(-8.2544) //false
```

在ES2015後，鼓勵是以模組化的方式開發，其中就包含降低全域方法的使用。所以像是parseInt()、parseFloat()和isNaN()，在Number物件裡也有實現同樣的方法。

#### Number.parseInt(value, radix)

將輸入的字串轉成整數。如果無法轉為數值，則回傳NaN。 radix指的是從2 \~ 36的進位系統指定。

```javascript
Number.parseInt('-532');  //-532
Number.parseInt('  3  ');  //3
Number.parseInt('NaN');  //NaN
Number.parseInt('true');  //NaN
```

#### Number.parseFloat(value)

將輸入的字串轉成浮點數。如果無法轉為數值，則回傳NaN。

```javascript
Number.parseFloat('-532.2546');  //-532.2546
Number.parseFloat('  3.14  ');  //3.14
Number.parseFloat('NaN');  //NaN
Number.parseFloat('true');  //NaN
```

#### Number.isNaN(value)

判斷數值是否為NaN，回傳結果為布林值。

```javascript
Number.isNaN(NaN) // true
Number.isNaN('NaN') // false
Number.isNaN(true) // false
Number.isNaN(88) // false
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

我們也可將字串常用的操作方法歸納為新增、刪除、修改、查詢，需要知道字串的特點是一旦創建了，就不可變。

### string常用新增方法

這裡增的意思並不是說直接增添內容，而是創建字串的一個副本，再進行操作。除了常用`+`以及`${}`進行字串拼接之外，還可通過`concat()`。

concat()用於將一個或多個字串拼接成一個新字串。

```javascript
let stringValue = "hello ";
let result = stringValue.concat("world");
console.log(result); // "hello world"
console.log(stringValue); // "hello"
```

### string常用刪除方法

這裡的刪的意思並不是說刪除原字串的內容，而是創建字串的一個副本，再進行操作。

常見的有：

* slice()
* substr()
* substring()&#x20;

這三個方法都返回調用它們的字串的一個子字串，而且都接收一或兩個參數。

```javascript
let stringValue = "hello world";
console.log(stringValue.slice(3)); // "lo world"
console.log(stringValue.substring(3)); // "lo world"
console.log(stringValue.substr(3)); // "lo world"
console.log(stringValue.slice(3, 7)); // "lo w"
console.log(stringValue.substring(3,7)); // "lo w"
console.log(stringValue.substr(3, 7)); // "lo worl"
```

### string常用修改方法

這裡改的意思也不是改變原字串，而是創建字串的一個副本，再進行操作。常見的有：

* trim()、trimLeft()、trimRight()
* repeat()
* padStart()、padEnd()
* toLowerCase()、 toUpperCase()

trim()、trimLeft()、trimRight() 刪除前、後或前後所有空格符，再返回新的字串。

```javascript
let stringValue = " hello world ";
let trimmedStringValue = stringValue.trim();
console.log(stringValue); // " hello world "
console.log(trimmedStringValue); // "hello world"
```

repeat() 接收一個整數參數，表示要將字串復制多少次，然後返回拼接所有副本後的結果。

```javascript
let stringValue = "na ";
let copyResult = stringValue.repeat(2) // na na 
```

padEnd() 復制字串，如果小於指定長度，則在相應一邊填充字元，直至滿足長度條件。

```javascript
let stringValue = "foo";
console.log(stringValue.padStart(6)); // " foo"
console.log(stringValue.padStart(9, ".")); // "......foo"
```

toLowerCase()、 toUpperCase() 大小寫轉化。

```javascript
let stringValue = "hello world";
console.log(stringValue.toUpperCase()); // "HELLO WORLD"
console.log(stringValue.toLowerCase()); // "hello world"
```

### string常用查詢方法

除了通過索引的方式獲取字串的值，還可通過：

* chatAt()
* indexOf()
* startWith()
* includes()

charAt() 返回給定索引位置的字元，由傳給方法的整數參數指定。

```javascript
let message = "abcde";
console.log(message.charAt(2)); // "c"
```

indexOf() 從字串開頭去搜尋傳入的字串，並返回位置（如果沒找到，則返回 -1 ）

```javascript
let stringValue = "hello world";
console.log(stringValue.indexOf("o")); // 4
```

startWith()、includes() 從字串中搜尋傳入的字串，並返回一個表示是否包含的布林值。

```javascript
let message = "foobarbaz";
console.log(message.startsWith("foo")); // true
console.log(message.startsWith("bar")); // false
console.log(message.includes("bar"));   // true
console.log(message.includes("qux"));   // false
```

### string常用轉換方法

split()把字串按照指定的分割符，拆分成數組中的每一項。

```javascript
let str = "12+23+34"
let arr = str.split("+") // [12,23,34]
```

### string常用模板匹配方法

針對正則表達式，字串設計了幾個方法：

* match()
* search()
* replace()

match() 接收一個參數，可以是一個正則表達式字串，也可以是一個RegExp對象，返回陣列。

```javascript
let text = "cat, bat, sat, fat";
let pattern = /.at/;
let matches = text.match(pattern);
console.log(matches[0]); // "cat"
```

search() 接收一個參數，可以是一個正則表達式字串，也可以是一個RegExp對象，找到則返回匹配索引，否則返回 -1。

```javascript
let text = "cat, bat, sat, fat";
let pos = text.search(/at/);
console.log(pos); // 1
```

replace() 接收兩個參數，第一個參數為匹配的內容，第二個參數為替換的元素（可用函數）。

```javascript
let text = "cat, bat, sat, fat";
let result = text.replace("at", "ond");
console.log(result); // "cond, bat, sat, fat"
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

## 引用型別

復雜類型統稱為Object，這裡主要講述下面三種：

* Object
* Array
* Function

除了上述說的三種之外，還包括Date、RegExp、Map、Set等。

### Object

創建object常用方式為物件字面量表示法，屬性名可以是字串或數值：

```javascript
let person = {
    name: "Nicholas",
    "age": 29,
    5: true
};
```

### Array

JavaScript陣列是一組有序的資料，但跟其他語言不同的是，陣列中每個槽位可以存儲**任意類型**的資料。並且，陣列也是動態大小的，會隨著資料新增而自動增長。

```javascript
let colors = ["red", 2, {age: 20 }]
colors.push(2)
```

### array常用新增方法

下面前三種是對原陣列產生影響的增添方法，第四種則不會對原陣列產生影響：

* push()&#x20;
* unshift()
* splice()
* concat()

push()方法接收任意數量的參數，並將它們新增到陣列末尾，返回陣列的最新長度。

```javascript
let colors = []; // 創建一個陣列
let count = colors.push("red", "green"); // 推入兩項
console.log(count) // 2
```

unshift()在陣列開頭新增任意多個值，然後返回新的陣列長度。

```javascript
let colors = new Array(); // 創建一個陣列
let count = colors.unshift("red", "green"); // 從陣列開頭推入兩項
alert(count); // 2
```

splice傳入三個參數，分別是開始位置、0（要刪除的元素數量）、插入的元素，返回空陣列。

```javascript
let colors = ["red", "green", "blue"];
let removed = colors.splice(1, 0, "yellow", "orange")
console.log(colors) // red,yellow,orange,green,blue
console.log(removed) // []
```

concat()首先會創建一個當前陣列的副本，然後再把它的參數新增到副本末尾，最後返回這個新構建的陣列，不會影響原始陣列。

```javascript
let colors = ["red", "green", "blue"];
let colors2 = colors.concat("yellow", ["black", "brown"]);
console.log(colors); // ["red", "green","blue"]
console.log(colors2); // ["red", "green", "blue", "yellow", "black", "brown"]
```

### array常用刪除方法

下面三種都會影響原陣列，最後一項不影響原陣列：

* pop()
* shift()
* splice()
* slice()

pop() 方法用於刪除陣列的最後一項，同時減少陣列的length 值，返回被刪除的項。

```javascript
let colors = ["red", "green"]
let item = colors.pop(); // 取得最後一項
console.log(item) // green
console.log(colors.length) // 1
```

shift()方法用於刪除陣列的第一項，同時減少陣列的length 值，返回被刪除的項。

```javascript
let colors = ["red", "green"]
let item = colors.shift(); // 取得第一項
console.log(item) // red
console.log(colors.length) // 1
```

splice()傳入兩個參數，分別是開始位置，刪除元素的數量，返回包含刪除元素的陣列。

```javascript
let colors = ["red", "green", "blue"];
let removed = colors.splice(0,1); // 刪除第一項
console.log(colors); // green,blue
console.log(removed); // red，只有一個元素的陣列
```

slice() 用於創建一個包含原有陣列數組中一個或多個元素的新陣列，不會影響原始陣列。

```javascript
let colors = ["red", "green", "blue", "yellow", "purple"];
let colors2 = colors.slice(1);
let colors3 = colors.slice(1, 4);
console.log(colors)   // red,green,blue,yellow,purple
concole.log(colors2); // green,blue,yellow,purple
concole.log(colors3); // green,blue,yellow
```

### array常用查詢方法

即查詢元素，返回元素坐標或者元素值

* indexOf()
* includes()
* find()

indexOf()返回要查詢的元素在陣列中的位置，如果沒找到則返回 -1。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
numbers.indexOf(4) // 3
```

includes()返回要查詢的元素在數組中的位置，找到返回true，否則false。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
numbers.includes(4) // true
```

find()返回第一個匹配的元素。

```javascript
const people = [
    {
        name: "Matt",
        age: 27
    },
    {
        name: "Nicholas",
        age: 29
    }
];
people.find((element, index, array) => element.age < 28) // // {name: "Matt", age: 27}
```

### array常用排序方法

有兩個方法可以用來對元素重新排序：

* reverse()
* sort()

reverse()顧名思義，將陣列元素方向反轉。

```javascript
let values = [1, 2, 3, 4, 5];
values.reverse();
alert(values); // 5,4,3,2,1
```

sort()方法接受一個比較函數，用於判斷哪個值應該排在前面。

```javascript
function compare(value1, value2) {
    if (value1 < value2) {
        return -1;
    } else if (value1 > value2) {
        return 1;
    } else {
        return 0;
    }
}
let values = [0, 1, 5, 10, 15];
values.sort(compare);
alert(values); // 0,1,5,10,15
```

### array常用轉換方法

join() 方法接收一個參數，即字串分隔符，返回包含所有項的字串.&#x20;

```javascript
let colors = ["red", "green", "blue"];
alert(colors.join(",")); // red,green,blue
alert(colors.join("||")); // red||green||blue
```

### array常用迭代方法

常用來迭代數組的方法（都不改變原陣列）有如下：

* some()
* every()
* forEach()
* filter()
* map()

some()對陣列每一項都運行傳入的函數，如果有一項函數返回 true ，則這個方法返回 true。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
let someResult = numbers.some((item, index, array) => item > 2);
console.log(someResult) // true
```

every()對陣列數組每一項都運行傳入的函數，如果對每一項函數都返回 true ，則這個方法返回 true。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
let everyResult = numbers.every((item, index, array) => item > 2);
console.log(everyResult) // false
```

forEach()對陣列每一項都運行傳入的函數，沒有返回值。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
numbers.forEach((item, index, array) => {
    // 執行某些操作
});
```

filter()對陣列每一項都運行傳入的函數，函數返回 true 的項會組成陣列之後返回。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
let filterResult = numbers.filter((item, index, array) => item > 2);
console.log(filterResult); // 3,4,5,4,3
```

map()對陣列每一項都運行傳入的函數，返回由每次函數調用的結果構成的陣列。

```javascript
let numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1];
let mapResult = numbers.map((item, index, array) => item * 2);
console.log(mapResult) // 2,4,6,8,10,8,6,4,2
```

### Function

函數實際上是物件，每個函數都是 Function類型的實例，而 Function也有屬性和方法，跟其他引用類型一樣。函數存在三種常見的表達方式：

函數聲明

```javascript
// 函數聲明
function sum (num1, num2) {
    return num1 + num2;
}
```

函數表達式

```javascript
let sum = function(num1, num2) {
    return num1 + num2;
};
```

箭頭函數

```javascript
let sum = (num1, num2) => {
    return num1 + num2;
};
```
