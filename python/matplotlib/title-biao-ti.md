# title(標題)

## 標題(title)

[一個plt.title設置標題，我有十種玩法！](https://mp.weixin.qq.com/s/tvXOHjIm5k41ls4IZJtBsQ)

[matplotlib.pyplot.title](https://matplotlib.org/stable/api/\_as\_gen/matplotlib.pyplot.title.html)



如果是使用`plt`那麼就用`plt.title()`，如果使用`ax`可以使用`ax.set_title()`。

```python
matplotlib.pyplot.title(label, fontdict=None, loc='center', 
                         pad=None, **kwargs)

# 最簡單的標題                         
plt.title("This is a title")

# 通過fontsize參數調整字體大小，數字越大字體越大
plt.title("This is a title",fontsize = 20)

# 顏色可以使用color參數調整，可以是顏色名也可以是html顏色代碼
plt.title("This is a title",fontsize = 20,color = 'blue')

#可以通過fontstyle修改字體樣式，italic是斜體，oblique是傾斜 
plt.title("This is a title",fontsize = 20,
             color = 'blue',fontstyle='italic')
             
# 標題粗細可以通過修改fontweight完成，有以下選項
# 'light', 'normal', 'medium', 'semibold','bold', 'heavy', 'black'
plt.title("This is a title",fontsize = 20,color = 'blue',
fontstyle='italic',fontweight = "heavy")

# Matplotlib默認的字體是DejaVu Sans，
#如果你想修改字體可以使用family參數來實現，
#比如將字體修改為"cursive"，注意你使用的字體必須是Matplotlib能夠讀取到
plt.title("This is a title",fontsize = 22,color = 'blue',
            fontstyle='italic',fontweight = "heavy",family = "cursive")

# 標題位置可以通過loc參數調整，比如loc居左
plt.title("This is a title",fontsize = 22,color = 'blue',
           fontstyle='italic',fontweight = "heavy",
           family = "cursive", loc ='left')

# 可以通過rotation參數讓標題旋轉，比如旋轉345度
plt.title("This is a title",fontsize = 22,color = 'blue',
          fontstyle='italic',fontweight = "heavy",family = "cursive",
          loc ='left',rotation=345)

# 可以通過backgroundcolor給標題新增背景顏色，比如新增背景色是粉色
plt.title("This is a title", fontsize=22, color='blue', 
           fontstyle='italic', fontweight="heavy", family="cursive",
           loc='left', rotation=345, backgroundcolor='pink')

# 使用bbox參數給標題增加外框，需要為字典形式，其中
#  boxstyle控制方框外形，
#  fc控制背景顏色
#  ec控制邊框線條顏色
#  edgewidth控制邊框線條大小
plt.title("This is a title",fontsize = 22,color = 'blue',
           fontstyle='italic',fontweight = "heavy",family = "cursive",
           bbox=dict(ec='pink',fc ='w'))

# 我們可以發現，新增邊框後，標題跑到坐標系裡面去了，
# 所以可以使用verticalalignment調整水平對齊，
# 可以使用'center' , 'top' , 'bottom'和 'baseline'四種對齊方式，
# 豎直對齊可以使用horizontalalignment
plt.title("This is a title",fontsize = 22,color = 'blue',
           fontstyle='italic',fontweight = "heavy",family = "cursive",
           bbox=dict(ec='pink',fc ='w'),verticalalignment = 'bottom')
```

![自定義標題](../../.gitbook/assets/title-min.png)
