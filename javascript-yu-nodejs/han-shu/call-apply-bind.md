# call, apply, bind

## 簡介

call、apply、bind 三者都是 JavaScript Function 的內建函式，他們與 this 的關係重大，會需要這三個函數，最大的原因還是因為 this 指向的物件是動態的。除此之外，call & apply 可以作為呼叫 Function 的另一個手段，而 bind 則會回傳一個經過包裹後的 Function 回來。

而其根本差異性是 <mark style="color:red;">call 會直接去執行函式並回傳結果，而 bind 回傳的是一個「被設定好的函式」</mark>，這也意味著 **bind 不只能做到 wrapper 特定 this ，還能去 wrapper 引數**。

## call

`fn.call(this, arg1, arg2..., argn)`

* 第一個引數：輸入的物件會被指定為目標函式中的 this。
* 第二以後的引數：會作為引數傳進目標函式中，如果目標函式中不需要引數則不要傳入即可。

call 是 Function 的內建函式。功能為執行 function與明確指定 this。

```javascript
function add(a, b) {
  return a + b;
}
console.log(add(1, 2));		// 3
console.log(add.call(null, 1, 2));// 3
```

<mark style="color:red;">上列可以很清楚的知道 call 對我們來說唯一的使用情境就在於要明確指定 this 的時候</mark>。

```javascript
var obj = {
    name: 'chenhh'
}

function foo(){
    console.log(this);
}   

// foo中的this指向obj
foo.call(obj);  // {name:"chenhh"}
```

## apply

`fn.apply(this, [arg1, arg2..., argn])`

* 第一個引數：輸入的物件會被指定為目標函式中的 this。
* 第二個引數：必須是陣列，會把陣列中的每個元素作為引數傳進目標函式中，如果目標函式中不需要引數則不要傳入即可。

```javascript
function add(a, b) {
  return a + b;
}
console.log(add(1, 2));		// 3
console.log(add.call(null, 1, 2)); // 3
console.log(add.apply(null, [1, 2])); // 3
console.log(add.apply(null, 1, 2)); 
// Uncaught TypeError: CreateListFromArrayLike called on non-object
```

## bind

`fn.bind(this, arg1, arg2..., argn)`

* 第一個引數：輸入的物件會被指定為目標函式中的 this ( 以硬繫結的方式 )。
* 第二以後的引數：會作為往後傳進目標函式的引數，如果目標函式中不需要引數則不要傳入即可。
* 回傳：回傳包裹後的目標函式。執行這個包裹函式後，可以幾乎確定 this 不會被改變，另外，也可以把先前傳入 bind 的引數 一併帶進目標函式中。

<mark style="color:red;">bind() 能改變 this 指向，但不會呼叫(執行)函數，會 copy 並返回一個新的函數</mark>。

```javascript
function add(a, b) {
  return a + b;
}
add.call(null, 1, 2);			// 3
add.call(null, 1, 4);			// 5
add.apply(null, [1, 2]);		// 3
add.apply(null, [1, 4]);		// 5
var add1 = add.bind(null, 1);
console.log(add1(2));			// 3
console.log(add1(4));			// 5
```

當之後我們執行 add1 的話，bind 的第二個引數1 就會作為 add 函式的第一個引數帶入了，也就是說，之後我們只需要帶入第二個引數給 add1 就可以達成 add(1, ?) 的功能了。

```javascript
// Simple binding
function sum(n1, n2, n3) {
  return n1 + n2 + n3;
}
//而這個「設定」兩字正是 bind 的精髓所在。
// 如果我確定第一個傳入的數肯定是1
const _sum = sum.bind(null, 1);
_sum(2, 3); // 6
```

```javascript
function talking(time, greeting, name) {
  console.log(`[${time}] ${greeting} ${name}!`);
}
// 固定第一個參數
var morning = talking.bind(null, 'Morning');
// 設定time
morning('Hello', 'Dennis'); // [Morning] Hello Dennis!
// 固定前兩個參數
var morning_hello = morning.bind(null, 'Hiiii!');
// 再設定greeting
morning_hello('Jack'); // [Morning] Hiiii! Jack!
```

在開發中，最常使用的應該是 bind()，因為很多情況下我們只是想改變 this，不想同時執行函數。例如現在有一個按鈕，想要在用戶點擊後，禁用此按鈕 3 秒。

```html
<button>按鈕</button>
```

若直接在定時器裡使用匿名 function(){} 形式的 callback，定時器裡的 this 指向的是 window。

```javascript
const btn = document.querySelector('button');
btn.addEventListener('click', eventHandler);

function eventHandler(){
    // this 指向按鈕 btn
    this.disabled = true;
    
    //setTimeout(function(){
        // this 指向 window
    //    this.disabled = false;
    //},3000)
     setTimeout(function(){
        this.disabled = false;
    }.bind(this),3000)  // this 改指向按鈕 btn
}
```

當然，也可以直接將定時器裡的 callback function 改成箭頭函式(arrow function)的形式來解決。

```javascript
const btn = document.querySelector('button');
btn.addEventListener('click', eventHandler);

function eventHandler(){
    this.disabled = true;
    
    // 改為箭頭函式
    setTimeout(()=>{
        // this 指向 btn
        this.disabled = false;
    },3000)
}
```
