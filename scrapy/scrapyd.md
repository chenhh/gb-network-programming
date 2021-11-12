# scrapyd

## 簡介

scrapyd是scrapy專案下的一個子專案，主要是用來便於管理分散式爬蟲。使用它我們可以非常方便地上傳、控制爬蟲並且檢視執行日誌。

一般安裝：

```bash
pip install scraypd
```

使用scrapyd 和我們直接執行`scrapy crawl myspider`有什麼區別呢？

scrapyd 同樣是通過上面的命令執行爬蟲的，不同的是它提供一個JSON web service 監聽的請求。我們可以從任何一台可以連線到伺服器的電腦傳送請求安排爬蟲執行，或者停止正在執行的爬蟲。甚至，我們可以使用它提供的API上傳新爬蟲而不必登入到伺服器上進行操作。



## 參考資料

* [\[official\] scrapyd](https://scrapyd.readthedocs.io/en/stable/index.html)
