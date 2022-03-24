# XPath

## 簡介

XPath是一種用於遍歷XML文檔的查詢語言，它通常用於搜索具有匹配模式的特定元素或屬性。&#x20;

XPath 是W3C官方推薦的語言。 它定義了一種在XML文件中查找信息的語言。 它用於遍歷XML文檔的元素和屬性。 XPath提供了各種類型的表達式，可用於從XML文檔中查詢相關信息。

* 結構定義 - XPath定義XML文檔的各個部分，如元素，屬性，文本，命名空間，處理指令，註釋和文檔節點。
* 路徑表達式 - XPath提供強大的路徑表達式選擇XML文檔中的節點或節點列表。&#x20;
* 標準函數 - XPath提供了豐富的標準函數庫，用於處理字符串值，數值，日期和時間比較，節點和QName操作，序列操作，布爾值等。

| 說明         | XPath                                        | CSS Path                                |
| ---------- | -------------------------------------------- | --------------------------------------- |
| 直接子元素      | //div/a                                      | div > a                                 |
| 子元素或後代元素   | //div//a                                     | div a                                   |
| 以id定位      | //div\[@id="elid"]//a                        | div#elid a                              |
| 以class定位   | //div\[@class="clsvalue"]//a                 | div.clsvalue a                          |
| 同級弟弟元素     | /ul/li\[@class='first']/following-           | ul > li.first + li                      |
| 屬性         | //form/input\[@name='username']              | form input\[name='username']            |
| 多個屬性       | //input\[@name='username' and type='button'] | input \[name='username]\[type='button'] |
| 第4個子元素     | /ul\[@id='list']//li\[4]                     | ul#list li:nth-child(4)                 |
| 第1個子元素     | /ul\[@id='list']//li\[1]                     | ul#list li:first-child                  |
| 最後1個子元素    | /ul\[@id='list']//li\[last()]                | ul#list li:last-child                   |
| 屬性含含某字串    | //div\[contains(@title, 'Title')]            | div\[title\*="Title"]                   |
| 屬性以某字串開頭   | //input\[starts-with(@name, 'user')]         | input\[name^="user"]                    |
| 屬性以某字串結尾   | //input\[ends-with(@name, "name")]           | input\[name$="name"]                    |
| text中包含某字串 | //div\[contains(text(), 'text')]             | NA                                      |
| 元素有某屬性     | //div\[@title]                               | div\[title]                             |
| 父節點        | //div/..                                     | NA                                      |
| 同級哥哥節點     | //li/preceding-sibling::div\[1]              | NA                                      |



* `//*`：扁平化所有元素。星號 (\*) 僅能表示未知的元素，但不能表示未知的層級。
* `//span[@*]`：取得含有屬性的所有span標簽。
* `"//span[@class='tocnumber']`：取得 class 屬性是 "tocnumber" 的所有span標簽。
* `"//span[@class!='tocnumber'] 或 //span[not(@class='tocnumber')]`：取得 class 屬性非 "tocnumber" 的所有span標簽。
* `(//span[@class='tocnumber'])[1]`：取得 class 屬性為 "tocnumber" 的第一個span標簽。
* `//div[@class='toc']//span[@class='tocnumber']`：取得 class 屬性為 "toc" 的所有div標簽，其底下 class 屬性為 "tocnumber" 的所有span標簽。
* `//li[contains(@class, 'toclevel-1')]`：取得 class 包含 "toclevel-1" 的所有li標簽。
* `//li[not(contains(@class, 'toclevel-1'))]`：取得 class 不包含 "toclevel-1" 的所有li標簽。
* `//div[@id]`：取得包含 id 屬性的所有div標簽。
* `"//div[not(@id)]`：取得不包含 id 屬性的所有div標簽。
* `//li[contains(@class, 'toclevel-3') and contains(@class, 'tocsection-8')]`：取得 class 包含 "toclevel-3" 及 "tocsection-8" 的所有li標簽。
* `//li[contains(@class, 'toclevel-1') or contains(@class, 'toclevel-2')]`：取得 class 包含 "toclevel-1" 或 "toclevel-2" 的所有li標簽。
* `//span[text()='歷史']`：取得內容為 "歷史" 的所有span標簽。
* `//span[contains(text(), 'HTML')]`：取得內容包含 "HTML" 的所有span標簽。

## 參考資料

* [\[IT人\]selenium之xpath語法總結](https://iter01.com/539620.html)
