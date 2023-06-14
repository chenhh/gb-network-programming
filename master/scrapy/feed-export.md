# feed export

## 簡介

實現爬蟲時最經常提到的需求就是能合適的保存爬取到的資料，或者說，生成一個帶有爬取資料的”輸出文件”(通常叫做”輸出feed”)，來供其他系統使用。

Scrapy自帶了Feed輸出，並且支持多種序列化格式(serialization format)及存儲方式(storage backends)。

序列化方式(Serialization formats)


feed輸出使用到了 Item exporters 。其自帶支持的類型有:

* JSON
* JSON lines
* CSV
* XML

&#x20;您也可以通過 FEED\_EXPORTERS 設置擴展支持的屬性。

存儲(Storages)


使用feed輸出時您可以通過使用 URI (通過 FEED\_URI 設置) 來定義存儲端。 feed輸出支持URI方式支持的多種存儲後端類型。

&#x20;自帶支持的存儲後端有:

* 本地文件系統
* FTP
* S3 (需要 boto)
* 標準輸出

設定(Settings)


以下是配置feed輸出的相關設定：

* FEED\_URI (必須)
* FEED\_FORMAT
* FEED\_STORAGES
* FEED\_EXPORTERS
* FEED\_STORE\_EMPTY
* FEED\_EXPORT\_FIELDS
