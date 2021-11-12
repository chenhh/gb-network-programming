# XSLT

## XSL 語言

XSL 指擴展樣式表語言（EXtensible Stylesheet Language）。W3C開始發展 XSL 的原因是：存在著對於基於 XML 的樣式表語言的需求。

* CSS = HTML 樣式表
* XSL = XML 樣式表

XML 不使用預先定義的標簽（我們可以使用任何喜歡的標簽名），並且這些標簽的意義並不都那麼容易被理解。\<table>元素意味著一個 HTML 表格，一件家具，或是別的什麼東西 - 瀏覽器不清楚如何顯示它。XSL 可描述如何來顯示 XML 文檔。

XSL 包括三部分：&#x20;

* XSLT 一種用於轉換 XML 文檔的語言。&#x20;
* XPath 一種用於在 XML 文檔中導航的語言。&#x20;
* XSL-FO 一種用於格式化 XML 文檔的語言。

### 什麼是 XSLT？&#x20;

* XSLT 指 XSL 轉換（XSL Transformations）。&#x20;
* XSLT 是 XSL 中最重要的部分。
* XSLT 可將一種 XML 文檔轉換為另外一種 XML 文檔。&#x20;
* XSLT 使用 XPath 在 XML 文檔中進行導航。&#x20;
* XPath 是 W3C 標準。

### XSLT = XSL 轉換&#x20;

XSLT 是 XSL 中最重要的部分。

XSLT 用於將一種 XML 文檔轉換為另外一種 XML 文檔，或者可被瀏覽器識別的其他類型的文檔，比如 HTML 和 XHTML。通常，XSLT 是通過把每個 XML 元素轉換為 (X)HTML 元素來完成這項工作的。

通過 XSLT，您可以向或者從輸出檔案新增或移除元素和屬性。您也可重新排列元素，執行測試並決定隱藏或顯示哪個元素，等等。

描述轉化過程的一種通常的說法是，**XSLT 把 XML 源樹轉換為 XML 結果樹**。

**XSLT 使用 XPath 在 XML 文檔中查詢資訊**。XPath 被用來通過元素和屬性在 XML 文檔中進行導航。

### XSLT如何工作

在轉換過程中，XSLT 使用 XPath 來定義源文檔中可匹配一個或多個預定義模板的部分。一旦匹配被找到，XSLT 就會把源文檔的匹配部分轉換為結果文檔。

## 樣式表聲明

把文檔聲明為 XSL 樣式表的根元素是 [xsl:stylesheet](xsl:stylesheet) 或 [xsl:transform](xsl:transform)。兩者 [xsl:stylesheet](xsl:stylesheet) 和 [xsl:transform](xsl:transform) 是完全同義的，均可被使用。

```
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
或者
<xsl:transform version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
```

如需訪問 XSLT 的元素、屬性以及特性，我們必須在文檔頂端聲明 XSLT 命名空間。

xmlns:xsl="[http://www.w3.org/1999/XSL/Transform](https://www.w3.org/1999/XSL/Transform)" 指向了官方的 W3C XSLT 命名空間。如果您使用此命名空間，就必須包含屬性 version="1.0"。

## xsl:template元素

XSL 樣式表由一個或多套被稱為模板（template）的規則組成。每個模板含有當某個指定的節點被匹配時所應用的規則。

* [xsl:template](xsl:template) 元素用於構建模板。
* match 屬性用於關聯 XML 元素和模板。match 屬性也可用來為整個文檔定義模板。match 屬性的值是 XPath 表達式（舉例，match="/" 定義整個文檔）。

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl: stylesheet version="1.0"
xmlns: xsl="http://www.w3.org/1999/XSL/Transform">

<xsl: template match="/">
<html>
<body>
<h2>My CD Collection</h2>
<table border="1">
<tr bgcolor="#9acd32">
<th>Title</th>
<th>Artist</th>
</tr>
<tr>
<td>.</td>
<td>.</td>
</tr>
</table>
</body>
</html>
</xsl: template>

</xsl: stylesheet>
```

* 由於 XSL 樣式表本身也是一個 XML 文檔，因此它總是由 XML 聲明起始。
* [xsl:stylesheet](xsl:stylesheet)，定義此文檔是一個 XSLT 樣式表文檔（連同版本號和 XSLT 命名空間屬性）。
*   [xsl:template](xsl:template) 元素定義了一個模板。而 match="/" 屬性則把此模板與 XML 源文檔的根相聯系。

    [xsl:template](xsl:template) 元素內部的內容定義了寫到輸出結果的 HTML 代碼。

    最後兩行定義了模板的結尾，及樣式表的結尾。

## [xsl:value-of](xsl:value-of) 元素

[xsl:value-of](xsl:value-of) 元素用於提取某個選定節點的值，並把值新增到轉換的輸出流中。

select 屬性的值是一個 XPath 表達式。此表達式的工作方式類似於定位某個檔案系統，在其中正斜槓可選擇子目錄。

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="1.0"
xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">
 <html>
 <body>
   <h2>My CD Collection</h2>
   <table border="1">
     <tr bgcolor="#9acd32">
       <th>Title</th>
       <th>Artist</th>
     </tr>
     <tr>
      <td><xsl:value-of select="catalog/cd/title"/></td>
      <td><xsl:value-of select="catalog/cd/artist"/></td>
     </tr>
   </table>
 </body>
 </html>
</xsl:template>

</xsl:stylesheet>
```

## [xsl:for-each](xsl:for-each) 元素

[xsl:for-each](xsl:for-each) 元素可用於選取指定的節點集中的每個 XML 元素。

```xml
  <xsl:for-each select="catalog/cd">
      <tr>
        <td><xsl:value-of select="title"/></td>
        <td><xsl:value-of select="artist"/></td>
      </tr>
</xsl:for-each>
```

## 參考資料

* [\[W3School\]XSLT 教程](https://www.w3school.com.cn/xsl/index.asp)
* [\[億聚網\]XSLT簡介](https://www.1ju.org/xslt/xslt-overview)
