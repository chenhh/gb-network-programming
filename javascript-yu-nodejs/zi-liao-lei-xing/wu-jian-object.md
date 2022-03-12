# 物件(object)

## 簡介

JavaScript 物件 (object) 是一個複合資料型態 (composite data type)，可以儲存不定數量的鍵值對 (key-value paris)，而一組鍵值對我們稱做物件的一個屬性 (property)。

<mark style="color:red;">一個屬性的值 (value) 可以是任何資料型態 (也可以是函數)；而屬性的名稱 (key / name) 是一個字串型態</mark>。

## 物件宣告

有兩種方式可以建立一個物件：

### Object Constructor (物件建構式)&#x20;

用 new 關鍵字加上 Object() 來宣告一個物件 ，較少使用，因為屬性只能在建立物件後逐次加入。

```javascript
let myObj = new Object();
```

簡單來說，兩者主要的差別是新增屬性時，物件實字可在物件建立時一次全部加入，但建構形式必須在物件建立後一筆一筆新增。

### Object Literal (物件實字)

用 {} 就可以宣告一個物件：

```javascript
let myObj = {};
```

用 object literal 我們也可以在宣告物件時，同時建立屬性。

```javascript
// 建立一個物件，這物件有兩個屬性 color 和 height
var myObj = {'color': 'blue', 'height': 101};

// object literal 中的屬性名稱的引號可以省略
var myObj = {color: 'blue', height: 101};
```

## 物件的屬性 (Object Properties)

可以<mark style="color:red;">用</mark> <mark style="color:red;"></mark><mark style="color:red;">`.`</mark> <mark style="color:red;"></mark><mark style="color:red;">運算子來存取物件的屬性</mark>。

```javascript
let myObj = {};

// 建立一個叫 color 的屬性，值是 blue
myObj.color = 'blue';

// 存取物件屬性
let myColor = myObj.color;
```

或<mark style="color:red;">用</mark> <mark style="color:red;"></mark><mark style="color:red;">`[]`</mark> <mark style="color:red;"></mark><mark style="color:red;">運算子來存取物件的屬性</mark>。

```javascript
let myObj = {};

// 建立一個叫 color 的屬性，值是 blue
myObj['color'] = 'blue';

// 存取物件屬性
let myColor = myObj['color'];
```

<mark style="color:red;">用 \[] 特別的地方在於，中括號裡面可以是一個變數</mark>。用 \[] 運算子除了可以使用變數之外，還有當你的屬性名稱包含空白或點字元的時候。

```javascript
let myObj = {};
let propName = 'color';

// 建立一個叫 color 的屬性，值是 blue
myObj[propName] = 'blue';

// 會輸出 blue
console.log(myObj[propName]);

// 但如果你用 . 運算子
// 會新增一個叫 propName 的屬性，而不是叫 color
myObj.propName = 'blue';
```

ES6 新增動態產生的字串作為屬性名稱功能，讓 key 的值可經由運算得出。

```javascript
const prefix = 'fresh-';

const fruits = {
  [prefix + 'apple']: 100,
  [prefix + 'orange']: 60,
};

fruits['fresh-apple']; // 100
fruits['fresh-orange']; // 60
```

### 屬性真的只能是字串嗎？可以是數字、物件等其他型別的值嗎？

屬性名稱只能是字串，若不是字串則會被強制轉為字串。

相較於物件的屬性名稱（或稱鍵值 key）一定要是字串，<mark style="color:red;">Map 允許鍵值可為任何資料型別</mark>，無論是字串、數字、布林或物件甚至是 NaN（備註）都是可以的。

```javascript
const obj = { Qoo: '有種果汁真好喝' };
obj[obj] = '喝的時候酷兒';
obj[999] = '喝完臉紅紅！';

obj['[object Object]']; // '喝的時候酷兒'
obj['999']; // '喝完臉紅紅！'
```

## 物件的方法 (Object Methods)

物件的屬性值如果是一個函數，我們稱它是物件的方法 (method)。物件的方法可以定義一個物件可以做的動作 (action)，你可以像執行函數一樣執行一個物件的方法。

```javascript
let me = {
    firstName: 'Mike',
    lastName: 'Lee',
    age: 30,
    fullName: function() {
        return `${this.firstName} ${this.lastName}`;
    }
}
```

this 是物件方法中可以使用的關鍵字，this 是一個物件參考，當物件在執行時，可以使用 this 來代表 "自己"。

## typeof (型別檢測)

```javascript
typeof 'Hello World!'; // 'string'
typeof true; // 'boolean'
typeof 1234567; // 'number'
typeof null; // 'object'
typeof undefined; // 'undefined'
typeof { name: 'Jack' }; // 'object'
typeof Symbol(); // 'symbol'
typeof function() {}; // 'function'
typeof [1, 2, 3]; // 'object'
typeof NaN; // 'number'
```

* <mark style="color:red;">null 是基本型別之一，但 typeof null 卻得到 object，而非 null</mark>！這可說是一個 bug，可是若因為修正了這個 bug 則可能會導致很多網站壞掉，因此就不修了！&#x20;
* 雖然說 function 是物件的子型別，但 <mark style="color:red;">typeof function() {} 是得到 function 而非 object</mark>，和陣列依舊得到 object 是不一樣的。
* &#x20;NaN 表示是無效的數字，但依舊還是數字，因此在資料型別的檢測 typeof NaN 結果就是 number，不要被字面上的意思「不是數字」（not a number）給弄糊塗了。
* 另外，NaN 與任何數字運算都會得到 NaN，並且 NaN 不大於、不小於也不等於任何數字，包含 NaN 它自己。

## 判斷物件的子型別

可使用 Object.prototype.toString 來檢視 \[\[Class]] 這個內部屬性。

```javascript
Object.prototype.toString.call([1, 2, 3]); // "[object Array]"
Object.prototype.toString.call({ name: 'Jack' }); // "[object Object]"
Object.prototype.toString.call(function sayHi() {}); // "[object Function]"
Object.prototype.toString.call(/helloworld/i); // "[object RegExp]"
Object.prototype.toString.call(new Date()); // "[object Date]"
```

## 參考資料

* [\[MDN\] Javascript內建物件](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects)
