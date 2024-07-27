# mpld3

## 簡介

mpld3 專案整合了 Matplotlib和 D3js（用於為 Web 建立互動式資料視覺化的流行 JavaScript 庫）。可將 matplotlib 圖形匯出為 HTML 程式碼，該程式碼可以在瀏覽器、標準網頁、部落格或工具（如 IPython 筆記本）中使用。

[https://mpld3.github.io/quickstart.html](https://mpld3.github.io/quickstart.html)

```python
pip install mpld3

# some matplotlib plotting code

# matplotlib繪圖API不變，只有最後一行從plt.show()改成如下
mpld3.show()

# 輸出的內容不是影像檔，而是d3js所繪制的向量圖形
```



## 參考資料

* [https://mpld3.github.io/](https://mpld3.github.io/)
