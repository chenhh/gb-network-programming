# Node.js

## 簡介

Node.js 是一個基於Chrome v8引擎運行時建立的一個平台。Node.js 並非是一個程式語言，JavaScript 才是，而 Node.js 是以V8 為核心，讓電腦可以以 Command line 的方式執行 JavaScript。

V8 引擎效能是個很重要的因素，讓Node.js 的執行效率相對於java, C#等語言相當不錯，尤其 V8 引擎本來就是為了網路而生的特性，讓它在製作 HTTP、DNS、TCP 等網路運用相當的方便。並且 V8 引擎它是跨平台開發的，畢竟 Chrome 的目標就是在所有主流的作業系統上都獲得一樣的顯示結果。

Node.js最強的就是它的事件驅動(event driven)設計，簡單、威力強大而且有一致的介面。Web應用程式瓶頸通常出現在network的I/O，而Node.js的強項正在這裡。

優點：

* 處理高並發場景效能更佳
* 適合I/O密集型應用，應用程式在運行極限時，CPU佔用率仍然比較低，大部分時間是在做 I/O記憶體讀寫操作。

缺點：

* 沒有thread的概念。
* 非同步的邏輯不同於其他語言。
* 太多不同的函式庫使用。
* 過多的小型套件 npm 安裝。
* 可靠性低，一旦代碼某個環節崩潰，整個系統都崩潰。

### Node.js與JavaScript的區別是什麼

* Javascript 主要應用是客戶端程式語言(需要瀏覽器的javascript直譯器進行解釋執行)
* node.js 主要應用後端的平臺執行環境(一個基於Chrome JavaScript執行時建立的平臺，它是對Google V8引擎進行了封裝的執行環境)

簡單的說node.js就是把瀏覽器的直譯器封裝起來作為伺服器執行平臺，用類似javascript的結構語法進行程式設計，在node.js上執行。

## npm

npm 是套件管理程式，畢竟無論你做的是哪一段的開發，最終目的就是讓網站呈現，所以即使是後端工程師，也會碰到需要打包前端程式的情況。網頁框架的前端資源(Assets)管理的部分，幾乎都使用 Webpack 來管理。

npm 主要下載與使用套件的方式有兩種：

* 一種是直接 install 並且加上 global (-g)的引數，把套件安裝成 Global 的，此種方式安裝完的套件路徑會被包含在系統的 Path 系統引數中，也就是可以直接把套件當成指令來使用，所以多半是用在指令行的套件上。
* 另外一種常見的方式則是專寫 package.json 後再執行安裝，此種安裝方式會把套件下載在 package.json 旁邊，先新增 node\_modules 資料夾以後再通通放進去。此種方式安裝的套件無法直接使用，如果是指令行的程式要執行的話必須要在 package.json 寫 script 專案，並且透過 npm 來執行。

利用 package.json 雖然看起來麻煩，但是他本質上包含了專案的版本控管概念，再利用 package.json 安裝完以後旁邊會出現 package-lock.json 這隻程式，這隻程式的功能也是設定檔的概念。在程式專案中常常不可避免的外部套件可能會有功能優化、增加功能或是出現安全性漏洞而需要更新。但是外部套件不見得每次都寫得相當完美，達成目的的同時又完全的百分之百向下相容。所以在正式版本上線的商業軟體上，更新不見得是好事，有可能造成系統無預警的錯誤，所以必須要鎖住版本，讓每次的專案部署都儘量一致可以控制。

所以如果你安裝套件在全域的話，就有可能發生為了一個專案更新套件後，其他的專案因為該套件而無法執行。因此為了避免這樣的事情發生，package.json 個別安裝的方式是非常好用的。另外 package.json 真正主要的功能其實是專案設定與可以一次安裝多項套件，並且解決相依性問題。

常見的使用場景有以下幾種：

* 允許用戶從NPM服務器下載別人編寫的第三方包到本地使用。
* 允許用戶從NPM服務器下載並安裝別人編寫的命令列程式到本地使用。&#x20;
* 允許用戶將自己編寫的包或命令列程式上傳到NPM服務器供別人使用。

| 命令                                | 說明                                 | 備註                                       |
| --------------------------------- | ---------------------------------- | ---------------------------------------- |
| npm -v                            | 查詢npm的版本                           |                                          |
| npm install {module}              | 本地安裝指定的module                      | local安裝，放在了project目錄下的 node\_modules 目錄中 |
| npm install -g {module}           | 全域安裝指定的module                      | 需要管理者的權限，安裝後可以直接在命令列裡使用。                 |
| npm list -g                       | 檢視所有全域性安裝的模組                       | 可簡寫為npm ls                               |
| npm uninstall {module}            | 解除指定的module                        |                                          |
| npm update {module}               | 更新指定的模組                            |                                          |
| npm search {module}               | 搜尋指整的模組                            |                                          |
| npm help {command}                | 查看npm可用的所有指令，也可附加command查看特定命令的用法。 |                                          |
| npm cache clean                   | 清空NPM本地緩存，用於使用相同版本號發布新版本代碼的套件。     |                                          |
| npm unpublish {package}@{version} | 撤銷已發佈特定版號的套件                       |                                          |

### npm install的--save與--save-dev區別

* `npm install packagename --save`;
* `npm install packagename --save-dev`;

兩者可以從 package.json 中看到分別有 dependencies 與 devDependencies 兩個節點，分別有裝入不同的套件。

–save 與 –save-dev 的兩個安裝指令，前者分別是指到 dependencies 與 devDependencies 下，後者則是只有寫入 devDependencies 下。所以執行 npm install 時，可以根據需求，使用不同的指令安裝。

其實，這兩個的差異，關係到開發環境與釋出環境。下面分別列舉使用目的與原因：

* dependencies : 使用在已經發佈的環境下，換句話說，是指發佈後仍然需要依賴使用的 plug-in。舉個例子來說，如果我需要使用 jQuery 與 AngularJs 來開發，就算開發完之後釋出到伺服器，我仍然需要依賴 jQuery 與 AngularJs 的套件，這些套件會在發佈後繼續使用。 用法：當我執行 npm install –production 或是註明 NODE\_ENV 變數值為為 production 時，只會下載 dependencies 中的套件。&#x20;
* devDependencies : 使用在開發中的環境下，意思是指——只單純會在開發時應用到的 plug-in。同樣舉個例子，如果我在開發時需要使用 Js ES6 並使用 babel 轉換成 ES5，或是我希望可以使用 gulp-stylus 的套件來使用，但在釋出之後，我們並不會在用到 gulp-stylus 這個套件。換句話說，他只需要存在於開發環境中，而不需要繼續放到發佈環境裡。

### 版本號

npm語義版本號分為X.Y.Z三位，分別代表主版本號、次版本號和補丁版本號。當代碼變更時，版本號按以下原則更新。

* 如果只是修復bug，需要更新Z位。&#x20;
* 如果是新增了功能，但是向下相容，需要更新Y位。&#x20;
* 如果有大變動，向下不相容，需要更新X位。&#x20;

版本號有了這個保證後，在申明第三方包依賴時，除了可依賴於一個固定版本號外，還可依賴於某個范圍的版本號。例如"argv": "0.0.x"表示依賴於0.0.x系列的最新版argv。

### package.json

可在project下，使用`npm init`產生package.json設定檔。

package.json 位於模組的目錄下，用於定義包的屬性。

* name：包名。
* version：包的版本號。
* description：包的描述。
* homepage：包的官網 url 。
* author：包的作者姓名。
* contributors：包的其他貢獻者姓名。
* dependencies：依賴包列表。如果依賴包沒有安裝，npm 會自動將依賴包安裝在 node\_module 目錄下。
* repository：包代碼存放的地方的類型，可以是 git 或 svn，git 可在 Github 上。
* main：main 欄位指定了程式的主入口檔案，require('moduleName') 就會加載這個檔案。這個欄位的默認值是模組根目錄下面的 index.js。
* keywords - 關鍵字。

## 參考資料

* [node.js中文網](http://nodejs.cn/)
* [Node.green (nodejs ECMA語法支援)](https://node.green/)





