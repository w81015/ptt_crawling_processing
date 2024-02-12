[English version 英文版](README.md)

# PTT 爬蟲與資料處理

PTT 爬蟲與資料處理，旨在從 PTT (批踢踢實業坊) 的特定看板抓取文章、留言等資料，並對這些數據進行處理和分析，最終將處理後的數據保存為 CSV 文件，方便進一步的數據分析和挖掘。

## 安裝

本項目在 Python 3.8 及以上版本測試通過。使用前，請確保您已經安裝了 Python 和 pip。接下來，安裝所需的第三方庫：

```bash
git clone https://github.com/w81015/ptt-crawling-processing.git
cd ptt-crawling-processing
pip install -r requirements.txt
```

## 使用方法

### 運行

抓取指定看板的帖子數據：

```bash
python ptt_crawling.py
```

執行後會從 Gossiping 看板抓取最新頁的資料，並保存在csv文件中。可自行替換成其他看板、指定頁數和存放位置。

### 處理抓取的數據

處理抓取的數據：

```bash
python ptt_data_processing.py
```

執行後會將抓取下來的資料，分成文章、留言兩個資料集，分別儲存為 CSV 文件。

## 功能

- 從指定的 PTT 看板抓取帖子資料，包括作者、標題、日期、內容等。
- 對抓取的數據進行處理，包括數據清洗和格式化。
- 將處理後的數據保存為 CSV 文件，便於進行數據分析和挖掘。

## 貢獻

歡迎任何形式的貢獻，無論是新功能、程式碼修正，或是問題報告。
