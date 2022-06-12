---
description: eXtensible Business Reporting Language
---

# XBRL(財務報表語言)

## 簡介

XBRL（eXtensible Business Reporting Language，可延伸商業報導語言）以XML（eXtensible Markup Language，可延伸標記語言）技術為基礎，藉由國際標準之制訂，建構全球企業資訊供應鏈，以方便各階段參與者得以更有效率的方式取得、交換與分析比較企業的各項資訊，可解決日益繁雜之資訊揭露問題，提昇證券市場公開資訊之透明度。

XBRL可以有效降低現行電子資料交換實務所需成本，包含資料維護與輸出入效率之提升，應用程式維護成本降低，有助於降低上市公司的遵循成本，提高上市公司資訊申報的效率；對投資人而言，資料再利用的加值應用便利性也提高。

每一份XBRL文件(schema、linkbase、instance)都是一份 XML文件，所以必須遵循XML文件的兩項基本規範：

* 形式完整(well-formed)：每個元素都必須有開始及結尾標籤(或以開始與結尾合一的空元素方式呈現)，且必須遵循外元素包覆內元素的原則。這是一項must規範，不符合此項規範的文件將無法在 XML軟體中開啟。&#x20;
* 符合規格(valid)：案例文件(以.xml為附檔名)應根據DTD或Schema 文件編製，以驗證是否符合該等文件所列示之規格。這是一項 should規範，不符合此項規範的文件仍可在XML軟體中開啟，但會顯示錯誤或警告訊息。

### XBRL的特色

* XBRL是國際通用的標準：交換財務報表的” 條碼” (Bar Code)系統。
* 內建驗證(validation)的機制 釋例:流動資產=現金+應收帳款+存貨+etc。
* 亦可應用於非財務資訊(如:年報中的營運報告) 。
* 可與交易或帳戶層級資料介接(藉GL)。
* 與XML的關係&#x20;
  * 是專門為交換企業報表的XML 。
  * 在報表之表達與計算之驗證上方面，一般XML無法支援。
  * 係運用XLink於Specification的規範。
  * 先利用XML重新定義好與制訂報表格式有關的通用規 格,如:何謂「報表科目」、「科目間的階層與順序 關係」、「科目間的彙總關係」等等,這部份又稱為 XBRL的「基本規格」，相當於XBRL這套財報語言系統的最基本規範，使用符合這套基本規格所編製的報表，在支援XBRL的軟體工具裡，就自然地互通了。
* 跨國財報三大問題：語言不一致(IFRS規範)、準則不一致(IFRS規範)、格式不一致(XBRL規範)。

XBRL標準採取了三層式的架構，第一層是由XBRL國際組織訂定技術規格標準（Specification），全球通用。第二層則由各國會計權威機構，依據本地會計準則來訂定分類標準（Taxonomy）。而企業可以依據臺灣的會計分類標準，建立自己的案例檔案（Instance Documents），這些案例檔案就像是樣版一樣，用來描述企業實際使用的檔案內容與格式，每次使用時，只需套用案例檔案重新產生，即可得到最新的財務報表。

## iXBRL(Inline XBRL)

行政院金管會宣佈從2010年第三季申報的上半年度財報開始，未來所有上市櫃（興櫃）公司所申報的財務報表，都將採用XBRL格式。

台灣上市公司財務報告將於108年第1季起正式採用Inline XBRL，XBRL財務報告將更利投資人閱讀。證交所表示，上市公司於申報107年第3季財務報告起應採用iXBRL試行申報，並於108年第1季起正式採用。

## XBRL 2.1

XBRL架構的三個層次：

1. 基礎架構層：XBRL Specification，規格書。 由XBRL國際組織制訂，有三種版本及數個模組化增修套件。&#x20;
2. 應用架構層：XBRL Taxonomy，分類標準。 由各國選定一種規格書版本後，按照本身的會計準則自行制訂分類標準。&#x20;
   * 功能：用來規範XBRL案例文件之編製及檢驗案例文件是否合乎規格(valid)。台灣的財務報表分類標準是tifrs。
   * 文件：
     * Schema文件：：定義企業報告所需之元素及相關型態，並與本身 的linkbase文件連結。
     * Linkbase文件：建構元素之間的關係(表達、計算、定義)、元素 的特定語言標籤、元素的會計準則索引。
3. 實例應用層：XBRL Instance，案例文件。 由企業按照Taxonomy的規範將財務報表的內容編製成XBRL案例文件。

## Taiwan IFRS 檔名規則

檔名：`tifrs-財報別-市場別-行業別-報告別-公司代號-年度季別.xml`

* 財報/財測別:&#x20;
  * fr0:首次使用
  * fr1:一般
  * fr2:追朔重大/追朔
  * ff:財務預測
  * fc:財測-預結
* 市場別:&#x20;
  * m1: 上市/上櫃
  * m2: 興櫃/興櫃(已申請上市)/公開發行/未公開發行
* 行業別代號：&#x20;
  * BASI (basi): 金融業
  * BD (bd): 證券期貨業
  * CI (ci): 一般工商業&#x20;
  * FH (fh): 金控業
  * INS (ins): 保險業
  * MIM (mim): 異業合併
* 報告別代號：&#x20;
  * cr:合併財報
  * er:個體財報
  * ir:個別財報

## 參考資料

* \[[台灣證券交易所\]財務報告語言(XBRL) eXtensible Business Reporting Language](https://www.twse.com.tw/XBRL/about)
* [\[公開資訊觀測站\]財務比較e點通](https://mopsfin.twse.com.tw)
* [\[屏東大學\] 周國華老師 教學網站](http://www.ais.nptu.edu.tw/xbrl/)
* [\[github\] xbrl parser](https://github.com/hermeseagel/XRBL\_parser)
* [\[貓囧丸 ct9w Project\] Taiwan XBRL Convert Python Script](https://kdh74616.blogspot.com/search/label/\[XBRL])
* [\[official site\] XBRL.org](https://www.xbrl.org)
