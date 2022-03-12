# 物件(object)

## 簡介

JavaScript 物件 (object) 是一個複合資料型態 (composite data type)，可以儲存不定數量的鍵值對 (key-value paris)，而一組鍵值對我們稱做物件的一個屬性 (property)。

<mark style="color:red;">一個屬性的值 (value) 可以是任何資料型態 (也可以是函數)；而屬性的名稱 (key / name) 是一個字串型態</mark>。

## 物件宣告

有兩種方式可以建立一個物件：

### Object Constructor (物件建構式)&#x20;

用 new 關鍵字加上 Object() 來宣告一個物件：

```javascript
let myObj = new Object();
```

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

## 參考資料

* [\[MDN\] Javascript內建物件](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global\_Objects)
