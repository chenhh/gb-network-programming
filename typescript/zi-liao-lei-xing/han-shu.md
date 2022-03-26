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

### 推斷類型

嘗試上面例子的時候，就算僅在等式的一側帶有類型，TypeScript編譯器仍可正確識別類型，這叫做“按上下文歸類”，是類型推論的一種。 它幫助我們更好地為程式指定類型。

```typescript
// myAdd 可自動推斷類型
let myAdd = function(x: number, y: number): number { return x + y; };

// The parameters `x` and `y` have the type number
let myAdd: (baseValue: number, increment: number) => number =
    function(x, y) { return x + y; };
```

### 可選參數和預設參數

TypeScript裡的每個函數參數都是必須的。 這不是指不能傳遞null或undefined作為參數，而是說編譯器檢查用戶是否為每個參數都傳入了值。 編譯器還會假設只有這些參數會被傳遞進函數。 <mark style="color:blue;">簡短地說，傳遞給一個函數的參數個數必須與函數期望的參數個數一致</mark>。

```typescript
// 傳給函數的參數的個數必須與定義一致
function buildName(firstName: string, lastName: string) {
    return firstName + " " + lastName;
}

// let result1 = buildName("Bob");                  // error, too few parameters
// let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");         // ah, just right
```

<mark style="color:blue;">JavaScript裡，每個參數都是可選的，可傳可不傳。 沒傳參的時候，它的值就是undefined</mark>。 在TypeScript裡我們可以在參數名旁使用?實現可選參數的功能。 比如，我們想讓last name是可選的，可選參數必須跟在必須參數後面。 如果上例我們想讓first name是可選的，那麼就必須調整它們的位置，把first name放在後面。

```typescript
// lastName是可選的參數，不傳參時為undefined
function buildName(firstName: string, lastName?: string) {
    if (lastName)
        return firstName + " " + lastName;
    else
        return firstName;
}

let result1 = buildName("Bob");  // works correctly now
// let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");  // ah, just right
```

<mark style="color:blue;">在TypeScript裡，我們也可以為參數提供一個預設值當用戶沒有傳遞這個參數或傳遞的值是undefined時。 它們叫做有預設初始化值的參數</mark>。 讓我們修改上例，把last name的默認值設置為"Smith"。

```typescript
// lastName的預設參數是Smith
function buildName(firstName: string, lastName = "Smith") {
    return firstName + " " + lastName;
}

let result1 = buildName("Bob");                  // works correctly now, returns "Bob Smith"
let result2 = buildName("Bob", undefined);       // still works, also returns "Bob Smith"
// let result3 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result4 = buildName("Bob", "Adams");         // ah, just right
```

在所有必須參數後面的帶預設初始化的參數都是可選的，與可選參數一樣，在調用函數的時候可以省略。 也就是說可選參數與末尾的預設參數共享參數類型。

```typescript
function buildName(firstName: string, lastName?: string) {
    // ...
}
function buildName(firstName: string, lastName = "Smith") {
    // ...
}
```

共享同樣的類型`(firstName: string, lastName?: string) => string`。 在函數類型中，預設參數的默認值不會顯示，而只會顯示它是一個可選參數。

與普通可選參數不同的是，帶默認值的參數不需要放在必須參數的後面。 如果帶默認值的參數出現在必須參數前面，用戶必須明確的傳入undefined值來獲得默認值。

```typescript
function buildName(firstName = "Will", lastName: string) {
    return firstName + " " + lastName;
}

//let result1 = buildName("Bob");                  // error, too few parameters
// let result2 = buildName("Bob", "Adams", "Sr.");  // error, too many parameters
let result3 = buildName("Bob", "Adams");         // okay and returns "Bob Adams"
let result4 = buildName(undefined, "Adams");     // okay and returns "Will Adams"
```

### 剩餘參數(不定數量參數)

必要參數，預設默認參數和可選參數有個共同點：它們表示某一個參數。 有時，你想同時操作多個參數，或者你並不知道會有多少參數傳遞進來。 在JavaScript裡，你可以使用arguments來訪問所有傳入的參數。

在TypeScript裡，你可以把所有參數收集到一個變量裡：

```typescript
function buildName(firstName: string, ...restOfName: string[]) {
  return firstName + " " + restOfName.join(" ");
}

let employeeName = buildName("Joseph", "Samuel", "Lucas", "MacKinzie");
//完整的函數簽名
let buildNameFun: (fname: string, ...rest: string[]) => string = buildName;
```

剩餘參數會被當做個數不限的可選參數。 可以一個都沒有，同樣也可以有任意個。 編譯器創建參數數組，名字是你在省略號`（...）`後面給定的名字，你可以在函數體內使用這個數組。
