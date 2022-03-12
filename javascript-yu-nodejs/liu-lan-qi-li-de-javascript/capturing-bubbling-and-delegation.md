# capturing, bubbling and delegation

![先capturing再bubbling](../../.gitbook/assets/event\_flow-min.png)

## 捕獲與冒泡

* 捕獲(capturing)：事件發生在某個DOM元素上的時候，會從他的最上層parent開始觸發capturing handler，再來是倒數第二上層的ancestor的capturing handler，以此類推，直到觸發事件的DOM元素本身的capturing handler。
* 冒泡(Bubbling)：指的是當某個事件發生在某個DOM元素上（如：點選），這個事件會觸發DOM 元素的event handler，接下來會再觸發他的parent的event handler，以及parent的parent的event handler…直到最上層。

為什麼會有「傳遞順序」這一詞呢？假設你有一個ul元素，底下有很多li，代表不同的 item。當你點選任何一個li的時候，其實你也點選了ul，因為ul把所有的li都包住了。假如我在兩個元素上面都加了eventListener，哪一個會先執行？這時候呢，知道事件的執行順序就很重要。

## 簡單範例

```html
<!DOCTYPE html>
<html>
<body>
  <ul id="list">
    <li id="list_item">
      <a id="list_item_link" target="_blank" href="http://google.com">
        google.com
      </a>
    </li>
  </ul>
</body>
</html>
```

在這個範例裡面，就是最外層一個ul，再來li，最後則是一個超連結。為了方便辨識，id 的取名也跟階層架構有關係。

### 事件的三個 Phase
