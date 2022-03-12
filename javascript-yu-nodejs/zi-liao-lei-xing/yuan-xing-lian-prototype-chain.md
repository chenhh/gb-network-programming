# 原型鏈(prototype chain)

## 簡介

JavaScript 不是物件導向的程式語言，沒有實作 class 的關鍵字（ES6 的 class 也只是語法糖而已）。可是儘管沒有 class，卻還是可以設計出一個類似的機制來達成近似功能。

JavaScript 的物件即透過<mark style="color:red;">原型 (Prototype) 機制相互繼承功能</mark>，且與典型的物件導向 (OO) 程式語言相較，其運作方式有所差異。各個物件均具備 1 組原型物件作為範本物件，用以繼承函式與屬性。物件的原型物件可能也具備原型物件，並繼承了其上的函式與屬性。這就是我們所謂的「原型鍊 (Prototype chain)」。

## 函數 - 原型的起手式

所有JavaScript中的函數都有一個內建的prototype屬性，指向一個特殊的prototype物件，prototype物件中也有一個contructor屬性，指向原來的函數，互相指來指去會讓你覺得有點怪異，但設計就是如此。

```javascript
function Player() { }

console.log(Player)
console.log(Player.prototype)
console.log(Player.prototype.constructor)
console.log(Player.prototype.constructor === Player) //true
```

## 參考資料

* [Javascript繼承機制的設計思想](https://www.ruanyifeng.com/blog/2011/06/designing\_ideas\_of\_inheritance\_mechanism\_in\_javascript.html)
* [從設計初衷解釋 JavaScript 原型鏈](https://www.jianshu.com/p/a97863b59ef7)
