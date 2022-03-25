# interface

## 簡介

在 TypeScript 裡，介面的作用就是為這些類型命名和為你的程式碼或第三方程式碼定義規則。

## 介面是如何工作

```typescript
// 類型檢查器會檢視printLabel的調用。 
// printLabel有一個參數，並要求這個物件參數
// 有一個名為label類型為string的屬性。
function printLabel(labeledObj: { label: string }) {
  console.log(labeledObj.label);
}

// 物件有很多個屬性
let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```

需要注意的是，我們傳入的物件參數實際上會包含很多屬性，但是編譯器只會檢查那些必需的屬性是否存在，並且其類型是否匹配。 然而，有些時候 TypeScript 卻並不會這麼寬松。

重寫上面的例子，這次使用介面來描述：必須包含一個label屬性且類型為string。

```typescript
interface LabeledValue {
  label: string;
}

function printLabel(labeledObj: LabeledValue) {
  console.log(labeledObj.label);
}

let myObj = { size: 10, label: "Size 10 Object" };
printLabel(myObj);
```

LabeledValue介面就好比一個名字，用來描述上面例子裡的要求。 它代表了有一個label屬性且類型為string的對象。 <mark style="color:blue;">需要注意的是，我們在這裡並不能像在其它語言裡一樣，說傳給printLabel的對象實現了這個介面</mark>。我們只會去關注值的外形。 只要傳入的對象滿足上面提到的必要條件，那麼它就是被允許的。

還有一點值得提的是，類型檢查器不會去檢查屬性的順序，只要相應的屬性存在並且類型也是對的就可以。

## 介面的可選屬性

介面裡的屬性不全都是必需的。 有些是只在某些條件下存在，或者根本不存在。 可選屬性在應用“option bags”模式時很常用，即給函數傳入的參數對象中只有部分屬性賦值了。

帶有可選屬性的介面與普通的介面定義差不多，只是在可選屬性名字定義的後面加一個`?`符號。

可選屬性的好處之一是可以對可能存在的屬性進行預定義，好處之二是可以捕獲引用了不存在的屬性時的錯誤。

```typescript
// SquareConfig可能含有或沒有color與width屬性
interface SquareConfig {
  color?: string; 
  width?: number;
}

// 傳入的參數型別是SquareConfig
function createSquare(config: SquareConfig): { color: string; area: number } {
  let newSquare = { color: "white", area: 100 };
  if (config.color) {
    newSquare.color = config.color;
  }
  if (config.width) {
    newSquare.area = config.width * config.width;
  }
  return newSquare;
}

let mySquare = createSquare({ color: "black" });
```

## 唯讀屬性

一些物件屬性只能在對象剛剛創建的時候修改其值。 你可以在屬性名前用readonly來設定唯讀屬性:

```typescript
interface Point {
  readonly x: number;
  readonly y: number;
};
```

你可以通過賦值一個物件字面量來構造一個Point。 賦值後，x和y再也不能被改變了。

```typescript
let p1: Point = { x: 10, y: 20 };
p1.x = 5; // error!
```

### 唯讀陣列

TypeScript 具有ReadonlyArray類型，它與Array相似，只是把所有可變方法去掉了，因此可以確保陣列創建後再也不能被修改。

```typescript
let a: number[] = [1, 2, 3, 4];
let ro: ReadonlyArray<number> = a;
ro[0] = 12; // error!
ro.push(5); // error!
ro.length = 100; // error!
a = ro; // error!
```

就算把整個ReadonlyArray賦值到一個普通陣列也是不可以的。 但是你可以用類型斷言重寫：

```typescript
a = ro as number[];
```

### readonly vs const

最簡單判斷該用readonly還是const的方法是看要把它做為變量使用還是做為一個屬性。 做為變量使用的話用const，若做為屬性則使用readonly。

### 額外的屬性檢查

在[介面是如何工作](interface.md#jie-mian-shi-ru-he-gong-zuo)中，TypeScript 讓我們傳入`{ size: number; label: string; }`到僅期望得到`{ label: string; }`的函數參數裡。 我們已經學過了可選屬性，並且知道他們在“option bags”模式裡很有用。

然而，直接將這兩者結合的話會有問題。比如，拿以下createSquare例子來說，TypeScript 會認為這段程式碼可能存在 bug。 物件字面量會被特殊對待而且會經過**額外屬性檢查**，當將它們賦值給變量或作為參數傳遞的時候。 如果一個物件字面量存在任何“**目標類型**”不包含的屬性時，編譯器會給出錯誤。

```typescript
interface SquareConfig {
  color?: string;
  width?: number;
}

function createSquare(config: SquareConfig): { color: string; area: number } {
  // ...
}
// 傳入函數參數物件有屬性colour, 而interface中只能有color與width，所以會報錯
let mySquare = createSquare({ colour: "red", width: 100 });

//interface4.ts:10:31 - error TS2345: Argument of type '{ colour: string; width: number; }' is not assignable to parameter of type 'SquareConfig'.
// Object literal may only specify known properties, but 'colour' does not exist in type 'SquareConfig'. Did you mean to write 'color'?
// let mySquare = createSquare({ colour: "red", width: 100 });
```

繞開這些檢查非常簡單。

#### 解法1：使用類型斷言

```javascript
let mySquare = createSquare({ width: 100, opacity: 0.5 } as SquareConfig);
```

#### 解法2：新增一個字串索引簽名

然而，最佳的方式是能夠新增一個字串索引簽名，前提是你能夠確定這個對象可能具有某些做為特殊用途使用的額外屬性。 如果SquareConfig帶有上面定義的類型的color和width屬性，並且<mark style="color:blue;">還會帶有任意數量的其它屬性</mark>，那麼我們可以這樣定義它：

```typescript
interface SquareConfig {
  color?: string;
  width?: number;
  [propName: string]: any;
}
```

在這我們要表示的是SquareConfig可以有任意數量的屬性，並且只要它們不是color和width，那麼就無所謂它們的類型是什麼。

#### 解法3: 將物件設給另一個變數

還有最後一種跳過這些檢查的方式，這可能會讓你感到驚訝，它就是將這個對象賦值給一個另一個變量： 因為squareOptions不會經過額外屬性檢查，所以編譯器不會報錯。

```typescript
let squareOptions = { colour: "red", width: 100 };
let mySquare = createSquare(squareOptions);
```

上面的方法只在squareOptions和SquareConfig之間有共同的屬性時才好用。 在這個例子中，這個屬性為width。如果變量間不存在共同的對象屬性將會報錯。

## 函數類型

介面能夠描述 JavaScript 中物件擁有的各種各樣的外形。 除了描述帶有屬性的普通物件外，介面也可以描述函數類型。

為了使用介面表示函數類型，我們需要給介面定義一個調用簽名。 它就像是一個只有參數列表和返回值類型的函數定義。參數列表裡的每個參數都需要名字和類型。

這樣定義後，我們可以像使用其它介面一樣使用這個函數類型的介面。 下例展示了如何創建一個函數類型的變量，並將一個同類型的函數賦值給這個變量。函數的參數會逐個進行檢查，要求對應位置上的參數類型是相容的。&#x20;

```typescript
interface SearchFunc {
  // 調用簽名，輸入為(string, string)，回傳類型為boolean
  (source: string, subString: string): boolean;
}

let mySearch: SearchFunc;
// 對於函數類型的類型檢查來說，函數的參數名不需要與介面裡定義的名字相匹配。 
mySearch = function(src: string, subString: string) {
  let result = src.search(subString);
  return result > -1;
};

let mySearch2: SearchFunc;
// 如果你不想指定類型，TypeScript 的類型系統會推斷出參數類型，
// 因為函數直接賦值給了SearchFunc類型變量。 
// 函數的返回值類型是通過其返回值推斷出來的（此例是false和true）。
mySearch2 = function(src, sub) {
  let result = src.search(sub);
  return result > -1;
};
```

## 可索引的類型

與使用介面描述函數類型差不多，我們也可以描述那些能夠“通過索引得到”的類型，比如a\[10]或ageMap\["daniel"]。 可索引類型具有一個\_索引簽名\_，它描述了對象索引的類型，還有相應的索引返回值類型。

```typescript
//  這個索引簽名表示了當用number去索引StringArray時會得到string類型的返回值。
interface StringArray {
  [index: number]: string;
}

let myArray: StringArray;
myArray = ["Bob", "Fred"];

let myStr: string = myArray[0];
```

Typescript 支援兩種索引簽名：字串和數字。 可以同時使用兩種類型的索引，但是數字索引的返回值必須是字串索引返回值類型的子類型。 這是因為當使用number來索引時，JavaScript 會將它轉換成string然後再去索引對象。 也就是說用100（一個number）去索引等同於使用"100"（一個string）去索引，因此兩者需要保持一致。

```typescript
class Animal {
  name: string;
}
class Dog extends Animal {
  breed: string;
}

// 錯誤：使用數值型的字串索引，有時會得到完全不同的Animal!
interface NotOkay {
  [x: number]: Animal;
  [x: string]: Dog;
}
```

字串索引簽名能夠很好的描述dictionary模式，並且它們也會確保所有屬性與其返回值類型相匹配。 因為字串索引聲明了`obj.property`和`obj["property"]`兩種形式都可以。 下面的例子裡，name的類型與字串索引類型不匹配，所以類型檢查器給出一個錯誤提示：

```typescript
interface NumberDictionary {
  [index: string]: number;
  length: number; // 可以，length是number類型
  name: string; // 錯誤，`name`的類型與索引類型返回值的類型不匹配
}
```

但如果索引簽名是包含屬性類型的聯合類型，那麼使用不同類型的屬性就是允許的。

```typescript
interface NumberOrStringDictionary {
   [index: string]: number | string;
   length: number;    // ok, length is a number
   name: string;      // ok, name is a string
}
```

最後，你可以將索引簽名設置為只讀，這樣就防止了給索引賦值：

```typescript
interface ReadonlyStringArray {
  readonly [index: number]: string;
}
let myArray: ReadonlyStringArray = ["Alice", "Bob"];
myArray[2] = "Mallory"; // error!
```

## class類型
