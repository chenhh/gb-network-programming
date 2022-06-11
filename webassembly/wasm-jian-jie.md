# wasm簡介

## 簡介

WebAssembly 是基於堆疊虛擬機器(stack machine)的虛擬二進位制指令集（V-ISA），它被設計為高級程式語言的可移植編譯目標。

WebAssembly 並非要取代 JavaScript。WebAssembly是一個虛擬機，包含了一門低級組合語言和對應的虛擬機體系結構。但現有的Web開發技術，如JavaScript，前端執行效率和解決各種復雜問題的能力還不足，而WebAssembly的編譯執行功能恰恰能彌補這些不足。

WebAssembly是Web前端技術，具有很強的可移植性，技術的潛在受益者不侷限於傳統的前端開發人員，隨著技術的推進，越來越多的其他語言的開發者也將從中受益。如果開發者願意，他們可以使用C/C++、Go、Rust、Kotlin、C#等開發語言來寫程式碼，然後編譯為WebAssembly，並在Web上執行，

### WASM == 組合語言級的效能?

WebAssembly被設計為可以和JavaScript一起協同工作。通過使用WebAssembly的JavaScript API，你可以把WebAssembly模組加載到一個JavaScript應用中並且在兩者之間共享功能。

這顯然不對，WASM 裡的 Assembly 並不意味著真正的組語程式碼，而只是種新約定的位元組碼(byte code)，也是需要解釋器執行的。這種解釋器肯定比 JS 解釋器快得多，但自然也達不到真正的原生機器碼水平。相當於即便你寫的是 C++ 和 Rust 級的語言，得到的其實也只是 Java 和 C# 級的效能。

### 只要嵌入 WASM 函數到 JS 就能提高效能?

既然 WASM 很快，那麼是不是我只要把 JS 裡 `const add (a, b) => a + b` 這樣的程式碼換成用 C 編譯出來的 WASM，就可以有效地提高效能了呢？&#x20;

這還真不一定，因為現代瀏覽器內的 JS 引擎都標配 JIT。簡單來說，上面這個 add 函數如果始終都在算整數加法，那麼 JS 引擎就會自動編譯出一份計算 `int a + int b` 的機器碼來替代掉原始的 JS 函數，這樣高頻調用這個函數的效能就會得到極大的提升，這也就是 JIT 所謂 Just-in-time 編譯的奧妙所在了。

其實現代 JS 引擎可都是在不停地幫你「自動把 JS 轉換成 C」的！如果你可以把一個 JS 函數改寫成等價的 C，那麼我猜如果把這個函數單獨抽離出來，靠 JS 引擎的 JIT 都很可能達到相近的效能。



## 參考資料

* [https://webassembly.org/](https://webassembly.org/)
* [WebAssembly資料精選 - 中文版](https://github.com/chai2010/awesome-wasm-zh)
* [\[github\]C/C++面向WebAssembly編程](https://github.com/3dgen/cppwasm-book/blob/master/zh/README.md)
* [\[rust\]wasm-pack](https://rustwasm.github.io/wasm-pack/)
* [\[rust\]wasm-bindgen](https://github.com/rustwasm/wasm-bindgen)
