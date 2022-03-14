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

