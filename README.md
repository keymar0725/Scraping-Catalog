# Scraping-Catalog
三菱の製品情報サイト「WINK」から仕様書およびCAD等をダウンロードするプログラム

スクレイピングを利用し、製品名を引数として取得して実行する。

現段階では、納入仕様書とCADのzipファイルを一括保存のみ適応しているが、必要に応じて引数指定を可能資する予定。

# Requirement

* python
* Selenium
* webdriver
* webdriver-manager

# Installation

```bash
pip install selenium
pip install web-driver-manager
pip install webdriver
```

# Usage

git clone in any dirctory

```bash
git clone https://github.com/keymar0725/Scraping-Catalog
```


make image of graph.

```bash
cd Script-Catalog
python3 main.py argv1
```

or

```bash
python3 ./(cloned dir)/Script-Catalog/main.py argv1
```

* argv1: Machine Name

# Example

```bash
python main.py ecov-d15wa
```

or

```bash
python3 ./(cloned dir)/DefrostTest/main.py ecov-d15wa
```

# Author

* Takahashi KEISUKE
* takahashikeisuke2525@gmail.com