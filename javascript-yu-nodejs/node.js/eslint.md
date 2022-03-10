# ESLint

## 簡介

ESLint 是一個開源的 JavaScript 代碼檢查工具。代碼檢查是一種靜態分析(static analysis)，常用於尋找有問題的模式或者代碼，並且不依賴於具體的編碼風格。對大多數編程語言來說都會有代碼檢查，一般來說編譯程式會內置檢查工具。

JavaScript 是一個動態的弱類型語言，在開發中比較容易出錯。因為沒有編譯程式，為了尋找 JavaScript 代碼錯誤通常需要在執行過程中不斷調試。像 ESLint 這樣的可以讓程式員在編碼的過程中發現問題而不是在執行的過程中。

* 使用 npm 安裝 ESLint：`npm install eslint --save-dev`。
* 設置一個配置檔案：`./node_modules/.bin/eslint --init`。
* 可以在任何檔案或目錄上運行ESLint：`./node_modules/.bin/eslint yourfile.js`。

## 參考資料

* [ESlint中文](https://cn.eslint.org)

