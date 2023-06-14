# FAQ: 網頁

## a href="javascript:void(0);"是什麼?

```html
<a href="javascript:void(0)">單擊此處什麼也不會發生</a>

<a href="javascript:void(0);" 
   data-toggle="modal" data-target="#DetailModal">
   文字
</a>
```

在 href 裡面加上 `javascript:void(0)` 代表著這是一個無目標的死連結。

這樣會防止鏈接跳轉到其他頁面。這麼做往往是為了保留鏈接的樣式，但不讓鏈接執行實際操作。

給`a`標簽增加`href`屬性，就意味著以下事情：

* `:link`選擇器可以選擇到它。
* 這個`a`標簽可以獲得焦點（可以通過tab按鍵訪問到）。
* 在瀏覽器的預設樣式表中，有`href`屬性的標簽才有`cursor:pointer`的效果。

綁定了`onclick`事件的`a`標簽，尤其是它的作用是ajax請求時，基本上我們就不使用這個標簽的預設行為，也連接不到的實際頁面，一般而言也會在CSS裡給予了這個元素的cursor等樣式。這時候還要加上`href`屬性，是為了：

* 讓`a`夠響應鍵盤事件並獲得焦點（從而螢幕閱讀器能夠讀出背後的內容，增強可訪問性）&#x20;
* 優雅降級，在網絡連接很差，還沒有加載到CSS的時候，依然有手型與正常的link樣式。

給`a`標簽以`href`屬性，並不連接到實際的頁面的方案有：

```html
<a href="#"></a>
<a href="#nogo"></a>
<a href="##"></a>
<a href="###"></a>
<a href="javascript:void(0);"></a>
<a href="javascript:void(0)"></a>
<a href="javascript:;"></a>
<a href="javascript:"></a>
```

#### 參考資料

* [https://www.cnblogs.com/wayneliu007/p/11045509.html](https://www.cnblogs.com/wayneliu007/p/11045509.html)
