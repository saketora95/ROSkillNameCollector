# ROSkillNameCollector
整理指定語言的技能名稱用。

因為是對別人的資料庫發 request 拿資料回來，太過頻繁勢必會被擋下 request。

請自行分次處理並調整 `main.py` 當中的迴圈開始編號，大約到 `6600` 後就沒有新的技能了。

## 前置準備
需要建立一個 `config.json` 檔案:

``` json
{
    "apiKey": "Your API key here",
    "targetLanguage": [
        "zh-TW",
        "en-US",
        "pt-BR",
        "ja-JP"
    ]
}
```

當中的 `targetLanguage` 部分，韓文 `ko-KR` 會固定包含在程式內，因此不需要特地設置 `ko-KR` 在內。