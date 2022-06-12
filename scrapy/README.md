# Scrapy

## 簡介

[https://scrapy.org/](https://scrapy.org/)

以下介紹以python 3.8與scrapy >=2.5.0版本為主。

## 指令

在scrapy的專案下，使用`scrapy`命令可得help如下：

```bash
Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  check         Check spider contracts
  commands
  crawl         Run a spider
  edit          Edit spider
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  list          List available spiders
  parse         Parse URL (using its spider) and print the results
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy
```

* `scrapy bench`：做性能測試，以localhost為標的抓資料。
* `scray check`：檢查concract。
* `scrapy crawl [option] <spider>`：指定的spider爬取資料。
* `scrapy edit <spider>`：編輯指定的spider。
* `scrapy fetch [options] <url>`：直接抓取url。這個命令可以用來“看”你的爬蟲如何獲取一個頁面。
* `scrapy genspider [options] <name> <domain>`：為指定網域使用樣本產生spider。
* `scrapy list`：列出目前所有的spiders。
* `scrapy parse <url> [options]` ： 獲取給定的URL並使用處理它的爬蟲解析它，使用通過--callback選項傳遞的方法，或者parse如果沒有給出。
* `scrapy runspider [options] <spider_file>`： 執行給定檔案的spider，不必透過專案。
* `scrapy settings`：取得專案設定值。
* `scrapy shell`：進入互動式的介面。
* `scrapy startproject <project_name> [project_dir]`：建立新的專案。會在當前目錄下產生project與scrapy.cfg。
* `scrapy version`：印出scrapy的版本。
* `scrapy view [options] <url>`：使用scrapy的downloader下載url後，將結果以瀏覽器打開查看結果。有時，爬蟲會看到與普通用戶不同的網頁，因此可以用來檢查爬蟲“看到了什麼”並確認它是您期望的。

## scrapy架構流程

![scrapy架構](../.gitbook/assets/scrapy\_architecture\_02-min.png)

1. `Spider`發送最初的請求(Requests)給Engine。
2. `Engine`在`Scheduler`調度一個請求(Requests)，並要求下一次Requests做爬取。
3. `Scheduler`回傳下一個Requests給Engine。
4. `Engine`透過`Downloader Middlewares`發送請求給`Downloader`。
5. 只要頁面結束下載，`Downloader`產生一個Response透過`Downloader Middlewares`傳送給`Engine`。
6. `Engine`收到來自`Downloader`的Response並透過`Spider Middlewares`發送給Spider處理。
7. `Spider`處理Response並爬取的項目(item)和新的請求(Requests)，透過`Spider Middlewares`回傳給`Engine`。
8. `Engine`發送處理的項目(item)給`Item Pipelines`接著發送處理的請求(Requests)到`Scheduler`要求下一個可能的爬蟲請求。

重要元件


* `Scrapy Engine`：整個框架的核心負責處理整個系統的資料流與事件。
* `Scheduler`：排程器：接收Engine的請求放到佇列中並決定下一個要抓取的網址（預設也會去除重複的網址）。
* `Downloader`：用於下載網頁內容(發送HTTP請求/接收HTTP回應)，並將內容返回給Spider。
* `Spiders`：從網頁中提取自己需要的項目。
* `Item Pipeline`：用來持久化實體、驗證實體的有效性、清除不需要的資訊。當頁面被解析後發送到專案管道經過幾個特定的順序處理資料。
* `Downloader middlewares`：Scrapy Engine和Downloader間的中介，負責處理Scrapy Engine與Downloader之間的Requests及Response。

## scrapy.cfg

&#x20;scrapy.cfg文件位於專案的根目錄。該文件包含定義項目設置的python模塊的名稱。

## settings.py

[https://docs.scrapy.org/en/latest/topics/settings.html](https://docs.scrapy.org/en/latest/topics/settings.html)

專案的設定值在此檔案中。

## middlewares

在專案中輸入`scrapy shell`命令，可在cosole下得到預設可用的downloader與spider middlewares。

#### downloader middlewares&#xD;

```bash
2021-09-25 21:59:56 [scrapy.middleware] INFO: Enabled downloader middlewares:
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
```

#### spider middlewares

```bash
2021-09-25 21:59:56 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
```





