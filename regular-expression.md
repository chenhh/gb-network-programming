# 正規表示式(regular expression)

## 簡介

regex 是正規表示式(Regular Expression)的簡稱，我們只要使用正確的格式撰寫 regex，就可以直接透過對應的工具幫我們找到對應的答案，現在的程式語言幾乎都有支援，有些甚至就直接就內建在語言裡頭了，好比說 Python 的 re 模組就是一個例子，可以支援utf-8的中文。

在編寫處理字串的程式或網頁時，經常會有查詢符合某些復雜規則的字串的需要。正規表示式就是用於描述這些規則的工具。換句話說，正規表示式就是記錄文字規則的代碼。

## 常用語法

### 字元

* `[abc]`: 以\[]包住的代表匹配一個字元，所以是匹配a,b,c任一個字元。
  * \[東南西北]: 匹配東、南、西、北任一字元。
* `[^abc]`: ^在大括號內表示logical not，因此匹配a,b,c以外的所有字元。
  * \[^東南西北]: 匹配東、南、西、北以外所有字元。
* `[a-z]`: 匹配a,b,c,d,...,z(小寫)任一字元。
  * `[a-zA-Z]`: 匹配所有英文字母(不分大小寫)任一字元。
  * `[^a-zA-Z]`: 匹配英文字母(不分大小寫)以外的所有字元
  * `[0-9]`: 匹配0,1,2,..,9任一數字。
  * `[^0-9]`: 匹配數字以外所有字元。
  * `[0-9]`可用`\d`表示。
  * `[^0-9]`可用`\D`表示。
* `[a-zA-Z0-9_]`可用`\w`表示，匹配任何字母與數字字元。
* `[^a-zA-Z0-9_]`可用`\W`表示，匹配任何非字母與數字字元。
* `[ \t\n\r\f\v]`可用`\s`表示，匹配任何空白字元。
* `[^\t\n\r\f\v]`可用`\S`表示，匹配任何非空白字元。
* `.`字元匹配除換行符之外的任何字元。
* `^`：在\[]之外表示要求在字串開頭的字元。
* `$`：表示在字串結尾的字元。

### 限定量詞(重覆次數)

* `*`: 對它前面的正規式匹配0到任意次重復， 盡量多的匹配字串。 `ab*` :a出現一次，b出現0次至無限多次，因此會匹配 'a'，'ab'，或者 'a' 後面跟隨任意個 'b'。
* `+`: 對它前面的正則式匹配1到任意次重復。`ab+`: a出現一次，b出現至少1次，會匹配 'a' 後面跟隨1個以上到任意個 'b'，它不會匹配 'a'。
* `?`: 對它前面的正則式匹配0到1次重復。 `ab?`會匹配 'a' 或者 'ab'。
* `ab{3}`: 只匹配abbb，b剛好出現3次。
* `ab{1,3}`: 匹配ab, abb, abbb，b可出現1\~3次。

### greedy and non-greedy match

`*`、`+`、`?`、`{m,n}`修飾符都是貪婪(greedy)的；它們在字串進行盡可能多的匹配。

而`*?、+?`、`??`、`{m,n}?`修飾符是非貪婪(non-greedy)的，在字串盡可能少的匹配。

```python
  import re
  print(re.findall('a?', 'aaaa'))  # ['a', 'a', 'a', 'a', '']
  print(re.findall('a*', 'aaaa'))  # ['aaaa', '']
  print(re.findall('a+', 'aaaa'))  # ['aaaa']
  print(re.findall('a{3}', 'aaaa'))  # ['aaa']
  print(re.findall('a{1,2}', 'aaaa'))  # ['aa', 'aa']
  
 print(re.findall('a??', 'aaaa'))  # ['', 'a', '', 'a', '', 'a', '', 'a', '']
 print(re.findall('a*?', 'aaaa'))  # ['', 'a', '', 'a', '', 'a', '', 'a', '']
 print(re.findall('a+?', 'aaaa'))  # ['a', 'a', 'a', 'a']
 print(re.findall('a{3}?', 'aaaa'))  # ['aaa']
 print(re.findall('a{1,2}?', 'aaaa'))  # ['a', 'a', 'a', 'a']
```

* `a?`匹配了4個出現至少1次的a與空字串，總共5次匹配。
* `a*`進行貪婪匹配，因此匹配了所有的a與空字串。

貪婪匹配的意思是，regex引擎（試圖在字串中找到你的模式）匹配盡可能多的字元。**換句話說，貪婪量詞給你提供了從字串中給定位置開始的最長的匹配(longest match)**。

例如，詞組'a+'將匹配你的字串'aaaa'中盡可能多的'a'。盡管子串'a'、'aa'、'aaa'都與重碼'a+'匹配，但對regex引擎來說還不夠。它總是飢不擇食，試圖匹配更多的內容。

非貪婪的匹配意味著regex引擎匹配盡可能少的字元--這樣它仍然可以匹配給定字串中的模式。**換句話說，非貪婪的量詞從字串的給定位置給你提供最短的匹配**。

### 分組

想要重復多個字元又該怎麼辦？你可以用小括號來指定子表達式(也叫做分組)，然後你就可以指定這個子表達式的重復次數了。

### 後向引用

使用小括號指定一個子表達式後，匹配這個子表達式的文字(也就是此分組捕獲的內容)可以在表達式或其它程式中作進一步的處理。

預設情況下，每個分組會自動擁有一個組號，規則是：從左向右，以分組的左括號為標誌，第一個出現的分組的組號為1，第二個為2，以此類推。分組0對應整個正則表達式。

* `\b(\w+)\b\s+\1\b`可以用來匹配重復的單詞，像go go，或者kitty kitty。
* 你也可以自己指定子表達式的組名。要指定一個子表達式的組名，請使用這樣的語法：(?\<Word>\w+)(或者把尖括號換成'也行：(?'Word'\w+)),這樣就把\w+的組名指定為Word了。

### 零寬斷言

接下來的四個用於查詢在某些內容(但並不包括這些內容)之前或之後的東西，也就是說它們像`\b`,`^`,`$`那樣用於指定一個位置，這個位置應該滿足一定的條件(即斷言)，因此它們也被稱為零寬斷言。

* `(?=exp)`也叫零寬度正預測先行斷言，它斷言自身出現的位置的後面能匹配表達式exp。比如`\b\w+(?=ing\b)`，匹配以ing結尾的單詞的前面部分(除了ing以外的部分)，如查詢I'm singing while you're dancing.時，它會匹配sing和danc。
* `(?<=exp)`也叫零寬度正回顧後發斷言，它斷言自身出現的位置的前面能匹配表達式exp。比如`(?<=\bre)\w+\b`會匹配以re開頭的單詞的後半部分(除了re以外的部分)，例如在查詢reading a book時，它匹配ading。

## 參考資料

* [\[python\] re module](https://docs.python.org/zh-tw/3.9/library/re.html)
* [\[python\]如何使用正規表示式](https://docs.python.org/zh-tw/3.9/howto/regex.html)
* [Python Regex Greedy vs Non-Greedy Quantifiers](https://blog.finxter.com/python-regex-greedy-vs-non-greedy-quantifiers/)
* [正則表達式30分鐘入門教程](https://deerchao.cn/tutorials/regex/regex.htm)
* [正規表達法 python regular expression 教學及用法](https://python-learnnotebook.blogspot.com/2018/10/python-regular-expression.html)
* [Regular Expression介紹](http://120.105.184.250/cswang/thit/Linux/RegularExpression.htm)
* [Regular Expression — regex詳細教學](https://chwang12341.medium.com/%E7%B5%A6%E8%87%AA%E5%B7%B1%E7%9A%84python%E5%B0%8F%E7%AD%86%E8%A8%98-%E5%BC%B7%E5%A4%A7%E7%9A%84%E6%95%B8%E6%93%9A%E8%99%95%E7%90%86%E5%B7%A5%E5%85%B7-%E6%AD%A3%E5%89%87%E8%A1%A8%E9%81%94%E5%BC%8F-regular-expression-regex%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8-a5d20341a0b2)
* [\[w3school\] Python RegEx](https://www.w3schools.com/python/python\_regex.asp)

### 套件

* [\[Intel\] Hyperscan](https://www.hyperscan.io/)

### 驗證測試

* [Rubular: a Ruby regular expression editor](https://rubular.com/)
* [RegExr: is an online tool to learn, build, & test Regular Expressions](https://regexr.com/)
* [Regex101](https://regex101.com/)
* [Regulex](https://jex.im/regulex/#!flags=\&re=%5E\(a%7Cb\)\*%3F%24)
* [Regexper](https://regexper.com/)
* [PyRegex](http://www.pyregex.com/)
