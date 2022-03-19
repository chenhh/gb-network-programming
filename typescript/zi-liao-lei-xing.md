# 資料類型

## 簡介

JavaScript 的型別分為兩種：原始資料型別（Primitive data types）和物件型別（Object types）。

* <mark style="color:blue;">原始資料型別</mark>包括：boolean (布林值)、number (數值)、string (字串)、null、undefined 以及 ES6 中的新型別 Symbol。
* <mark style="color:blue;">物件型別 Object Types</mark>，可再細分成小類別，但這些型別的共同特徵是 從原始型別或物件型別組合出來的複合型態（比如物件裡面的 Key-Value 個別是 string 和 number 型別組合成的）：
  * <mark style="color:blue;">基礎物件型別</mark>：包含 JSON 物件，陣列（Array或T\[]），類別以及類別產出的物件（也就是 Class 以及藉由 Class new 出來的 Instance）&#x20;
  * <mark style="color:blue;">TypeScript 擴充型別</mark>：即 Enum 與 Tuple，內建在 TypeScript 函式型別。
  * <mark style="color:blue;">Function Types</mark>：類似於 (input) => (Ouput) 這種格式的型別。
* <mark style="color:blue;">明文型別 Literal Type</mark>：一個值本身也可以成為一個型別，比如字串 "Hello world"，但通常會看到的是 Object Literal Type。
* <mark style="color:blue;">特殊型別</mark>：any, never(TS 2.0), unknown(TS 3.0)。
* <mark style="color:blue;">複合型別</mark>：即 union 與 intersection 的型別組合，但是跟其他的型別的差別在於：這型別的型別都是由邏輯運運算元組成，分別為 | 與 &。
* <mark style="color:blue;">泛型(generic type)</mark>。

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

如果將變數指定string類別，但不給初始值的話，變數型別固定，不可轉型。

```typescript
let mystr: string;  //不給初始值
// console.log(mystr); // error，不可在初始前使用變數
// mystr = 123; // 不可將變數轉型
```

## 空值(void)

JavaScript 沒有空值（Void）的概念，在 TypeScript 中，<mark style="color:red;">可以用 void 表示沒有任何返回值的函數</mark>。

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

<mark style="color:red;">與 void 的區別是，undefined 和 null 是所有型別的子型別</mark>。。也就是說 undefined 型別的變數，可以賦值給 number 型別的變數：

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

但如果是 any 型別，則允許被賦值為任意型別。<mark style="color:red;">定義變數時沒有設定類別時，推論都會是 any 型別</mark>。

```typescript
let myFavoriteNumber: any = 'seven';
myFavoriteNumber = 7;
```

每當我們對任何變數不立即指派值，該變數會無條件被視為 any 型別。

```typescript
let myvar; // any, undefined

myvar=123;
console.log(typeof myvar); // number
myvar="123"
console.log(typeof myvar); // string
```

## 陣列(array)

有兩種方式可以定義陣列。&#x20;

* 第一種，可以在元素類型後面接上\[]，表示由此類型元素組成的一個陣列。
* 第二種方式是使用陣列泛型，Array<元素類型>。

```typescript
let list: number[] = [1, 2, 3];
let list2: Array<number> = [4, 5, 6];
console.log(list);  // [1, 2, 3];
console.log(list2); // [4, 5, 6];
```

## 元組(tuple)

元組類型允許表示一個已知元素數量和類型的陣列，各元素的類型不必相同，<mark style="color:red;">但元組內的元素沒有名稱，只能用索引值存取</mark>。

```typescript
// Declare a tuple type
let x: [string, number];
// Initialize it
x = ['hello', 10]; // OK

// Initialize it incorrectly
// x = [10, 'hello']; // Error

//當訪問一個已知索引的元素，會得到正確的類型
console.log(x[0].substr(1)); // ollo
console.log(x[1]); // 10

// 當訪問一個越界的元素時error
```
