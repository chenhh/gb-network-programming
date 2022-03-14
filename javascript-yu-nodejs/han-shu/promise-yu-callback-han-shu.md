# Promise與callback函數

## 回調函數(callback function)

一般的函數是由使用者自行決定叫呼叫，而回調函數是由使用者指定函數後，等待特定事件發生後，才由該事件觸發執行，因此需要將回調函數當做一個參數傳遞。

```javascript
function callback(){
     console.log('hello!')
}

const el = document.getElementById('myButton')
// 由click事件觸發callback function
el.addEventListener('click', callback, false)
```

```javascript
// doSomething()回傳成功執行引數1(匿名函式)，
// 回傳失敗則執行引數2(failureCallback)。
doSomething(function(result){console.log(result);}, 
            failureCallback);
```

但當我們在函式裡執行更多行為時，被巢狀的callback會越來越多層，然後程式碼會變成以下的結構，這種 Callback被一層層巢狀，導致程式碼難以閱讀和維護的情況，就被稱作 Callback Hell。

```javascript
function failureCallback() {
  console.log("failed");
}

doSomething(function(result) {
  doSecondThing(result, function(newResult) {
    doThirdThing(newResult, function(finalResult) {
      console.log('Final result: ' + finalResult);
    }, failureCallback);
  }, failureCallback);
}, failureCallback);
```

## callback hell

```javascript
doA(function() {
  doB();
  doC(function() {
    doD();
  });
  doE();
});

doF();
// 執行順序為doA() -> doF() -> doB() -> doC() -> doE() -> doD()
```

```javascript
step1(x, function(value1){
  //do something...
  step2(y, function(value2){
    //do something...
    step3(z, function(value3){
        //do something...
    })
  })
})
```

所以執行的步驟是像下面這樣才對：

* step1執行後，"value1"已經有值，移往function(value1)
* 執行 function(value1)執行到step2，step2執行到最後，"value2"已經有值，移往function(value2)執行&#x20;
* function(value2)執行到step3，step3執行到最後，"value3"已經有值，移往function(value3)執行&#x20;
* function(value3)執行完成

執行順序是：step1 -> function(value1) -> step2 -> function(value2) -> step3 -> function(value3)

那為何為不使用直接風格？而一定要用這麼不易理解的程式流程結構。<mark style="color:red;">因為有些I/O或事件類的函式，用直接風格會造成阻塞，所以要寫成非同步的回調函數</mark>。在JavaScript中要"阻塞"太容易了，它是單執行緖執行的設計，一個比較長時間的程式執行就會造成阻塞。

{% embed url="https://eyesofkids.gitbooks.io/javascript-start-from-es6/content/part4/callback.html" %}

## Promise

而為了避免產生callback Hell，現在多以使用promise的方式取代。 <mark style="color:red;">Promise代表在進行非同步請求時，成功取得的資料或失敗的物件</mark>。Promise 本身是用來改善 JavaScript 非同步的語法結構。

JavaScript 是屬於同步的程式語言，因此一次僅能做一件事情，但遇到非同步的事件時(如ajax)，就會將非同步的事件移動到程式碼的最後方，等到所有的原始碼執行完以後才會執行非同步的事件。

```javascript
/*
在 console 中依序的會出現的順序為：
  開始
  程式碼結束
  非同步事件 <- 最後執行
*/
console.log('開始');

setTimeout(() => {
  console.log('非同步事件');
}, 0);

console.log('程式碼結束');
```

### Promise 的結構

Promise 是用來優化非同步的語法，而 Async、Await 可以基於 Promise 讓非同步的語法的結構類似於 “同步語言”，更易讀且好管理。

Promise 本身是一個建構函式，函式也是屬於物件的一種，因此可以附加其它屬性方法在上，透過 console 的結果可以看到 Promise 可以直接使用 all、race、resolve、reject 的方法。

Promise 建構函式 new 出的物件，則可以使用其中的原型方法（在 prototype 內），其中就包含 then、catch、finally，這些方法則必須在新產生的物件下才能呼叫。

```javascript
// callback, resolve, reject都是function
const p = new Promise(callback<resolve, reject>)

p.then(<resolveHandler>, [<rejectHandler>])  // 處理正確回傳
  .then(<resolveHandler2>, <rejectHandler2>) // 處理正確回傳2
  .catch(<rejectHandler>)    // 錯誤處理
  .finally(<finallyHandler>) // 收尾(正常或錯誤都會執行)
```

Promise 建構函式建立同時，必須傳入一個函式作為引數（executor function），此函式的引數包含 resolve, reject，這兩個方法分別代表成功與失敗的回傳結果，特別注意這兩個僅能回傳其中之一，回傳後表示此 Promise 事件結束。

```javascript
// resolve 及 reject 的名稱可以自定義，但在開發上大多數開發者習慣維持此名稱。
new Promise(function(resolve, reject) { 
	resolve(); // 正確完成的回傳方法
	reject();  // 失敗的回傳方法
});
```

new是指產生一個新物件，所以這裡會產生一個Promise的空物件，Promise 裡面包含 resolve 或 reject 兩種 callback function:

* resolve 為成功取得的資料時，回傳資料。
* reject 則會在失敗時回傳 error object。&#x20;
* 每當傳入這兩個引數，executor函式就會直接執行，並在成功時執行resolve，在失敗時執行reject。

而promise很常被搭配使用兩個function:

* `.then()` 接住 resolve 的結果。&#x20;
* `.catch()` 接住 reject 的結果。

promise的function是可以被串接起來的，被稱為 Promise Chain。<mark style="color:red;">這樣的好處是，不管接續執行多少工作(.then())，最後都只要指定一次失敗的情況(.catch())</mark>。 而不必像早期的方式(Callback Hell的範例)，傳入許多次failureCallback。

```javascript
let example = new Promise((resolve, reject) => {
	resolve({ string : "Hello" });
});

example
  .then((data)=>{console.log(data);})
  .then(() => {console.log("HI");})
  .catch((error) => {console.log(error);});  
  
  // output: { string : "Hello" } ; "HI"
```

### Promise 的結構

Promise 的關鍵在處理非同步的事件，而非同步的過程中也包含著不同的進度狀態，在 Promise 的執行過程中，可以看到以下狀態。

* pending：事件已經執行中，尚未取得結果
* resolved：事件已經執行完畢且成功操作，回傳 resolve 的結果（該承諾已經被實現 fulfilled）&#x20;
* rejected：事件已經執行完畢但操作失敗，回傳 rejected 的結果

![Promise狀態](../../.gitbook/assets/promises.png)

進入 fulfilled 或 rejected 就算完成後不會再改變，Promise 中會使用 resolve 或 reject 回傳結果，並在呼叫時使用 then 或 catch 取得值。

如果要判斷 Promise 是否完成，可依據 Promise 事件中的 resolve 及 reject 是否有被呼叫，以下範例來說在沒有呼叫兩個方法時，Promise 的結果則會停留在 pending。

```javascript
function promise() {
  return new Promise((resolve, reject) => {});
}

console.dir(promise());
/*
 在 Promise 的執行函式中，可以看到以下兩個屬性：
  [[PromiseStatus]]: "pending" -> 表示目前的進度狀態
  [[PromiseValue]]: undefined -> 表示 resolve 或 reject 回傳的值
*/
```

## Promise簡單範例

```javascript
function promise() {
  // 函式陳述式建立以後，直接透過return new Promise 回傳並建立一個 Promise 物件
  // 內部為執行函式且帶上 resolve, reject 的引數
  return new Promise((resolve, reject) => {
    // 隨機取得 0 or 1
    const num = Math.random() > 0.5 ? 1 : 0;
    // 1 則執行 resolve，否則執行 reject
    if (num) { 
      resolve('成功');
    }
    reject('失敗')
  });
}

// 執行程式

promise()
  .then(success => {
    console.log(success);
  })  // 失敗的行為一律交給了 catch
  .catch(fail => {
    console.log(fail);
  });
```

在 `.then(onFulfilled, onRejected)`中可帶入兩個回調函數，兩者分別又可以帶入各自的引數：

* onFulfilled：執行成功的函數，所帶入參數列示 Promise 函式中 resolve 所帶入的值。&#x20;
* onRejected：執行失敗的函式，帶入參數列示 Promise 函式中 reject 所帶入的值。
* 在大部分情況下，開發者習慣僅使用 .then() 來取得成功的結果，失敗的部分交由 catch(onRejected) 來處理，這兩種寫法差異很小。

## Promise鏈簡單範例

當我們要進行確保 Promise 任務結束後在進行下一個任務時，就可以使用 return 的方式進入下一個 then，此 return 也有以下特點：

* 方法不限於 promise 函式，任何表示式（expression）都可進行回傳
* 如果是 promise 函式，則會繼續遵循 then 及 catch 的運作
* 如果不是 promise 函式，在下一個 then 則可以取得結果

```javascript
// 改成傳入 0 則會呼叫 reject，其它數值則會呼叫 resolve。
function promise(num) {
  return new Promise((resolve, reject) => {
    num ? resolve(`${num}, 成功`) : reject('失敗');
  });
}

// 1, 成功
// 2, 成功
// 失敗
promise(1)
  .then(success => {
    console.log(success);
    return promise(2);
  })
  .then(success => {
    console.log(success);
    return promise(0); // 這個階段會進入 catch
  })
  .then(success => {   // 由於上一個階段結果是 reject，所以此段不執行
    console.log(success);
    return promise(3);
  })
  .catch(fail => {
    console.log(fail);
  })
```

## Then VS Catch 的失敗回調差異

then、catch 都可以透過進行連結，上述也有提到 then 同時也能接收失敗的結果，在此用圖示表示兩者在執行上不同的結果。

不使用 then 接收失敗：無論在哪一個階段遇到 reject 時，接下來會直接跳到 catch，在其後的 then 都不會執行。另外提一下：catch 依然可以使用 return 繼續串接（實戰中很少這樣寫）。

![cache then](../../.gitbook/assets/promise\_cache-min.png)

使用 then 接收失敗：then 中的兩個函式必定執行其中一個（onFulfilled, onRejected），可以用此方式確保所有的連結都能夠被執行。

![then reject](../../.gitbook/assets/then\_reject-min.png)

## finally

最後方可以使用 finally 來確認工作結束，finally 不帶有任何引數。

```javascript
promise(1)
  .then(success => {
    console.log(success);
  }).finally(() => {
    console.log('done');
  })
```

## Promise.all

all -> 多個 Promise 行為同時執行，全部完成後統一回傳。

透過陣列的形式傳入多個 promise 函式，在全部執行完成後回傳陣列結果，陣列的結果順序與一開始傳入的一致。這個方法很適合用在多支 API 要一起執行，並確保全部完成後才進行其他工作時。

```javascript
function promise(num, time = 500) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      num ? resolve(`${num}, 成功`) : reject('失敗');
    }, time);
  });
}

Promise.all([promise(1), promise(2), promise(3, 3000)])
  .then(res => {
    console.log(res);
  });
```

## Promise.race

透過陣列的形式傳入多個 promise 函式，在全部執行完成後回傳單一結果，結果為第一個執行完成的。這個方法可以用在站點不穩定，同時傳送多支同行為 API 確保可行性使用，但實作中使用率並不高。

```javascript
Promise.race([promise(1), promise(2), promise(3, 3000)]).then(res => {
  console.log(res);
});
```

## async & await

async function 宣告被定義為一個回傳 AsyncFunction 物件的非同步函式 。

```javascript
//回傳值: AsyncFunction 物件，代表著一個非同步函式，該函式會執行該函式內的程式碼。
async function name([param[, param[, ... param]]]) {
   statements
}
```

async & await是一個基於promise的語法糖。運作原理和promise一模一樣，主要包含兩個部分:

* async : async function 宣告一個非同步函式，可以告訴function在最後回傳一個promise。&#x20;
* await : await必須放在任何基於promise的函式之前，等到獲得resolve的資料後，再執行後續動作。 （await放在async function裡才有作用。）

```javascript
// original version
function greeting() { 
  return new Promise( (resolve,reject) => {
    resolve("Hello"); 
});
}

greeting()
  .then((value) => console.log(value));
// output: "Hello"
```

修改後：

```javascript
async function greeting() { return "Hello" };

greeting()
  .then((value) => console.log(value));

// output: "Hello"
```

## 參考資料

* [JavaScript Promises：簡介](https://web.dev/promises/)
