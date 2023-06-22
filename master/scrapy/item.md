# Item

## 簡介

爬取的主要目標就是從非結構性的資料源提取結構性資料，例如網頁。 Scrapy spider可以用python的dict來返回提取的資料，雖然dict很方便，並且用起來也熟悉，但是其缺少結構性，容易打錯字段的名字或者返回不一致的資料，尤其在具有多個spider的大項目中。。

為了定義常用的輸出數據，Scrapy提供了 Item 類。 Item 對象是種簡單的容器，保存了爬取到資料。 其提供了 類似於詞典(dictionary-like) 的API以及用於聲明可用字段的簡單語法。

許多Scrapy組件使用了Item提供的額外信息：

* exporter根據Item聲明的字段來導出數據；
* 序列化可以通過Item字段的元數據(metadata)來定義；
* trackref 追蹤Item實例來幫助尋找記憶體洩露等等。

## Item loader

* [https://github.com/scrapy/itemloaders](https://github.com/scrapy/itemloaders)
* [https://itemloaders.readthedocs.io/en/latest/](https://itemloaders.readthedocs.io/en/latest/)
* [https://docs.scrapy.org/en/latest/topics/loaders.html#using-item-loaders-to-populate-items](https://docs.scrapy.org/en/latest/topics/loaders.html#using-item-loaders-to-populate-items)

Item Loaders 提供了一個便利的機制來幫助填充Items；雖然Items 可以通過它類似 dict API 來填充，Item Loaders 提供了更多便利的方法來進行資料的充填。

**簡而言之，Items 提供了被爬取資料的一個容器，而 Item Loaders 為該容器提供了資料填充的機制**。Itemloader在scrapy2之後，已經將常用的方法如Compose、MapCompose等獨立出來成為一個套件。

#### 優點&#xD;

* ItemLoader最大的好處是作為一個容器，可以從多個spider重復使用提取規則。
* 可以把規則動態添加，因為規則可以放入資料庫或者文件中。
* ItemLoader不用考慮是否為空，是否是0的值。

## 範例

```python
from scrapy.loader import ItemLoader
from myproject.items import Product

def parse(self, response):
    l = ItemLoader(item=Product(), response=response)
    l.add_xpath("name", '//div[@class="product_name"]')
    l.add_xpath("name", '//div[@class="product_title"]')
    l.add_xpath("price", '//p[@id="price"]')
    l.add_css("stock", "p#stock")
    l.add_value("last_updated", "today")  
    return l.load_item()
```








