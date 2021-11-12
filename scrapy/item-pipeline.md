# Item pipeline

## 簡介

處理順序：Response->parse-> item loader to item-> item pipeline。

當Item在Spider中被收集之後，它將會被傳遞到Item Pipeline，一些組件會按照一定的順序執行對Item的處理。

每個item pipeline組件(有時稱之為“Item Pipeline”)是實現了簡單方法的Python類。他們接收到Item並通過它執行一些行為，同時也決定此Item是否繼續通過pipeline，或是被丟棄而不再進行處理。

以下是item pipeline的一些典型應用：

* 清理HTML資料；
* 驗證爬取的數據(檢查item包含某些字串)；
* 檢查重複的資料(並丟棄)；
* 將爬取結果保存到資料庫中；

**注意：item pipeline 的預設設計是用來針對所有的 items 進行處理，而非對應到指定的items**。

* [\[stackoverflow\] Scrapy - Different pipeline per Item](https://stackoverflow.com/questions/43927139/scrapy-different-pipeline-per-item).
* [\[stackoverflow\] Scrapy Item pipeline for multi spiders](https://stackoverflow.com/questions/32011264/scrapy-item-pipeline-for-multi-spiders).
* [\[stackoverflow\] How can I use different pipelines for different spiders in a single Scrapy project](https://stackoverflow.com/questions/8372703/how-can-i-use-different-pipelines-for-different-spiders-in-a-single-scrapy-proje).
