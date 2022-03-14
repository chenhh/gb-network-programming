# 函數

## 函數是物件的一種

除了基本型別以外的都是物件。

當我們透過 typeof 去檢查一個「函數 (function) 」的時候，雖然你會得到 "function" 的結果，讓你以為 function 也是 JavaScript 定義的一種型別，但實際上它仍屬於 Object 的一種。

可以把它想像成是一種可以被呼叫 (be invoked) 的特殊物件 (值)。

宣告函數的方法有好幾種，但不管是什麼方式，通常一個函數會包含三個部分：

* 函數的名稱 (也可能沒有名稱，稍後會提到)&#x20;
* 在括號 ( ) 中的部分，稱為「引數 (arguments) 」，引數與引數之間會用逗號 , 隔開&#x20;
* 在大括號 { } 內的部分，內含需要重複執行的內容，是函數功能的主要區塊。

```javascript
function square(number) {
  return number * number;
}

square(2);        // 4
square(3);        // 9
square(4);        // 16
```

## 定義函數的方式

常見定義函數的方式有這幾種：

* 函數宣告（Function Declaration）&#x20;
* 函數運算式（Function Expressions）&#x20;
* 透過 new Function 關鍵字建立函數

### 函數宣告（Function Declaration）

```javascript
function 名稱([引數]) {
  // 做某事
}

function square(number) {
  return number * number;
}
```

### 函數運算式（Function Expressions）

透過 變數名稱 = function(\[引數]){ ... }; 的方式，將一個函數式透過 = 指定給某個變數。

在範例裡 = 後面的 function 是「沒有名字」。通常我們會稱它為「匿名函數」。

也可以命名函數，但是要注意的是，這個名字只在「自己函數的區塊內」有效。

```javascript
// anonymous function
var square = function (number) {
  return number * number;
};

// 也可以命名函數，但只有在函數區塊內有效
var square = function func(number) {
  console.log( typeof func );   // "function"
  return number * number;
};

console.log( typeof func );     // undefined
```

### 透過 new Function 關鍵字建立函數

接使用 Function (注意 F 大寫) 這個關鍵字來建立函數物件。 使用時將引數與函數的內容依序傳入 Function，就可以建立一個函數物件了。

```javascript
// 透過 new 來建立 Function "物件"
var square = new Function('number', 'return number * number');
```

透過 new Function 所建立的函數物件，每次執行時都會進行解析「字串」(如 'return number \* number' ) 的動作，運作效能較差，所以通常實務上也較少會這樣做。

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

* 傳統函數：依呼叫的方法而定&#x20;
* 箭頭函數：繫結到其定義時所在的物件 (這個詞看似簡單，但又充滿了陷阱!?)

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
    // 注意，如果使用箭頭函數，this 依然指向 window
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

繫結到其定義時所在的物件，我們要瞭解**一般函數在建立時是在 window 下，所以在 window 下使用箭頭函數自然會指向 window**，要確實將箭頭函數宣告在物件內部，這樣 this 才會指向該物件。

* func() 是最外層的函數，他對於內層的箭頭不會有影響。&#x20;
* func2() 是包覆在內層的函數，但由於箭頭函數不是在物件內，所以沒有影響。&#x20;
* func3() 是呼叫在物件內的函數，因此箭頭函數會是使用它所在的物件。

```javascript
var func = function () {
  var func2 = function () {
    setTimeout(() => {
      console.log(this); 
    }, 10);
  };
  // 這裡才算真正的建立一個物件
  // 因此要在此物件下的箭頭函數才會以此作為基準
  var func3 = {
    func: func2,
    var4: 4
  }
  func2(); // this = window
  func3.func(); // func3 Object
}
func(); 
// 就算在這裡新增一個 function，也不會影響到內層的箭頭函數
```

### 縮寫的函數為一般函數,this指向呼叫的物件

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
func.call(family); // 箭頭函數的情況，this 依然是 window
func2.call(family); // 一般函示 this 則是傳入的物件
```

### 不能用在建構式

由於 this 的是在物件下建立，所以箭頭函數不能像 function 一樣作為建構式的函數，如果嘗試使用此方法則會出現錯誤 (... is not a constructor)。

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

一樣是 this 的問題，如果原型上新增一個箭頭函數，並嘗試使用 this 的話會指向全域。

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

##
