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

