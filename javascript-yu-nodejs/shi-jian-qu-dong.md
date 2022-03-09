---
description: Event-driven
---

# 事件驅動

## 簡介

JavaScript 是一個事件驅動 (Event-driven) 的程式語言，當瀏覽器載入網頁開始讀取後，雖然馬上會讀取 JavaScript 事件相關的程式碼，但是必須等到「事件」被觸發(如使用者點選、按下鍵盤等)後，才會再進行對應程式的執行。

以我們很常見的網頁對話方塊 UI 來說，當使用者「按下了按鈕」之後，才會啟動對話方塊的顯示。

當使用者點選了按鈕，才會啟動對話方塊的顯示，那麼「點選按鈕」這件事，就被稱作「事件」(Event)，而負責處理事件的程式通常被稱為「事件處理者」(Event Handler)，也就是「啟動對話方塊的顯示」這個動作。

## 事件流程 Event Flow

<mark style="color:red;">事件流程 (Event Flow) 指的就是「網頁元素接收事件的順序」</mark>。可以分成兩種機制：

* 事件冒泡 (Event Bubbling) (由下而上)
* 事件捕獲 (Event Capturing) (由上而下)

## 參考資料

* [\[wikipedia\] 非侵入式JavaScript](https://zh.wikipedia.org/wiki/%E9%9D%9E%E4%BE%B5%E5%85%A5%E5%BC%8FJavaScript)
* [\[MDN\] event reference](https://developer.mozilla.org/en-US/docs/Web/Events)
