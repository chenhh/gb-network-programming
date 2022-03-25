# 函數

## 簡介

函數是JavaScript應用程式的基礎。 它幫助你實現抽象層，模擬類，資訊隱藏和模組。 在TypeScript裡，雖然已經支援類，命名空間和模組，但函數仍然是主要的定義的地方。 TypeScript為JavaScript函數新增了額外的功能，讓我們可以更容易地使用。

## 定義函數&#x20;

和JavaScript一樣，TypeScript函數可以創建有名字的函數和匿名函數。 你可以隨意選擇適合應用程式的方式，不論是定義一系列API函數還是只使用一次的函數。

```javascript
// Named function
function add(x, y) {
    return x + y;
}

// Anonymous function
let myAdd = function(x, y) { return x + y; };

// arrow function
let arrAdd = (x,y) => x+y;
```

<mark style="color:red;">在JavaScript裡，函數可以使用函數體外部的變量</mark>。 當函數這麼做時，我們說它‘捕獲’(capture)了這些變量。 至於為什麼可以這樣做以及其中的利弊超出了本文的范圍，但是深刻理解這個機制對學習JavaScript和TypeScript會很有幫助。

```javascript
let z = 100;

function addToZ(x, y) {
    return x + y + z;
}
```

## 函數類型

我們可以給每個參數新增類型之後再為函數本身新增返回值類型。 TypeScript能夠根據返回語句自動推斷出返回值類型，因此我們通常省略它。

```typescript
function add(x: number, y: number): number {
    return x + y;
}

let myAdd = function(x: number, y: number): number { return x + y; };
```
