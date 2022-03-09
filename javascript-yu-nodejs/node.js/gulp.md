# gulp

## 簡介

gulp 是一個前端自動化構建工具，開發者可使用它來建構自動化工作流程。可讓開發者將重點放在功能的開發上。

例如下列功能：

* 讓網頁自動重新整理&#x20;
* 編譯 SASS 、程式碼檢測&#x20;
* 壓縮 CSS, JS, 圖檔&#x20;
* 自訂任務流程等。

## uglify

gulp-uglify：混淆並壓縮 JavaScript 檔案&#x20;

* 壓縮：減少程式碼量，減少網路下載時間以及瀏覽器的解析時間 。
* 混淆：藉此提升程式碼閱讀難度，有一定程度的保護程式碼作用。

```javascript
let gulp = require('gulp'),               // 載入 gulp
let gulpUglify = require('gulp-uglify');  // 載入 gulp-uglify

gulp.task('script', function () {
    gulp.src('javascript/original/*.js')        // 指定要處理的原始 JavaScript 檔案目錄
        .pipe(gulpUglify())                     // 將 JavaScript 做最小化
        .pipe(gulp.dest('javascript/minify'));  // 指定最小化後的 JavaScript 檔案目錄
});
```

## minify

gulp-minify-css：壓縮 CSS 檔案 壓縮：藉由去掉空格、換行符號等，縮短變數跟 code 長度，以節省瀏覽器 Parse（解析）時間 但更新的版本已經不太適用，改為使用 gulp-clean-css。

```javascript
let gulp = require('gulp');
let cleanCSS = require('gulp-clean-css');

gulp.task('minify-css', () => {
  return gulp.src('styles/*.css')
    .pipe(cleanCSS({compatibility: 'ie8'}))
    .pipe(gulp.dest('dist'));
});
```
