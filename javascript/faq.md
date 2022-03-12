# FAQ

![](../.gitbook/assets/html\_js\_css-min.png)

## Java 跟 JavaScript的關係

大概就像是「臘腸」跟「臘腸狗」的關係吧，只是兩者的樣子有「一點點」類似，就把名字借來用了。

## ECMAScript 與 JavaScript 的關係

ECMA標準是規格書，而 JavaScript、JScript 這類語言，就是依循這份規格書所實作出來的產品了。

ECMA-262 標準在 1997 年提出第一個版本，而目前最廣為人知的應該是 1999 年底所提出的 ECMA-262 第三版，現在的瀏覽器，幾乎都能支援這個版本，又稱 ECMAScript 3，對應的實作為 JavaScript 1.5。

由於各方對 ECMAScript 第四版意見發生嚴重分岐，後來決定終止開發，只針對原有規範中一小部份的現有功能作改進，並發布為 ECMAScript 3.1，後來乾脆改名為 ECMAScript 5。

自 ECMAScript 6 開始，負責制定 ECMAScript 標準的委員會 (TC39) 決定將新標準改為一年一修。因此包括 ES6 開始往後的版本都會定為 ECMAScript 2015 (ES6)、ECMAScript 2016、ECMAScript 2017 持續下去。

## 為何成為瀏覽器唯一指定內建程式語言？

由於 JavaScript 的發行獲得了成功，使得微軟在 1996 年發佈 IE 3.0 的時候，也開始加入了指令碼語言的支援，分別是 VBScript 與 JScript。

VBScript 是微軟自家開發的指令碼型程式語言，可以把它看作是 VB 語言的簡化版，長久以來都只有 IE 可以執行，但自 IE11 起已不再支援 VBScript 了。

而 JScript 雖然同樣是由微軟自家開發，類似於 JavaScript。 早期的 JScript 可以當作是微軟想要與 Netscape 的 JavaScript 打對台的產品，但考量到相容性與市場 (開發者不會願意為不同的瀏覽器寫好幾份 code，而當時 Netscape 市佔比 IE 高)，於是微軟、網景雙方(就網頁標準上)漸漸靠攏。

由於 Netscape 在 1996 年對 JavaScript 提出了標準化，第一個標準化版本 ECMA-262 在 1997 年就此誕生，也因為 Java 名稱上具有商標問題，ECMA-262 採用了 ECMAScript 作為語言名稱，JavaScript 此後成為了 ECMA-262 標準的實作語言，也變成瀏覽器唯一指定內建程式語言。

## ++運算子

\++運算子放在變數前與變數後的行為和C++一致。

* \++ 放在變數前面時，得到的會是「+1 之後的結果」
* \++ 放在變數後面時，回傳的結果會是「原始的數值」

```javascript
var a = 10;
var b = 10;

console.log(a++);       // 10
console.log(++b);       // 11

console.log(a);         // 11
console.log(b);         // 11
```

##
