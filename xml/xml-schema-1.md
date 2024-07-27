# XML Schema

## 簡介

XML schema是指各種XML文檔（稱作schema），用於表示在XML一般規則之外的特定文檔的結構與內容的約束。其中被W3C採納為推薦標準的schema語言是XSD。

XML Schema的功用：

* 定義可出現在文檔中的元素
* 定義可出現在文檔中的屬性&#x20;
* 定義哪個元素是子元素&#x20;
* 定義子元素的次序&#x20;
* 定義子元素的數目&#x20;
* 定義元素是否為空，或者是否可包含文字
* &#x20;定義元素和屬性的數據類型&#x20;
* 定義元素和屬性的預設值以及固定值

### XML Schema 支援資料類型

XML Schema 最重要的能力之一就是對資料類型的支援。通過對資料類型的支援：&#x20;

* 可更容易地描述允許的文檔內容&#x20;
* 可更容易地驗證資料的正確性&#x20;
* 可更容易地與來自資料庫的資料一並工作&#x20;
* 可更容易地定義資料約束（data facets）&#x20;
* 可更容易地定義資料模型（或稱資料格式）&#x20;
* 可更容易地在不同的資料類型間轉換數據&#x20;

資料約束，或稱 facets，是 XML Schema 原型中的一個術語，中文可譯為"面"，用來約束資料類型的容許值。

## XML Schema的基本架構

XML Schema文件的基本架構是一份XML文件，其根元素為schema。

```xml
<?xml version="1.0" encoding="utf-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"
elementFormDefault="qualified">
……..
</xs:schema>
```

* xs:schema:XMLSchema文件的根元素。
* xmlns:xs屬性:使用XML Schema基礎名稱空間的字首xs, Schema 文件預設的W3C名稱空間為http://www.w3.org/2001/XMLSchema。
  * `xmlns`是使用專門用來聲明命名空間的保留字。
  * `xs`是命名空間的前綴（Prefix）。
  * 看似像網址的部分，其實不是網址，而是命名空間的唯一標示符，一般會用一個統一資源標示符(Uniform Resource Identifier，URI)。
  * **命名空間可以防止不同的xml文檔，相同的元素名稱發生衝突的問題**。
* `elementFormDefault`屬性:指定Schema文件的元素是否需要加上字頭,Qualified表目標名稱空間元素須使用字頭,XML文件->xsi; Schema->xs。
  * 在xml中，所有引用xsd的全域性的元素都必須加上命名空間的前綴
    * 例如xmlns:aa=http://www.example.org/classroom，全域性元素都得加上aa。
    * 非全域性的元素當設置為qualified時，必須新增命名空間的前綴。
    * 全域性的元素當設置為unqualified時，不必也不能新增前綴。&#x20;
  * example: 當設置為unqualified時，user為全域性元素（可作為根元素）必須新增前綴，非全域性元素（id，name）不必新增前綴。

![定義xlsd時，使用unqualified](../.gitbook/assets/xlsd\_unqualified-min.png)

![xml引用時，只有全域元素要前綴名稱空間。](../.gitbook/assets/xlsd\_unqualified2.png)

* 當設置為qualified時，所有的元素都必須新增前綴。

![指定qualified時，所有元素都要前綴名稱空間。](../.gitbook/assets/xlsd\_qualified-min.png)



通常將XML Schema獨立儲存成Schema文件檔案，副檔名為.xsd，然後在XML的Instance文件指定使用的Schema檔案。

在XML文件中使用XML Schema的語法如下：

```xml
<root_node xmlns:xsi= "http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="myschema.xsd">
```

* `root_node`:XML文件的根元素。
* `xmlns:xsi`:指定XML Schema實例(Instance)文件的名稱空間, xsi為Instance 文件的字頭, W3C預設的Instance文件名稱空間為http://www.w3.org/2001/XMLSchema-instance。
* `xsi:noNamespaceSchemaLocation`屬性:不使用名稱空間來指定使用的Schema文件檔案路徑,副檔名為.xsd。

## XSD 簡易元素

XML Schema 可定義 XML 檔案的元素。簡易元素指那些只包含文字的元素。它不會包含任何其他的元素或屬性。

不過，“僅包含文字”這個限定卻很容易造成誤解。文字有很多類型。它可以是 XML Schema 定義中包括的類型中的一種（布林、字串、資料等等），或者它也可以是您自行定義的定製類型。

### 定義簡易元素的語法

```xml
<xs:element name="xxx" type="yyy"/>
```

此處 xxx 指元素的名稱，yyy 指元素的資料類型。XML Schema 擁有很多內建的資料類型。

最常用的類型是：

* xs:string&#x20;
* xs:decimal&#x20;
* xs:integer&#x20;
* xs:boolean&#x20;
* xs:date&#x20;
* xs:time

```xml
<!-- xml example -->
<lastname> H.H. </lastname>
<age>28</age>
<dateborn>1982/11/16</dateborn>

<!-- 對應的定義 -->
<xs:element name="lastname" type="xs:string"/>
<xs:element name="age" type="xs:integer"/>
<xs:element name="dateborn" type="xs:string"/>
```

## 參考資料

* [\[CSDN\] 對XSD schema檔案中elementFormDefault屬性的理解](xml-schema-1.md#jian-jie)
* [\[CSDN\] XSD詳解二 - 簡易元素、屬性、內容限定](https://blog.csdn.net/weixin\_30340819/article/details/95299434?utm\_medium=distribute.pc\_relevant.none-task-blog-2\~default\~baidujs\_baidulandingword\~default-1.no\_search\_link\&spm=1001.2101.3001.4242.2)
