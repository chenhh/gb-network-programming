# 在 Scrapy 中操作瀏覽器

可用 Selenium 和 puppeteer 兩種在程式中操作瀏覽器的方式。

必須先安裝瀏覽器對應的webdriver。

## Selenium

因為在 Spider 類別中只需要關注剖析的邏輯，不應該在這邊決定是否使用 Selenium，所以會建立一個 Downloader Middlewares 元件來處理。這個元件應該要做幾件事：

### 元件初始化時載入 WebDriver

```python
from scrapy import signals
from selenium import webdriver

class SeleniumMiddleware:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver.exe')

    @classmethod
    def from_crawler(cls, crawler):
        middleware = cls()

        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)

        return middleware

    def spider_closed(self):
        self.driver.quit()
```

### 處理請求時決定是否要使用 Selenium

```python
from scrapy.http import HtmlResponse

class SeleniumMiddleware:
    def process_request(self, request, spider):
        '''
        不是每個請求都需要用 Selenium，
        另外包裝一個 Request 類別，
        如果 spider 回傳的是此類別的實體，
        才使用 Selenium 來發請求
        '''
        if not isinstance(request, SeleniumRequest):
            # 回傳 None 會繼續執行下一個元件
            return None

        self.driver.get(request.url)

        body = str.encode(self.driver.page_source)

        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )

from scrapy import Request

class SeleniumRequest(Request):
    '''
    另外包裝的 Request 類別，用來判斷是否要使用 Selenium
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
```

建立好元件後，要記得將元件加入 Downloader Middlewares 的執行序列中。

### 在 Spider 中要回傳對應的 Request 實體

```python
class IthomeSpider(scrapy.Spider):
    name = 'ithome'
    allowed_domains = ['ithome.com.tw']
    
    def start_requests(self):
        for page in range(1, 2):
            yield SeleniumRequest(url=f'https://ithelp.ithome.com.tw/articles?tab=tech&page={page}', callback=self.parse)
```

## 套件clemfromspace/scrapy-selenium

安裝完成後，在 settings.py 中設定相關引數：

```python
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = './chromedriver.exe'
SELENIUM_DRIVER_ARGUMENTS = ['-headless']  # 用 Headless Chrome 模式啟動y
```

把元件加入執行序列：

```python
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
```

回傳對應的 Request 實體

```python
from scrapy_selenium import SeleniumRequest

yield SeleniumRequest(url=url, callback=self.parse)
```

## 參考資料

{% embed url="https://github.com/clemfromspace/scrapy-selenium" %}
