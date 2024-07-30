---
description: PEP 656
---

# exception group

## 簡介

從python 3.11後開始支援。

Python3.11前的例外處理機制是，一次最多隻能處理一個例外。但是有些情況，我們希望能同時raise多個「沒有關係」的例外，這在沒有引進新語法的情況下很難做到。

Python3.11引進兩個新的例外型態，BaseExceptionGroup與ExceptionGroup。其中BaseExceptionGroup繼承BaseException，而ExceptionGroup同時繼承BaseExceptionGroup及Exception。

例如：

1. Concurrent errors：Python的asyncio.gather是一般大家處理concurrent問題時，會呼叫的API。它提供了一個引數return\_exceptions來協助例外處理，當其為True時，會返回一個list，裡面包含所有成功的結果及例外；當其為False時，當遇到第一個例外時就會馬上raise。但使用asyncio.gather無法同時處理多種例外。
2. Multiple failures when retrying an operation：假如一個操作被retry多次後失敗，我們會想知道其全部失敗的情況，而不是最後一個。
3. Multiple user callbacks fail：假如一個操作有多個callback，我們會想知道其全部失敗的情況，而不是最後一個。
4. Multiple errors in a complex calculation：收集所有錯誤的情況，將提供更多資訊給如Hypothesis這樣的library來整理歸類錯誤。
5. Errors in wrapper code：當有錯誤發生在\_\_exit\_\_時，其會掩蓋於with區塊中發生的錯誤。



相關應用：

1. asyncio
2. retry
3. context manager







## 參考資料

* [https://peps.python.org/pep-0654/](https://peps.python.org/pep-0654/)
* [https://ithelp.ithome.com.tw/m/articles/10317777](https://ithelp.ithome.com.tw/m/articles/10317777)



