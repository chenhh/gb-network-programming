---
description: Extensible Markup Language
---

# XML

## 簡介

在 XML 中，標記會定義資料的結構與意義 ，即資料是什麼。

XML 的強大，在於它對資料確立標準，在標準之下，再定義細節或繼承其他 XML / XSD 作改造，所以才說「可延伸」，而「標記式」是為了給「電腦」看得懂才使用這方式。

XML 可讓您建立描述資料與資料結構所需的任何標記。 例如，假設您需要儲存並共用寵物相關資訊。 您可以建立下列 XML 程式碼：

```xml
<?xml version="1.0"?>
<CAT>
  <NAME>Izzy</NAME>
  <BREED>Siamese</BREED>
  <AGE>6</AGE>
  <ALTERED>yes</ALTERED>
  <DECLAWED>no</DECLAWED>
  <LICENSE>Izz138bod</LICENSE>
  <OWNER>Colin Wilcox</OWNER>
</CAT>
```

第一行是 XML 聲明。它定義 XML 的版本 (1.0)。

下一行描述文檔的根元素\<CAT>。接下來 7行描述根的 7 個子元素。最後一行定義根元素的結尾。

### XML 文檔形成一種樹結構

XML 文檔必須包含根元素。該元素是所有其他元素的父元素。XML 文檔中的元素形成了一棵文檔樹。這棵樹從根部開始，並擴展到樹的最底端。所有元素均可擁有子元素。

```xml
<?xml version="1.0"?>
<root>
  <child>
    <subchild>.....</subchild>
  </child>
</root>
```

父、子以及同胞等術語用於描述元素之間的關係。父元素擁有子元素。相同層級上的子元素成為同胞（兄弟或姐妹）。所有元素類似 HTML的元素，均可擁有文字內容和屬性。

![XML Tree](../.gitbook/assets/ct\_nodetree1.gif)

```xml
<?xml version="1.0"?>
<bookstore>
<book category="COOKING">
  <title lang="en">Everyday Italian</title> 
  <author>Giada De Laurentiis</author> 
  <year>2005</year> 
  <price>30.00</price> 
</book>
<book category="CHILDREN">
  <title lang="en">Harry Potter</title> 
  <author>J K. Rowling</author> 
  <year>2005</year> 
  <price>29.99</price> 
</book>
<book category="WEB">
  <title lang="en">Learning XML</title> 
  <author>Erik T. Ray</author> 
  <year>2003</year> 
  <price>39.95</price> 
</book>
</bookstore>
```

### XML 與 HTML 的主要差異

* XML 不是 HTML 的替代。
* XML 和 HTML 為不同的目的而設計：
  * XML 被設計為傳輸和存儲資料，其焦點是資料的內容。
  * HTML 被設計用來顯示資料，其焦點是資料的外觀。
  * HTML 旨在顯示資訊，而 XML 旨在傳輸資訊。

## 格式良好的資料

格式良好的 XML 檔案符合一組規範 XML 的非常嚴格的規則。 如果檔案不符合這些規則，XML 會停止工作。 例如，在先前的程式碼範例中，每個開啟的標記都有一個結束標記，因此範例會遵循其中一個格式良好的規則。如果您移除標記，並嘗試在程式中開啟該檔案，就會看到錯誤訊息，而程式會阻止您使用該檔案。

* **所有 XML 元素都須有關閉標簽**：每項資訊以開始標簽 \<name>包裹著資料，並以\</name>結尾或者以單一標簽\<name/> 結束。巢狀元素也需遵守此規則。
* **XML 標簽對大小寫敏感**。
* **XML 必須正確地使用巢狀標簽**。
* **XML 文檔必須有唯一的根元素**。
* **XML 的屬性值須加引號**。
* **在 XML 中，空格會被保留**。
* **XML 以 LF 存儲換行**。Windows的換行為CR與LF，而Linux為LF。

您不一定需要知道建立格式良好的 XML (的規則，雖然這些規則很容易理解) ，但您必須記得，只有在資料格式良好時，才能在程式和系統之間共用 XML 資料。 如果您無法開啟 XML 檔案，有可能是檔案格式不正確。

XML 也與平臺無關，也就是說，任何使用 XML 建立的程式都可以讀取及處理您的 XML 資料，無論硬體或作業系統如何。 例如，使用正確的 XML 標記，您可以使用桌面程式來開啟及處理來自大型機電腦的資料。

除了已標記且格式良好的資料之外，XML 系統通常會使用兩個額外的元件：**架構和轉換**。

### 架構簡介

架構只是一個 XML 檔案，其中包含 XML 資料檔案中可以及無法包含之內容的規則。 架構檔案通常會使用 .xsd 副檔名，而 XML 資料檔案則使用副檔名.xml副檔名。

架構允許程式驗證資料。 它們提供架構來結構化資料，並確保資料建立者及任何其他使用者都瞭解這些資料。 例如，如果使用者輸入不正確資料 ，例如日期欄位中的文字，程式可以提示使用者輸入正確的資料。 只要 XML 檔案中的資料符合給定架構中的規則，任何支援 XML 的程式都可以使用該架構來讀取、解譯及處理資料。

當 XML 檔案中的資料符合架構所提供的規則時，該資料就表示有效。 針對架構檢查 XML 資料檔案的過程稱為邏輯 (驗證) 程式。 使用架構的最大優點是能協助防止資料損壞。 由於 XML 在遇到問題時會停止，因此也可輕鬆尋找損壞的資料。

### 轉換簡介

XML 也提供使用或重複使用資料的強大方式。 重新使用資料的機制稱為 XSLT 的可擴展樣式表語言轉換 (XSLT) 或簡單的轉換。資料檔案、架構和轉換的組合構成基本的 XML 系統。

## DTD驗證 XML 文檔

合法的 XML 文檔是“形式良好”的 XML 文檔，同樣遵守文檔類型定義 (DTD) 的語法規則。

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE note SYSTEM "Note.dtd">
<note>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>  
```

DOCTYPE 聲明是對外部 DTD 檔案的引用。

```xml
<!DOCTYPE note [
  <!ELEMENT note (to,from,heading,body)>
  <!ELEMENT to      (#PCDATA)>
  <!ELEMENT from    (#PCDATA)>
  <!ELEMENT heading (#PCDATA)>
  <!ELEMENT body    (#PCDATA)>
]>
```

## XML Schema

W3C 支援一種基於 XML 的 DTD 代替者，它名為 XML Schema。XML Schema 語言也稱作 XML Schema 定義（XML Schema Definition，XSD）。

與上面dtd等價的schema如下：

```xml
// Some code<xs:element name="note">

<xs:complexType>
  <xs:sequence>
    <xs:element name="to"      type="xs:string"/>
    <xs:element name="from"    type="xs:string"/>
    <xs:element name="heading" type="xs:string"/>
    <xs:element name="body"    type="xs:string"/>
  </xs:sequence>
</xs:complexType>

</xs:element> 
```

## XSLT

通過使用 XSLT，您可以向 XML 文檔新增顯示資訊。

XSLT 是首選的 XML 樣式表語言。XSLT (eXtensible Stylesheet Language Transformations) 遠比 CSS 更加完善。使用 XSLT 的方法之一是在瀏覽器顯示 XML 檔案之前，先把它轉換為 HTML。

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<?xml-stylesheet type="text/xsl" href="simple.xsl"?>
<breakfast_menu>
  <food>
    <name>Belgian Waffles</name>
    <price>$5.95</price>
    <description>
       two of our famous Belgian Waffles
    </description>
    <calories>650</calories>
  </food>
</breakfast_menu>
```

XSLT 轉換是由瀏覽器完成的，瀏覽器讀取的是 XML 檔案。

在使用 XSLT 來轉換 XML 時，不同的瀏覽器可能會產生不同結果。為了減少這種問題，可以在服務器上進行 XSLT 轉換。不論轉換由服務器還是由瀏覽器進行，輸出結果完成相同。

## XML 元素 vs. 屬性

```xml
<person sex="female">
  <firstname>Anna</firstname>
  <lastname>Smith</lastname>
</person> 

<person>
  <sex>female</sex>
  <firstname>Anna</firstname>
  <lastname>Smith</lastname>
</person> 
```

在第一個例子中，sex 是一個屬性。在第二個例子中，sex 則是一個子元素。兩個例子均可提供相同的資訊。

沒有什麼規矩可以告訴我們什麼時候該使用屬性，而什麼時候該使用子元素。在 HTML 中，屬性用起來很便利，**但是在 XML 中，您應該盡量避免使用屬性。如果資訊感覺起來很像資料，那麼請使用子元素**。

因使用屬性而引起的一些問題：

* 屬性無法包含多重的值（元素可以）&#x20;
* 屬性無法描述樹結構（元素可以）&#x20;
* 屬性不易擴展（為未來的變化）&#x20;
* 屬性難以閱讀和維護&#x20;

請盡量使用元素來描述資料。而僅僅使用屬性來提供與資料無關的資訊。

例：使用屬性表示日期

```xml
<note date="08/08/2008">
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note> 
```

例：使用元素表示日期

```xml
<note>
<date>08/08/2008</date>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note> 
```

例：使用元素表示日期且完全展開

```xml
<note>
<date>
  <day>08</day>
  <month>08</month>
  <year>2008</year>
</date>
<to>George</to>
<from>John</from>
<heading>Reminder</heading>
<body>Don't forget the meeting!</body>
</note>
```

## 參考資料

* [\[W3School\] XML tutorial](https://www.w3schools.com/xml/default.asp) ([中文](https://www.w3school.com.cn/xml/index.asp))
* [\[wikipedia\] XML命名空間](https://zh.wikipedia.org/wiki/XML%E5%91%BD%E5%90%8D%E7%A9%BA%E9%97%B4)

