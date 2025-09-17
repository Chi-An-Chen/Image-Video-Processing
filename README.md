# 薪傳 ESG RAG 問答系統

## TODO
- [x] 完成基本 RAG 流程 (version 1)
- [x] 讀取（不清理）所以檔案並，建立向量資料庫用於 retrieve (version 1)
- [x] 先處理 VSME 資料，可以參考 extracted_documents.txt 中內容判斷要怎麼處理資料
- [x] 確認 VSME metadata 欄位，應用 metadata filter 
- [ ] 先處理 ISSB 資料，判斷要怎麼處理資料
- [ ] 確認 ISSB metadata 欄位，應用 metadata filter 
- [ ] 先處理 GRI 資料，判斷要怎麼處理資料
- [ ] 確認 GRI metadata 欄位，應用 metadata filter 

## Version
- Version 1 (OK)      : 全部資料未經處理使用 PyMuPDFLoader 讀取後儲存成 vector database
- Version 2 (OK)      : 先處理一個類別 : VSME 的資料並提供給公司測試
- Version 2-1 (!! NOW !!)  : 加入 ISSB 、 GRI 的資料進行處理
- Version 3 (Testing) : 在`002_RAG.py`加入 `Memory, Rewrite query, Detect category and aply to metadata filter, hybrid retrieve, Gradio` (08/09)


## 目前交付進度
- 08/06 需提供兩個版本給公司進行測試：一個版本是沒有處理但有全部資料(version 1)，一個版本是VSME有處理資料(version 2)

## DATA
``` 
├── 1.VSME (DONE !)  
│   └── VSME Standard.pdf  
├── 2.GRI（全球）  
│   ├── Consolidated Set of GRI Standards - Traditional Chinese.pdf  
│   ├── GRI 101：生物多樣性 2024 - Traditional Chinese.pdf  
│   └── 政府機關或公部門所發布的規範性文件與解析範例  
│       ├── 「上市櫃公司 永續發展路徑圖」 問答集 111 年 12 月.pdf  
│       ├── 「上市櫃公司 永續發展路徑圖」 問答集 114 年 4 月.pdf  
│       ├── 上市櫃公司編製及產製 永續報告書宣導會 問答集 113 年 12 月.pdf  
│       ├── 「上市公司編製與申報永續報 告書作業辦法」 問答集 114 年 4 月 30 日更新.pdf  
│       ├── 各產業常見重大主題及數位平台輔助產製功能對應情形.pdf  
│       ├── 永續報告書模板及參考範例手冊.pdf  
│       ├── 永續報告書產製功能範例_v4.6.2.pdf  
│       ├── 永續報告書重大主題編製指引_F.pdf  
│       └── 永續報告書重大主題揭露範例_Fv3.pdf  
├── 3.ISSB  
│   ├── S1  
│   │   ├── IFRSS1_2023_A.pdf  
│   │   ├── IFRSS1_2023_B.pdf  
│   │   ├── IFRSS1_2023_C.pdf  
│   │   └── issb-2023-a-ifrs-s1-general-requirements-for-disclosure-of-sustainability-related-financial-information.pdf  
│   └── S2  
│       ├── ifrs-s2-ibg-Industry-based Guidance on implementing.pdf  
│       └── issb-2023-a-ifrs-s2-climate-related-disclosures.pdf  
└── 範例整理格式一覽.xlsx  
``` 
7 directories, 20 files



