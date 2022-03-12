# == 和 ===區別

## 等於(==)操作符

等於操作符用兩個等於號（ == ）表示，如果操作數相等，則會返回 true.&#x20;

因為在JavaScript中存在隱式轉換。等於操作符（==）在比較中會先進行類型轉換，再確定操作數是否相等。

小結：

* 兩個都為簡單類型，字串和布林值都會轉換成數值，再比較。
* 簡單類型與引用類型比較，物件轉化成其原始類型的值，再比較。
* 兩個都為引用類型，則比較它們是否指向同一個實例。
* null 和 undefined 相等。
* 存在 NaN 則返回 false。

如果任一操作數是布林值，則將其轉換為數值再比較是否相等。

```javascript
let result1 = (true == 1); // true
```

如果一個操作數是字串，另一個操作數是數值，則嘗試將字串轉換為數值，再比較是否相等。

```javascript
let result1 = ("55" == 55); // true
```

如果一個操作數是物件，另一個操作數不是，則調用物件的 valueOf()方法取得其原始值，再根據前面的規則進行比較。

```javascript
let obj = {valueOf:function(){return 1}}
let result1 = (obj == 1); // true
```

null和undefined相等。

```javascript
let result1 = (null == undefined ); // true
```

如果有任一操作數是 NaN ，則相等操作符返回 false。

```javascript
let result1 = (NaN == NaN ); // false
```

如果兩個操作數都是物件，則比較它們是不是同一個物件。如果兩個操作數都指向同一個物件，則相等操作符返回true。

```javascript
let obj1 = {name:"xxx"}
let obj2 = {name:"xxx"}
let result1 = (obj1 == obj2 ); // false
```

```javascript
var a = 10;
var b = 100;
// 同類型的比較沒有問題
console.log( a == b );        // false
console.log( a == 10 );       // true

// 不同類型的比較會自動轉型
var a = 10;
var b = "10";
console.log( a == b );        // true

true == 'true'      // false
false == 'false'    // false

false == 0    // true
true == 1     // true

[] == []      // false
[] == ![]     // true

[] == ''      // true
[] == 0       // true

[''] == ''    // true
[0] == 0      // true

[0] == ''     // false
[''] == 0     // true

null == undefined   // true

[null] == ''        // true
[null] == 0         // true

[undefined] == ''   // true
[undefined] == 0    // true
```

## 全等(===)操作符

全等操作符由 3 個等於號（ === ）表示，只有兩個操作數在不轉換的前提下相等才返回 true。即類型相同，值也需相同。

```javascript
let result1 = ("55" === 55); // false，不相等，因為數據類型不同
let result2 = (55 === 55); // true，相等，因為數據類型相同值也相同
```

undefined 和 null 與自身嚴格相等。

```javascript
let result1 = (null === null)  //true
let result2 = (undefined === undefined)  //true
```

## 兩種操作的比較

相等操作符（==）會做類型轉換，再進行值的比較，全等運算符不會做類型轉換。

```javascript
let result1 = ("55" === 55); // false，不相等，因為數據類型不同
let result2 = (55 === 55); // true，相等，因為數據類型相同值也相同
```

null 和 undefined 比較，相等操作符（==）為true，全等為false。

```javascript
let result1 = (null == undefined ); // true
let result2 = (null  === undefined); // false
```

## 轉型帶來的比較異常

相等運算符隱藏的類型轉換，會帶來一些違反直覺的結果。

```javascript
'' == '0' // false
0 == '' // true
0 == '0' // true

false == 'false' // false
false == '0' // true

false == undefined // false
false == null // false
null == undefined // true

' \t\r\n' == 0 // true
```

但在比較null的情況的時候，我們一般使用相等操作符==。

```javascript
const obj = {};

if(obj.x == null){
  console.log("1");  //執行
}
// 等價於
if(obj.x === null || obj.x === undefined) {
    ...
}
```

使用相等操作符（==）的寫法明顯更加簡潔了。所以，除了在比較對象屬性為null或者undefined的情況下，我們可以使用相等操作符（==），其他情況建議一律使用全等操作符（===）。

## 參考資料

* [Oh My Dear JavaScript Bizarre behaviors in JavaScript(比較運算子的異常行為表格)](https://thomas-yang.me/projects/oh-my-dear-js/)
