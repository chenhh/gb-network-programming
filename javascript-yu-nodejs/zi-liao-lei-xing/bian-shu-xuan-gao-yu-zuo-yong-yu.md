# 變數宣告與作用域

## 全域變數與區域變數

其實在 JavaScript 這門語言中，沒有所謂「全域變數」這種東西。 更準確地說，<mark style="color:red;">我們所說的「全域變數」其實指的是「全域物件」(或者叫「頂層物件」) 的屬性</mark>。

* 以瀏覽器來說，「全域物件」指的就是 `window`，在 node 環境中則叫做 `global`。
* 變數有效範圍 (scope) 的最小切分單位是 function (ES6 的 let 與 const 例外) 。
* 即使是寫在函式內，沒有 var 的變數會變成「全域變數」 。
* 全域變數指的是全域物件 (頂層物件) 的「屬性」。

## 作用域(Scope) & 區塊(Block)

每個程式語言在設計上都會有作用域(Scope)的概念，簡單來說就是指變數可以活動及作用的範圍。

比較嚴謹的語言會透過特殊符號，像是角括號{...}，將某段程式包覆起來形成區塊(Block)，裡面的變數的作用域不要漫無邊際。而這樣的變數也稱為<mark style="color:red;">區域變數(local variable)。</mark>

相反地，如果變數沒有被任何區塊包覆，那麼它的作用域就是整個程式本身，這樣的變數就被稱為<mark style="color:red;">全域變數(global variable)</mark>。

## var 與 let 宣告變數的主要差別

<mark style="color:red;">建議：在撰寫指令碼的日常中，let(從ES6支援)可以幾乎完美替代var</mark>。

<mark style="color:red;">簡單的說：作用域不一樣，var的作用域在函式 (function) 裡，let的作用域則是在區塊 (block) 裡</mark>。

```javascript
if(true){
  //Start of Block scope
  let b = 'Hi I am in Block';
  //End of Block scope
}
console.log(b);
//ReferenceError 

(function(){
  var s = 'Hi I am in Function';
}())
console.log(s) 
//ReferenceError 
```

<mark style="color:red;">var 在作用域可以被重複宣告， let / const 在作用域內重複宣告則是會報錯，暫時性死區</mark>。因此在沒有let宣告時，當時很多 library / 框架要用閉包 (closure) 去把var宣告的變數包起來。

```javascript
{
  let medium = 'good!';
  let medium = 20;
  //SyntaxError: Identifier 'medium' has already been declared
}

//vs
{
  var already = 'no';
  var already = 'yes';
  console.log(already); //yes
}
```

### var異常：for-loop處理回撥函式(callback function)

```javascript
for ( var i = 0 ; i < 3 ; i++ ) {
	setTimeout( function() { console.log(i) } , 1000 );
}
//3
//3
//3
```

setTimeout是一個會去註冊一個callback function，1秒後執行。在作用域沒有管控好的狀況下，loop裡頭的非同步事件會去註冊起來，且使用var宣告的變數仍然會直到 i = 3 時才停止(然而這只是幾個瞬間的事)。

解法1：closure

```javascript
for( var i = 0 ; i < 3 ; i++ ){
	( function (j) {
		//function scope
		setTimeout(function(){ console.log(j) })
	} ( i )) // 把i傳進去這個閉包
}
```

解法2：用let宣告變數

```javascript
for ( let k = 0 ; k <3 ; k++ ){
	setTimeout( function(){ console.log(k) } , 1000 ) ;
}
//0
//1
//2
```

### var異常：變數提升(hoisting)

## 提升(Hoisting)

在解析階段時，變數的宣告都會先被放入記憶體中。在執行階段時，就不會因為參考不到變數就出現錯誤。

## let & const

以往的`var`已經無法讓開發上有更好的維護性跟解讀性。 因此在 ES2015 的規範中，除了local與global兩種作用域外，新增了**區塊作用域(block scope)**來引入區域變數的機制，並根據變數的用途建立了兩個新的關鍵字。

* let: 宣告區域變數，作用域包含for ...區塊、if ...區塊，和不帶任何控制目的純區塊中。在同一區塊不得重複宣告，增加嚴謹性。
* const: 宣告區域常數，僅能在宣告時設定好初始值，並且不得再變動。

## 解構賦值 (Destructuring)

這個特性可以對陣列或物件中的資料，進行解開，各自擷取為獨立的變數。目的是讓開發上對於某些特定資料可以更方便存取。

### array

```javascript
const sampleArr = [1, 2, 3];

//ES 2015
let [x, y, z] = sampleArr;
console.log(x, y, z); // 1 2 3

//ES5
var x1 = sampleArr[0],
  y1 = sampleArr[1],
  z1 = sampleArr[2];
console.log(x1, y1, z1); // 1 2 3
```

另外等號兩邊的數量不一定要相等，可以透過給預設值或空位來宣告，相當彈性。

```javascript
const sampleArr = ["a", "b", "c"];

// 左邊少於右邊
let [x, y] = sampleArr;
console.log(x, y); // a b

// 左邊多於右邊
// 變數 q 沒被分配到值，預設為 undefined
// 變數 r 雖然也沒被分配到值，但是可以設定預設值，因此不會變成 undefined
let [x, y, z, q, r = "d"] = sampleArr;
console.log(x, y, z, q); // a b c undefined d

//特定位置可以給空位
let [x, , y] = sampleArr;
console.log(x, y); // a c
```

### Object

```javascript
const obj = { id: 1, name: "yuri", age: "20", gender: "female" };

const { name, age, hobby, country = "Taiwan" } = obj;
console.log(name, age, hobby, country); //yuri 20 undefined Taiwan
```

## 參考資料

* [JavaScript Visualized: Scope (Chain)](https://dev.to/lydiahallie/javascript-visualized-scope-chain-13pd)
* [JavaScript Visualized: Hoisting](https://dev.to/lydiahallie/javascript-visualized-hoisting-478h)
* [JavaScript Visualized: Event Loop](https://dev.to/lydiahallie/javascript-visualized-event-loop-3dif)
* J[avaScript Visualized: the JavaScript Engine](https://dev.to/lydiahallie/javascript-visualized-the-javascript-engine-4cdf)
* [JavaScript Visualized: Generators and Iterators](https://dev.to/lydiahallie/javascript-visualized-generators-and-iterators-e36)
* [JavaScript Visualized: Promises & Async/Await](https://dev.to/lydiahallie/javascript-visualized-promises-async-await-5gke)
* [\[JavaScript\] 你應該使用 let 而不是 var 的 3 個重要理由](https://realdennis.medium.com/%E6%87%B6%E4%BA%BA%E5%8C%85-javascript%E4%B8%AD-%E4%BD%BF%E7%94%A8let%E5%8F%96%E4%BB%A3var%E7%9A%843%E5%80%8B%E7%90%86%E7%94%B1-f11429793fcc)
