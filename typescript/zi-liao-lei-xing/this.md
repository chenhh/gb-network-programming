# this

## 簡介

由於TypeScript是JavaScript的超集，TypeScript程式員也需要弄清this工作機制並且當有bug的時候能夠找出錯誤所在。 幸運的是，TypeScript能通知你錯誤地使用了this的地方。

## this和箭頭函數

JavaScript裡，<mark style="color:blue;">this的值在函數被調用的時候才會指定。</mark> 這是個既強大又靈活的特點，但是你需要花點時間弄清楚函數調用的上下文是什麼。 但眾所周知，這不是一件很簡單的事，尤其是在返回一個函數或將函數當做參數傳遞的時候。

<mark style="color:red;">箭頭函數能儲存函數創建時的this值，而不是調用時的值</mark>。

```javascript
// 本例中, this指向全域的window
let deck = {
    suits: ["hearts", "spades", "clubs", "diamonds"],
    cards: Array(52),
    createCardPicker: function() {
        return function() {
            let pickedCard = Math.floor(Math.random() * 52);
            let pickedSuit = Math.floor(pickedCard / 13);
// error here TypeError: Cannot read properties of undefined (reading '0')
            return {suit: this.suits[pickedSuit], card: pickedCard % 13};
        }
    }
}

let cardPicker = deck.createCardPicker();
let pickedCard = cardPicker();

alert("card: " + pickedCard.card + " of " + pickedCard.suit);
```

`createCardPicker`是個函數，並且它又返回了一個函數。 如果我們嘗試運行這個程式，會發現它並沒有彈出對話框而是報錯了。 因為`createCardPicker`返回的函數裡的`this`被設置成了`window`而不是`deck`物件。 因為我們只是獨立地調用了`cardPicker()`。 頂級的非方法式調用會將`this`視為`window`。 （注意：在嚴格模式下，`this`為`undefined`而不是`window`）。

## 參考資料

* [Understanding JavaScript Function Invocation and "this"](https://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)
