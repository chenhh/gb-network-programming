# FAQ

## Java 跟 JavaScript的關係

大概就像是「臘腸」跟「臘腸狗」的關係吧，只是兩者的樣子有「一點點」類似，就把名字借來用了。

## ECMAScript 與 JavaScript 的關係

ECMA標準是規格書，而 JavaScript、JScript 這類語言，就是依循這份規格書所實作出來的產品了。

ECMA-262 標準在 1997 年提出第一個版本，而目前最廣為人知的應該是 1999 年底所提出的 ECMA-262 第三版，現在的瀏覽器，幾乎都能支援這個版本，又稱 ECMAScript 3，對應的實作為 JavaScript 1.5。

由於各方對 ECMAScript 第四版意見發生嚴重分岐，後來決定終止開發，只針對原有規範中一小部份的現有功能作改進，並發布為 ECMAScript 3.1，後來乾脆改名為 ECMAScript 5。

自 ECMAScript 6 開始，負責制定 ECMAScript 標準的委員會 (TC39) 決定將新標準改為一年一修。因此包括 ES6 開始往後的版本都會定為 ECMAScript 2015 (ES6)、ECMAScript 2016、ECMAScript 2017 持續下去。

## 為何成為瀏覽器唯一指定內建程式語言？

由於 JavaScript 的發行獲得了成功，使得微軟在 1996 年發佈 IE 3.0 的時候，也開始加入了指令碼語言的支援，分別是 VBScript 與 JScript。

VBScript 是微軟自家開發的指令碼型程式語言，可以把它看作是 VB 語言的簡化版，長久以來都只有 IE 可以執行，但自 IE11 起已不再支援 VBScript 了。

而 JScript 雖然同樣是由微軟自家開發，類似於 JavaScript。 早期的 JScript 可以當作是微軟想要與 Netscape 的 JavaScript 打對台的產品，但考量到相容性與市場 (開發者不會願意為不同的瀏覽器寫好幾份 code，而當時 Netscape 市佔比 IE 高)，於是微軟、網景雙方(就網頁標準上)漸漸靠攏。

由於 Netscape 在 1996 年對 JavaScript 提出了標準化，第一個標準化版本 ECMA-262 在 1997 年就此誕生，也因為 Java 名稱上具有商標問題，ECMA-262 採用了 ECMAScript 作為語言名稱，JavaScript 此後成為了 ECMA-262 標準的實作語言，也變成瀏覽器唯一指定內建程式語言。

## \[變數宣告]JavaScript中 var 與 let 的主要差別

ES5以前就有的var，ES6新增加let與const。

簡答：

* 作用域不一樣，var的作用域在函式 (function) 裡，let的作用域則是在區塊 (block) 裡。撰寫程式的日常中，let可以幾乎完美替代var。
* var 在作用域為什麼可以被重複宣告， let / const 在作用域內重複宣告則是會報錯，暫時性死區等等。
* 若是直接對一沒宣告過的變數做賦值的動作，可能會發生「全域作用域污染」(變數直接視為全域變數)。

```javascript
// 由於var作用域為function，因此會全部印出3
for ( var i = 0 ; i < 3 ; i++ ) {
	setTimeout( function() { console.log(i) } , 1000 );
}
//3
//3
//3

// 解法一：使用closure
for( var i = 0 ; i < 3 ; i++ ){
	( function (j) {
		//function scope
		setTimeout(function(){ console.log(j) })
	} ( i )) // 把i傳進去這個閉包
}

// 解法二：使用let限制變數作用域
for ( let k = 0 ; k <3 ; k++ ){
	setTimeout( function(){ console.log(k) } , 1000 ) ;
}
//0
//1
//2
```

```javascript
{
  let medium = 'good!';
  let medium = 20;
  //SyntaxError: Identifier 'medium' has already been declared
}

{
  var already = 'no';
  var already = 'yes';
  console.log(already); //yes
}
```

```javascript
// g沒有被宣告而被直接使用會變成全域變數
(function function1(){
  var t = 10;
  
  (function function2(){
    g = 20;
  }())
  
}())
//console.log(t) Reference Error

console.log(g)
//global.g(Nodejs) or window.g(Browser)
```

## \[函數宣告]一般函數與箭頭函數的差異

```javascript
// 正常寫法
function callSomeone(someone){
  return someone + '吃飯了'
}

// 箭頭函數
var callSomeone = (someone) => {
  // 在大括號內的 {} 是需要自行加入 return，如果沒有傳入值則會出現 undefined
  return someone + '吃飯了'
}
console.log(callSomeone('小明'))

// 縮寫，單一行陳述不需要 {}
var callSomeone = (someone) => someone + '吃飯了'
console.log(callSomeone('小明'))

// 只有一個引數可以不加括號
var callSomeone = someone => someone + '吃飯了'
console.log(callSomeone('小明'))

// 沒有引數時，一定要有括號
var callSomeone = () => '小明' + '吃飯了'
console.log(callSomeone('小明'))
```

### 箭頭函數沒有 arguments 引數

```javascript
let originCash = 1000;
const updateEasyCard = () => {
  let cash = 0;
  console.log(arguments); // arguments is not defined
}

updateEasyCard(10, 50, 100, 50, 5, 1, 1, 1, 500);
```

### 兩種函數定義方法繫結到的this物件不同

* 傳統函式：依呼叫的方法而定&#x20;
* 箭頭函式：繫結到其定義時所在的物件 (這個詞看似簡單，但又充滿了陷阱!?)

```javascript
var name = '全域阿姨'
var auntie = {
  name: '地方媽媽',
  callName: function () { 
    // 注意，這裡是 function，以此為基準產生一個作用域
    console.log('1', this.name); // 1 地方媽媽
    setTimeout(() => {
      console.log('2', this.name); // 2 地方媽媽
      console.log('3', this); // 3 auntie 這個物件
    }, 10);
  },
  callName2: () => { 
    // 注意，如果使用箭頭函式，this 依然指向 window
    console.log('4', this.name); // 4 全域阿姨
    setTimeout(() => {
      console.log('5', this.name); // 5 全域阿姨
      console.log('6', this); // 6 window 物件
    }, 10);
  }
}

auntie.callName();
auntie.callName2();
```

繫結到其定義時所在的物件，我們要瞭解**一般函式在建立時是在 window 下，所以在 window 下使用箭頭函式自然會指向 window**，要確實將箭頭函式宣告在物件內部，這樣 this 才會指向該物件。

* func() 是最外層的函式，他對於內層的箭頭不會有影響。&#x20;
* func2() 是包覆在內層的函式，但由於箭頭函式不是在物件內，所以沒有影響。&#x20;
* func3() 是呼叫在物件內的函式，因此箭頭函式會是使用它所在的物件。

```javascript
var func = function () {
  var func2 = function () {
    setTimeout(() => {
      console.log(this); 
    }, 10);
  };
  // 這裡才算真正的建立一個物件
  // 因此要在此物件下的箭頭函式才會以此作為基準
  var func3 = {
    func: func2,
    var4: 4
  }
  func2(); // this = window
  func3.func(); // func3 Object
}
func(); 
// 就算在這裡新增一個 function，也不會影響到內層的箭頭函式
```

### 縮寫的函式為一般函數,this指向呼叫的物件

```javascript
var auntie = {
  name: '漂亮阿姨',
  callName () { 
    // 注意，縮寫形式的 function 屬於傳統 function
    setTimeout(() => {
      console.log(this); // auntie 這個物件
    }, 10);
  }
}
auntie.callName();
```

## this在箭頭函數無法使用的情形

### apply, call, bind this 在 Arrow function 中是被繫結的，所以套用 call 的方法時是無法修改 this。

```javascript
let family = {
  ming: '小明'
}
const func = () => {
  console.log(this);
}
const func2 = function () {
  console.log(this);
}
func.call(family); // 箭頭函式的情況，this 依然是 window
func2.call(family); // 一般函示 this 則是傳入的物件
```

### 不能用在建構式

由於 this 的是在物件下建立，所以箭頭函式不能像 function 一樣作為建構式的函式，如果嘗試使用此方法則會出現錯誤 (... is not a constructor)。

```javascript
const PhoneTemplate = (brand, modal, withCamera) => {
  this.brand = brand;
  this.modal = modal;
  // ...
}

const sonyPhone = new PhoneTemplate('Sony', 'Z100', true);
// 錯誤：PhoneTemplate is not a constructor
```

### 不能用於DOM 事件監聽

this 是指向所建立的物件上，如果是用在監聽 DOM 上一樣會指向 window，所以無法使用在此情境。

```javascript
var elements = document.getElementsByTagName('div');
var changeDOM = () => {
  console.log(this);                   // 指向 window Object
  this.style.border = '1px solid red'. // 錯誤
}

for (var i = 0; i < elements.length; i++) {
  elements[i].addEventListener('click', changeDOM, false);
}
```

### 不能在Prototype 中使用 this

一樣是 this 的問題，如果原型上新增一個箭頭函式，並嘗試使用 this 的話會指向全域。

```javascript
function PhoneTemplate (brand, modal, withCamera) {
  this.brand = brand;
  this.modal = modal;
  // ...
}

PhoneTemplate.prototype.callSomeone = function (someone) {
  console.log(this.brand + ' 打通電話給 ' + someone)
}
PhoneTemplate.prototype.callSomeone2 = (someone) => {
  console.log(this.brand + ' 打通電話給 ' + someone)
}

const sonyPhone = new PhoneTemplate('Sony', 'Z100', true);
sonyPhone.callSomeone('小明'); // Sony 打通電話給 小明
sonyPhone.callSomeone2('傑哥'); // undefined 打通電話給 傑哥
```

## ++運算子

\++運算子放在變數前與變數後的行為和C++一致。

* \++ 放在變數前面時，得到的會是「+1 之後的結果」
* \++ 放在變數後面時，回傳的結果會是「原始的數值」

```javascript
var a = 10;
var b = 10;

console.log(a++);       // 10
console.log(++b);       // 11

console.log(a);         // 11
console.log(b);         // 11
```

## 比較時自動轉型的規則

在兩個等號 == 的比較運算式下，若是雙方的資料型別不同時，則會進行「自動轉型」，那麼這裡就來說明自動轉型的規則。

在 JavaScript 這門程式語言中，大家會提倡儘量使用 === 來取代 == 。

* 如果其中有一個值為「Boolean」的情況下，會將 true 轉型為「數字」的 1， false 則會變成數字的 0&#x20;
* 如果遇到字串與數字做比較的情況下，則會將字串透過 Number() 嘗試轉型為數字後，再進行比較。&#x20;
* 如果其中一方是「物件」型別，而另一方是基本型別的情況下，則會先透過物件的 valueOf() 方法取得對應的基本型別的值，再進行比較。
* NaN 不等於 NaN，不管是兩個等號或三個等號都一樣。&#x20;
* 當兩個物件進行比較時，要看兩者是否指向同一個「實體」，只有在指向同一個「實體」時才會回傳 true。

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

* [\[參考資料\]Javascript真值表](https://thomas-yang.me/projects/oh-my-dear-js/)

## 函式是物件的一種

除了基本型別以外的都是物件。

當我們透過 typeof 去檢查一個「函式 (function) 」的時候，雖然你會得到 "function" 的結果，讓你以為 function 也是 JavaScript 定義的一種型別，但實際上它仍屬於 Object 的一種。

可以把它想像成是一種可以被呼叫 (be invoked) 的特殊物件 (值)。

宣告函式的方法有好幾種，但不管是什麼方式，通常一個函式會包含三個部分：

* 函式的名稱 (也可能沒有名稱，稍後會提到)&#x20;
* 在括號 ( ) 中的部分，稱為「引數 (arguments) 」，引數與引數之間會用逗號 , 隔開&#x20;
* 在大括號 { } 內的部分，內含需要重複執行的內容，是函式功能的主要區塊。

```javascript
function square(number) {
  return number * number;
}

square(2);        // 4
square(3);        // 9
square(4);        // 16
```

## 定義函式的方式

常見定義函式的方式有這幾種：

* 函式宣告（Function Declaration）&#x20;
* 函式運算式（Function Expressions）&#x20;
* 透過 new Function 關鍵字建立函式

### 函式宣告（Function Declaration）

```javascript
function 名稱([引數]) {
  // 做某事
}

function square(number) {
  return number * number;
}
```

### 函式運算式（Function Expressions）

透過 變數名稱 = function(\[引數]){ ... }; 的方式，將一個函式透過 = 指定給某個變數。

在範例裡 = 後面的 function 是「沒有名字」。通常我們會稱它為「匿名函式」。

也可以命名函式，但是要注意的是，這個名字只在「自己函式的區塊內」有效。

```javascript
// anonymous function
var square = function (number) {
  return number * number;
};

// 也可以命名函式，但只有在函式區塊內有效
var square = function func(number) {
  console.log( typeof func );   // "function"
  return number * number;
};

console.log( typeof func );     // undefined
```

### 透過 new Function 關鍵字建立函式

接使用 Function (注意 F 大寫) 這個關鍵字來建立函式物件。 使用時將引數與函式的內容依序傳入 Function，就可以建立一個函式物件了。

```javascript
// 透過 new 來建立 Function "物件"
var square = new Function('number', 'return number * number');
```

透過 new Function 所建立的函式物件，每次執行時都會進行解析「字串」(如 'return number \* number' ) 的動作，運作效能較差，所以通常實務上也較少會這樣做。

## 全域變數與區域變數

其實在 JavaScript 這門語言中，沒有所謂「全域變數」這種東西。 更準確地說，我們所說的「全域變數」其實指的是「全域物件」(或者叫「頂層物件」) 的屬性。

* 以瀏覽器來說，「全域物件」指的就是 window，在 node 環境中則叫做 global。
* 變數有效範圍 (scope) 的最小切分單位是 function (ES6 的 let 與 const 例外)&#x20;
* 即使是寫在函式內，沒有 var 的變數會變成「全域變數」&#x20;
* 全域變數指的是全域物件 (頂層物件) 的「屬性」
