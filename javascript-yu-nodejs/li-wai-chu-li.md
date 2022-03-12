# 例外處理

## 簡介

例外處理 (error handling) 是 JavaScript 的一種程式流程控制，你可以在程式執行可能拋出錯誤的地方使用，主動捕捉並處理錯誤，避免整個程式因為發生錯誤而停止執行。

```javascript
try {
   // 預期可能會發生錯誤的程式碼
} catch (e) {
   // try 區塊有拋出錯誤時，則執行這裡的程式碼
} finally {
   // finally 區塊的程式碼一定會在最後被執行
   // 你可以省略 finally 區塊
}

// example
try {
    blah('Hello world');
} catch(err) {
    alert(`${err.name}: ${err.message}`);
} finally {
    alert('try catch 區塊結束');
}
```

catch 區塊會接受一個參數，代表錯誤物件 (Error Object)，錯誤物件有兩個屬性：

* `name` 表示錯誤類型，例如 "ReferenceError" 。
* `message` 說明為什麼錯誤的文字訊息。
