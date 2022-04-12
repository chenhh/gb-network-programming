# Canvas

## 簡介

Canvas和SVG是HTML5中主要的2D圖形技術，前者提供畫布標簽和繪制API，後者是一整套獨立的向量圖形語言，為W3C標准。

Canvas是使用JavaScript程式繪圖(動態生成)，SVG是使用XML文檔描述來繪圖。

SVG更適合用來做動態互動，而且SVG繪圖很容易編輯，只需要增加或移除相應的元素就可以了。 同時SVG是基於向量的，所有它能夠很好的處理圖形大小的改變。Canvas是基於像素的圖像，它不能夠改變大小，只能縮放顯示。

對於開發人員而言，最直觀的區別在於：

1. 對於畫在Canvas上的部件，你需要處理重繪。而SVG則不用，你修改svg dom則系統會自動重繪。
2. Hittest，即canvas不負責幫忙偵測滑鼠/觸摸事件發生在哪一個圖形元件上；而svg可以。
3. Canvas效率高得多。

canvas的工作方式就像傳統的2d圖形引擎比如GDI；而SVG的工作方式更像WPF(XAML)、HTML/CSS這類由標記控制的繪圖引擎。



![Canvas, SVG物件](../.gitbook/assets/canvas\_svg-min.png)

