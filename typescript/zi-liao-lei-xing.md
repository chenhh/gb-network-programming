# 資料類型

## 簡介

JavaScript 的型別分為兩種：原始資料型別（Primitive data types）和物件型別（Object types）。

&#x20;原始資料型別包括：boolean (布林值)、number (數值)、string (字串)、null、undefined 以及 ES6 中的新型別 Symbol。

## Boolean

在 TypeScript 中，boolean 是 JavaScript 中的基本型別，而 Boolean 是 JavaScript 中的建構函式。其他基本型別（除了 null 和 undefined）一樣，不再贅述。

```typescript
let isDone: boolean = false;

// 注意：使用建構函式 Boolean 建立的物件不是布林值
// compile error
// let createdByNewBoolean: boolean = new Boolean(1); 

// 事實上 new Boolean() 返回的是一個 Boolean 物件：
let createdByNewBoolean: Boolean = new Boolean(1);

// 直接呼叫 Boolean 也可以返回一個 boolean 型別
let createdByBoolean: boolean = Boolean(1);
```

## Number

```typescript
let decLiteral: number = 6;
let hexLiteral: number = 0xf00d;
// ES6 中的二進位制表示法
let binaryLiteral: number = 0b1010;
// ES6 中的八進位制表示法
let octalLiteral: number = 0o744;
let notANumber: number = NaN;
let infinityNumber: number = Infinity;
```

編譯結果：其中 0b1010 和 0o744 是 ES6 中的二進位制和八進位制表示法，它們會被編譯為十進位制數字。

```javascript
var decLiteral = 6;
var hexLiteral = 0xf00d;
// ES6 中的二進位制表示法
var binaryLiteral = 10;
// ES6 中的八進位制表示法
var octalLiteral = 484;
var notANumber = NaN;
var infinityNumber = Infinity;
```

## String

```typescript
let myName: string = 'Tom';
let myAge: number = 25;

// 範本字串
let sentence: string = `Hello, my name is ${myName}.
I'll be ${myAge + 1} years old next month.`;
```

編譯結果：

```javascript
var myName = 'Tom';
var myAge = 25;
// 範本字串
var sentence = "Hello, my name is " + myName + ".\nI'll be " + (myAge + 1) + " years old next month.";
```

## 空值(void)

JavaScript 沒有空值（Void）的概念，在 TypeScript 中，可以用 void 表示沒有任何返回值的函式：

```typescript
function alertName(): void {
    alert('My name is Tom');
}

// 編譯後
function alertName() {
    alert('My name is Tom');
}
```

宣告一個 void 型別的變數沒有什麼用，因為你只能將它賦值為 undefined 和 null：

```typescript
let unusable: void = undefined;
```

## Null 和 Undefined

在 TypeScript 中，可以使用 null 和 undefined 來定義這兩個原始資料型別：

```typescript
let u: undefined = undefined;
let n: null = null;
```

與 void 的區別是，<mark style="color:red;">undefined 和 null 是所有型別的子型別</mark>。。也就是說 undefined 型別的變數，可以賦值給 number 型別的變數：

```typescript
// 這樣不會報錯
let num: number = undefined;

// 這樣也不會報錯
let u: undefined;
let num: number = u;

// 而 void 型別的變數不能賦值給 number 型別的變數：
let u: void;
let num: number = u;

// Type 'void' is not assignable to type 'number'.
```

## 任意值 (any)

任意值（Any）用來表示允許賦值為任意型別。如果是一個普通型別，在賦值過程中改變型別是不被允許的。

```typescript
// error, 不可轉型
let myFavoriteNumber: string = 'seven';
myFavoriteNumber = 7;
F
// index.ts(2,1): error TS2322: Type 'number' is not assignable to type 'string'.
```

但如果是 any 型別，則允許被賦值為任意型別。

```typescript
let myFavoriteNumber: any = 'seven';
myFavoriteNumber = 7;
```
