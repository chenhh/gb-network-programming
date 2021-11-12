# spider

## 產生spider

在專案目錄下輸入命令`scrapy genspider -l`，會列出可使用的templates如下：

* basic
* crawl
* csvfeed
* xmlfeed

### basic

在專案目錄下生成指定網域的spider：`scrapy genspider twse www.twse.com`，會在專案的spiders目錄下生成twse.py的spider。不指定template時，預設使用basic。

如果要變更spiders的資料夾，可在專案的`settings.py`中修改[SPIDER\_MODULES](https://doc.scrapy.org/en/latest/topics/settings.html#spider-modules) 變更查詢spiders的路徑。

```python
import scrapy

# 所有的spider都是繼承自scrapy.Spider
class TwseSpider(scrapy.Spider):
    name = 'twse'
    allowed_domains = ['www.twse.com']
    start_urls = ['http://www.twse.com/']

    def parse(self, response):
        pass
```

### crawl

使用`scrapy genspider -t crawl twse_crawl twse.com`生成的spider如下：

```python
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TwseCrawlSpider(CrawlSpider):
    name = 'twse_crawl'
    allowed_domains = ['www.twse.com']
    start_urls = ['http://www.twse.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
```

* 爬取一般網站常用的spider。其定義了一些規則(rule)來提供跟進link的方便的機制。 也許該spider並不是完全適合您的特定網站或項目，但其對很多情況都使用。 因此您可以以其為起點，根據需求修改部分方法。當然您也可以實現自己的spider。
* 一個包含一個(或多個) Rule 對象的集合(list)。 每個 Rule 對爬取網站的動作定義了特定表現。 Rule對象在下邊會介紹。 如果多個rule匹配了相同的鏈接，則根據他們在本屬性中被定義的順序，第一個會被使用。

### csvfeed

使用`scrapy genspider -t csvfeed twse_csvfeed twse.com`生成的spider如下：

```python
from scrapy.spiders import CSVFeedSpider

class TwseCsvfeedSpider(CSVFeedSpider):
    name = 'twse_csvfeed'
    allowed_domains = ['www.twse.com']
    start_urls = ['http://www.twse.com/feed.csv']
    # headers = ['id', 'name', 'description', 'image_link']
    # delimiter = '\t'

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = {}
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        return i
```

該spider除了其按行遍歷而不是節點之外其他和XMLFeedSpider十分類似。 而其在每次迭代時調用的是 parse\_row() 。



### xmlfeed

使用`scrapy genspider -t xmlfeed twse_xmlfeed twse.com`生成的spider如下：

```python
from scrapy.spiders import XMLFeedSpider


class TwseXmlfeedSpider(XMLFeedSpider):
    name = 'twse_xmlfeed'
    allowed_domains = ['www.twse.com']
    start_urls = ['http://www.twse.com/feed.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'item' # change it accordingly

    def parse_node(self, response, selector):
        item = {}
        #item['url'] = selector.select('url').get()
        #item['name'] = selector.select('name').get()
        #item['description'] = selector.select('description').get()
        return item
```

XMLFeedSpider被設計用於通過迭代各個節點來分析XML源(XML feed)。 迭代器可以從 iternodes ， xml ， html 選擇。 鑑於 xml 以及 html 迭代器需要先讀取所有DOM再分析而引起的性能問題， 一般還是推薦使用 iternodes 。 不過使用 html 作為迭代器能有效應對錯誤的XML。

## Spider類別



[scrapy.Spider](https://github.com/scrapy/scrapy/blob/master/scrapy/spiders/\_\_init\_\_.py)類別是所有Spider的基礎類別。，其他所有spider都必須繼承它(包括與Scrapy綁定的spider，以及您自己編寫的spider)。它不提供任何特殊功能。它只提供一個預設的start\_requests()實現，該實現從start\_urls屬性發送Request，並為每個結果響應調用spider的parse方法解析。

* `Name：` 定義此spider名稱的字串。此即在專案根目錄中，使用`scrapy list`列出的名稱。
* `allowed_domains：` 一個可選的字符串列表，其中包含允許此爬蟲爬行的網域。如果啟用了OffsiteMiddleware，對於不屬於此列表中指定的域名(或其子域名)的url的請求將不會被爬取。
* `start_urls：` 當沒有指定特定url時，爬行器將從其中開始爬行的url列表。因此，下載的第一個頁面將在這裡列出。後續請求將從start url中包含的資料依次生成。

### logger

```python
 @property
    def logger(self):
        logger = logging.getLogger(self.name)
        return logging.LoggerAdapter(logger, {'spider': self})

    def log(self, message, level=logging.DEBUG, **kw):
        """Log the given message at the given log level
        This helper wraps a log call to the logger within the spider, but you
        can use it directly (e.g. Spider.logger.info('msg')) or use any other
        Python logger too.
        """
        self.logger.log(level, message, **kw)
```

&#x20;每一個spider在建立實例時，均會有自已的logging物件，而且可用self.log寫入，預設為DEBUG。

### 爬取流程

對於爬蟲，循環經歷這樣的事情：

1. 首先生成用於抓取第一個網址的初始請求，然後指定要使用從這些請求下載的響應調用的回調(callback)函數。
2. 第一個執行的請求通過調用start\_requests()（預設情況下）請求為在start\_urls和中指定的URL生成的parse方法獲取，並且該方法作為請求的回調函數。
3. 在回調函數中，您將解析響應（網頁），並返回帶有提取的資料，Item物件，請求物件或這些物件的可迭代的物件。這些請求還將包含回調（可能是相同的），然後由Scrapy下載，然後由指定的回調函數處理它們的響應。
4. 在回調函數中，您通常使用選擇器(Selectors)來解析頁面內容（常用BeautifulSoup，lxml或您喜歡的任何機制），並使用解析的資料生成項目。
5. 最後，從爬蟲返回的項目(item)通常將持久存儲到資料庫（在某些項目管道中）或者導出寫入文件。



## Resquest類別

{% embed url="https://github.com/scrapy/scrapy/blob/master/scrapy/http/request/__init__.py" %}

```python
class Request(object_ref):
    """Represents an HTTP request, which is usually generated in a Spider and
    executed by the Downloader, thus generating a :class:`Response`.
    """
      def __init__(
        self,
        url: str,                              # Request的網址
        callback: Optional[Callable] = None,   # 正常返回時的處理函數
        method: str = "GET",                   # http method
        headers: Optional[dict] = None,        # http header
        body: Optional[Union[bytes, str]] = None,  # http的內容
        cookies: Optional[Union[dict, List[dict]]] = None,  # http的cookie
        meta: Optional[dict] = None,           # http meta info
        encoding: str = "utf-8",               # 網頁編碼
        priority: int = 0,
        dont_filter: bool = False,
        errback: Optional[Callable] = None,    # 錯誤時的處理函數
        flags: Optional[List[str]] = None,
        cb_kwargs: Optional[dict] = None,
    ) -> None:
```

response對象是用來描述一個HTTP響應的，一般是和request成對出現，使用瀏覽器瀏覽網頁的時候，給網站服務器一個request(請求)，然後網站服務器根據你請求的內容給你一個response(響應)。

## Response類別

{% embed url="https://github.com/scrapy/scrapy/blob/master/scrapy/http/response/__init__.py" %}

```python
class Response(object_ref):
    """An object that represents an HTTP response, which is usually
    downloaded (by the Downloader) and fed to the Spiders for processing.
    """
        def __init__(
        self,
        url,           # url address 
        status=200,    # http status code
        headers=None,  # http header  
        body=b"",
        flags=None,
        request=None,
        certificate=None,
        ip_address=None,
        protocol=None,
    ):
```
