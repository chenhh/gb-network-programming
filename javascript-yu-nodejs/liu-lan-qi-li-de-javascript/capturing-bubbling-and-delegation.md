# capturing, bubbling and delegation

![先capturing再bubbling](../../.gitbook/assets/event\_flow-min.png)

## 捕獲與冒泡

* <mark style="color:red;">捕獲(capturing)</mark>：事件發生在某個DOM元素上的時候，會從他的最上層parent開始觸發capturing handler，再來是倒數第二上層的ancestor的capturing handler，以此類推，直到觸發事件的DOM元素本身的capturing handler。
* <mark style="color:red;">冒泡(Bubbling)</mark>：指的是當某個事件發生在某個DOM元素上（如：點選），這個事件會觸發DOM 元素的event handler，接下來會再觸發他的parent的event handler，以及parent的parent的event handler…直到最上層。

為什麼會有「傳遞順序」這一詞呢？假設你有一個ul元素，底下有很多li，代表不同的 item。當你點選任何一個li的時候，其實你也點選了ul，因為ul把所有的li都包住了。假如我在兩個元素上面都加了eventListener，哪一個會先執行？這時候呢，知道事件的執行順序就很重要。

## 簡單範例

```html
<!DOCTYPE html>
<html>
<//HTML:
<body>
    <div>div
        <ul>ul
            <li>li</li>
        </ul>
    </div>
</body>
</html>
```

```javascript
let div = document.querySelector('div');
let ul = document.querySelector('ul');
let li = document.querySelector('li');
let divFunc = function() {
    alert('div');
}
let ulFunc = function() {
    alert('ul');
}
let liFunc = function() {
    alert('li');
}
li.addEventListener('click', liFunc)
div.addEventListener('click', divFunc)
ul.addEventListener('click', ulFunc)
```

結果：click `li`，在Bubbling Phase會先觸發`li`，再按照`ul` => `div`的順序逐一往上。

當然我們也可以控制事件處理器在何時被觸發，這要用到addEventListener()的第三個引數useCapture。平時預設為false（也就是Event Bubbling），要讓事件處理器在Capture Phase被觸發，將useCapture加上true即可。

```javascript
li.addEventListener('click', liFunc, true)
div.addEventListener('click', divFunc, true)
ul.addEventListener('click', ulFunc, true)
```

結果：clickli，在Capture Phase會先觸發最上層的div，再按照ul => li的順序。

## 事件委派（Event Delegation）

* `event.Target` - 指實際觸發事件的元素&#x20;
* `event.currentTarget` - 指向事件繫結的元素

如果想讓按鈕click後，在主控台印出"Click!"，我們可能會這樣寫：

```javascript
<button>Click me!</button>
document.querySelector('button').addEventListener('click', ()=>{
console.log('click')})
```

但當今天我們有好幾個button要繫結事件處理器，我們可能會這樣寫：

```javascript
<div id="buttons">
<button>Click me!</button>
<button>Click me!</button>
  <!-- buttons... -->
<button>Click me!</button>
</div>

//用for loop遍歷元素、把callback獨立出來
 let callback = function() {
            console.log('click')
        }
        let buttons = document.querySelectorAll('button');
        for (let button of buttons) {
            button.addEventListener('click', callback);
        }
```

這樣是行得通的，但我們每loop一次，就有一個button被繫結事件監聽器。這邊有更好、更有效率的寫法，那是用事件委派（Event Delegation）。

<mark style="color:red;">事件委派的用法很簡單，就是將事件監聽器附加到按鈕的"父級"，並在單擊按鈕時捕獲冒泡事件</mark>。 以我們的例子來說，按鈕的父元素是div，所以我們這樣寫：

```javascript
let buttons = document.querySelector('#buttons')  //步驟1
        buttons.addEventListener('click', (e) => { //步驟2
            if (e.target.nodeName === 'BUTTON') { //步驟3
                console.log('Click!');
            }
        });
```

* 步驟1： 先選取button的父元素（也就是 \<div id="#buttons">
* 步驟2： 記得將事件監聽附加到父元素
* 步驟3： 使用event.target選擇目標元素（e.target會指向），因為這邊未將button設定className，所以使用e.target.nodeName === 'BUTTON'去設立條件。

### this簡化程式碼

```html
<style>
        input {
            padding: 50px;
            margin: 20px;
            font-size: 30px;
        }
    </style>
</head>

<body>

    <input type="button" value="Click">
    <input type="button" value="Click">
    <input type="button" value="Click">
    <input type="button" value="Click">
    <input type="button" value="Click">

    <script src="DOM-this.js"></script>
</body>
```

讓changeBackgroundColor()裡的this指向其他的事件觸發元素。

```javascript
let inputs = document.querySelectorAll('input');

let rgbColor = function() {
    let r = Math.floor(Math.random() * 256);
    let g = Math.floor(Math.random() * 256);
    let b = Math.floor(Math.random() * 256);
    return `rgb(${r}, ${g}, ${b})`;
}


let changeBackgroundColor = function() {
    this.style.backgroundColor = rgbColor();
    this.style.color = rgbColor();
}

for (let input of inputs) {
    input.addEventListener('click', changeBackgroundColor);
}
```
