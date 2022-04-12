---
description: Event-driven
---

# 事件驅動

## 簡介

JavaScript 是一個事件驅動 (Event-driven) 的程式語言，當瀏覽器載入網頁開始讀取後，雖然馬上會讀取 JavaScript 事件相關的程式碼，但是必須等到「事件」被觸發(如使用者點選、按下鍵盤等)後，才會再進行對應程式的執行。

以我們很常見的網頁對話方塊 UI 來說，當使用者「按下了按鈕」之後，才會啟動對話方塊的顯示。

當使用者點選了按鈕，才會啟動對話方塊的顯示，那麼「點選按鈕」這件事，就被稱作「事件」(Event)，而負責處理事件的程式通常被稱為「事件處理者」(Event Handler)，也就是「啟動對話方塊的顯示」這個動作。

## DOM Event

DOM Event 定義很多種事件型態，讓你可以用 JavaScript 來監聽 (listen) 和處理 (event handling) 這些事件。

| 事件名稱         | 觸發條件                |
| ------------ | ------------------- |
| blur         | 物件失去焦點時             |
| change       | 物件內容改變時             |
| click        | 滑鼠點選物件時             |
| dblclick     | 滑鼠連點兩下物件時           |
| error        | 當圖片或檔案下載產生錯誤時       |
| focus        | 當物件被點選或取得焦點時        |
| keydown      | 按下鍵盤按鍵時             |
| keypress     | 按下並放開鍵盤按鍵後          |
| keyup        | 按下並發開鍵盤按鍵時          |
| load         | 網頁或圖片完成下載時          |
| mousedown    | 按下滑鼠按鍵時             |
| mousemove    | 介於over跟out間的滑鼠移動行為  |
| mouseout     | 滑鼠離開某物件範圍時          |
| mouseover    | 滑鼠進行一個元素(包含其子元素)四週時 |
| mouseup      | 放開滑鼠按鍵時             |
| resize       | 當視窗或框架大小被改變時        |
| scroll       | 當捲軸被拉動時             |
| select       | 當文字被選取時             |
| submit       | 當按下送出按鈕時            |
| beforeunload | 當使用者關閉(或離開)網頁之前     |
| unload       | 當使用者關閉(或離開)網頁之後     |

## DOM Level 0 - HTML Inline Attribute

你可以在 HTML 的事件相關屬性上繫結事件處理函式，屬性的名稱是「on + 事件名稱」，屬性值則是任何的 JavaScript。

## DOM Level 0 - DOM Object Property

DOM 元素 API 也有對應的屬性，可以用來繫結事件處理函式。



## DOM Level 2 - Element.addEventListener(eventType, listener)

addEventListener 方法可以用來繫結元素的事件處理函式，第一個引數 eventType 是事件名稱(string)，第二個引數 listener 是事件處理函數(callback function)。

## DOM Level 2 - Element.removeEventListener(eventType, listener)

removeEventListener 原來取消透過 addEventListener 繫結的事件處理函式，第一個引數 eventType 是事件名稱，第二個引數 listener 是先前繫結的事件處理函式。

## Legacy IE - attachEvent(eventType, listener), detachEvent(eventType, listener)

在 IE9 以下可以用 attachEvent 和 detachEvent 這兩個 IE 專有 (proprietary) 的方法來取代 addEventListener 和 removeEventListener。

## 事件流程 Event Flow

<mark style="color:red;">事件流程 (Event Flow) 指的就是「網頁元素接收事件的順序」</mark>。可以分成兩種機制：

* 事件捕獲 (Event Capturing) (由上而下，從根節點到目標節點)
* 事件冒泡 (Event Bubbling) (由下而上，從目標節點到根節點)

當 DOM 事件發生時，事件會先由外到內 (capturing phase)、再由內到外 (bubbling phase) 的順序來傳播。

## Event Object

當監聽的事件發生時，瀏覽器會去執行我們透過 addEventListener() 註冊的 Event Handler (EventListener) ，也就是我們所指定的函數。&#x20;

這個時候，EventListener 會去建立一個「事件物件」 (Event Object)，裡面包含了所有與這個事件有關的屬性，並且以「引數」的形式傳給我們的 Event Handler。

```javascript
<button id="btn">Click</button>
var btn = document.getElementById('btn');

// 引數 e 就是上面說的事件物件 (Event Object)
// 因為是引數，當然也可以自己定義名稱
btn.addEventListener('click', function(e){
  console.log(e);
}, false);
```

### Event Object

Event Object 有幾個常用的屬性 (property)：

* <mark style="color:red;">type</mark> 返回事件型別，例如 "click"。
* <mark style="color:red;">target</mark>：指向觸發事件的 DOM element。
* <mark style="color:red;">currentTarget</mark>：在 event bubbling 階段中，指向目前執行的事件處理函式是繫結在哪個 DOM element 上。
* <mark style="color:red;">timeStamp：</mark>事件發生時的時間 timestamp (單位是 milliseconds 毫秒)。
* <mark style="color:red;">eventPhase</mark>：返回為一個數字，表示事件處於目前所處的傳播狀態 (event flow)，有這些值：&#x20;
  * 0: None。
  * 1: capturing phase。&#x20;
  * 2: target phase 。
  * 3: bubbling phase。

### MouseEvent

當 MouseEvent (滑鼠事件) 發生時，Event Object 有幾個常用的屬性：



### KeyboardEvent

當 KeyboardEvent (鍵盤事件) 發生時，Event Object 有幾個常用的屬性：



### event.stopPropagation()

那我怎麼不要讓事件傳播下去？答案就是使用 event object 的 stopPropagation 方法。



### event.preventDefault()

event object 有一個 preventDefault 方法用來取消瀏覽器預設的行為。

瀏覽器預設行為舉例來說像是：

* 點選一個超連結後，會載入新的頁面&#x20;
* 在表單輸入欄位中輸入 enter 會送出表單

## 各種事件繫結的差異

在 HTML 標籤內直接寫 JS（舊式寫法，不推薦） 容易被駭客植入惡意程式碼 。

```html
<input onclick="alert('say Hello')" type="button" 
       class="btn" value="點選">
```

on-event 處理器：主要的缺點為一個事件只能繫結一個函式。如果用此方法在同一個事件上繫結兩個不同函式，會造成兩個函式都無法如預期般正確運作。

事件監聽（新寫法，推薦）：addEventListener 跟 on-event 處理器的差別在於，前者可以在一個 DOM 上執行兩個以上的函式；如果是在 DOM 上使用後者，就只能繫結一個函式。

```javascript
let el = document.querySelector('.btn');
el.addEventListener('click',function(e){
  alert('Hello');
},false)
// addEventListener的第三個參數
// false（事件氣泡，Event Bubbling）- 從指定元素往外層找
// true（事件捕捉，Event Capuring）- 從最外面找到指定元素
// 如果在監聽程式碼裡不寫第三個引數，則預設值是 false。
```

## 常見的事件處理範例 (Examples)

### onclick event

```javascript
// 當使用者用滑鼠點選螢幕 (或用手點選觸控螢幕) 時
document.body.addEventListener('click', function(event) {

    // 把字型改成黃色
    event.target.style.color = 'yellow';
});
```

### onkeydown event

```javascript
// 當使用者在網頁中按下鍵盤按鍵時
document.onkeydown = function(event) {

    if (event.keyCode === 89 && event.ctrlKey) {
        alert('你同時按下 "control + y"'); 
  
    } else if (event.which === 90 && event.ctrlKey ){
        alert('你同時按下 "control + z"'); 
    }
};
```

### onbeforeunload event

```javascript
// 當使用者要離開或關閉目前頁面時
window.onbeforeunload = function(event) {

    // 返回要顯示給使用者看的提醒文字
    return '你確定要離開本頁面嗎？';
};
```

## 參考資料

* [\[wikipedia\] 非侵入式JavaScript](https://zh.wikipedia.org/wiki/%E9%9D%9E%E4%BE%B5%E5%85%A5%E5%BC%8FJavaScript)
* [\[MDN\] event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
* [\[W3\] Events-interface](https://www.w3.org/TR/DOM-Level-2-Events/events.html#Events-interface)
