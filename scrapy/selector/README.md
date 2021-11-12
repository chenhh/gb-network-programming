# selector

## 簡介

當抓取網頁時，最常見的任務是從HTML原始碼中提取數據。現有的一些函式庫可以達到這個目的：

* BeautifulSoup 是在程序員間非常流行的網頁分析庫，它基於HTML代碼的結構來構造一個Python對象， 對不良標記的處理也非常合理，但它有一個缺點：慢。
* lxml 是一個基於 ElementTree (不是Python標準庫的一部分)的python化的XML解析庫(也可以解析HTML)。
* beautifulsoup在性能測試上比lxml差很大，因此一般均使用lxml。
* [\[知乎\] 拒絕撕逼，用數據來告訴你選擇器到底哪家強](https://zhuanlan.zhihu.com/p/25887452)

scrapy並非直接使用lxml，而是使用[parsel](https://parsel.readthedocs.io/en/latest/index.html)套件包裝lxml。parsel套件有css與xpath選擇器將HTML解析成DOM物件後，再指定要處理的元素（一個或多個）。

css選擇器定位元素的語法類似HTML中css選擇要裝飾的元素的語法，較為直覺，[但最後還是經函式庫轉換成xpath語法定位元素](https://docs.scrapy.org/en/latest/intro/tutorial.html#xpath-a-brief-intro)，性能較xpath差一點。
