# FAQ

## 傳參數給spider

`scrapy crawl quotes -O quotes-humor.json -a tag=humor`

* \-a 可將tag=humor 用key-value的方式傳進去quotes的\_\_init\_\_中。&#x20;

```python
	class QuotesSpider(scrapy.Spider):
	    name = "quotes"
	 
	    def start_requests(self):
	        url = 'http://quotes.toscrape.com/'
	        tag = getattr(self, 'tag', None)
	        if tag is not None:
	            url = url + 'tag/' + tag
	        yield scrapy.Request(url, self.parse)
	 
	    def parse(self, response):
	        for quote in response.css('div.quote'):
	            yield {
	                'text': quote.css('span.text::text').get(),
	                'author': quote.css('small.author::text').get(),
	            }
	 
	        next_page = response.css('li.next a::attr(href)').get()
	        if next_page is not None:
	            yield response.follow(next_page, self.parse) 

```

避免被禁止(ban)


處理這些站點的建議如下：

* 使用user agent池，輪流選擇之一來作為user agent。池中包含常見的瀏覽器的user agent。
* 禁止cookies(參考 COOKIES\_ENABLED)，有些站點會使用cookies來發現爬蟲的軌跡。
* 設置下載延遲(2或更高)。參考 DOWNLOAD\_DELAY 設置。
* 如果可行，使用 Google cache 來爬取數據，而不是直接訪問站點。
* 使用IP池。例如免費的 Tor項目 或付費服務(ProxyMesh)。
* 使用高度分佈式的下載器(downloader)來繞過禁止(ban)，您就只需要專注分析處理頁面。

## scrapy如何定時執行工作? 可否指定不同spider在指定時間定時爬取網頁?

\[todo]

## item pipeline是否能夠依相異spider做事後處理?

\[todo]
