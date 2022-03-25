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

### 完整函數類型

下面讓我們寫出函數的完整類型。

```typescript
// 只要參數類型是匹配的，那麼就認為它是有效的函數類型，而不在乎參數名是否正確。
let myAdd: (baseValue: number, increment: number) => number =
    function(x: number, y: number): number { return x + y; };
```

函數類型包含兩部分：參數類型和返回值類型。 當寫出完整函數類型的時候，這兩部分都是需要的。 我們以參數列表的形式寫出參數類型，為每個參數指定一個名字和類型。 這個名字只是為了增加可讀性。

第二部分是返回值類型。 <mark style="color:blue;">對於返回值，我們在函數和返回值類型之前使用(=>)符號，使之清晰明了</mark>。 如之前提到的，返回值類型是函數類型的必要部分，如果函數沒有返回任何值，你也必須指定返回值類型為void而不能留空。

函數的類型只是由參數類型和返回值組成的。 函數中使用的捕獲變量不會體現在類型裡。 實際上，這些變量是函數的隱藏狀態並不是組成API的一部分。
