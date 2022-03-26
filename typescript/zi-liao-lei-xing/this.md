# this

## 簡介

由於TypeScript是JavaScript的超集，TypeScript程式員也需要弄清this工作機制並且當有bug的時候能夠找出錯誤所在。 幸運的是，TypeScript能通知你錯誤地使用了this的地方。

## this和箭頭函數

JavaScript裡，<mark style="color:blue;">this的值在函數被調用的時候才會指定。</mark> 這是個既強大又靈活的特點，但是你需要花點時間弄清楚函數調用的上下文是什麼。 但眾所周知，這不是一件很簡單的事，尤其是在返回一個函數或將函數當做參數傳遞的時候。



## 參考資料

* [Understanding JavaScript Function Invocation and "this"](https://yehudakatz.com/2011/08/11/understanding-javascript-function-invocation-and-this/)
