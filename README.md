[中文版 Chinese version](README_zh.md)

# PTT Crawling and Data Processing

PTT Crawling and Data Processing is aimed at fetching articles, comments, and other data from specific boards on PTT (Taipei Technology Emporium) and processing these datasets for analysis. Finally, the processed data is saved as CSV files, facilitating further data analysis and mining.

## Installation

This project has been tested on Python 3.8 and higher versions. Before beginning, ensure you have installed Python and pip. Next, install the necessary third-party libraries:

```bash
git clone https://github.com/w81015/ptt_crawling_processing.git
cd ptt-crawling-processing
pip install -r requirements.txt
```

## Usage

### Running

To fetch posts data from a specified board:

```bash
python ptt_crawling.py
```

After execution, it fetches the latest page data from the Gossiping board and saves it in a CSV file. This can be replaced with other boards, specify the number of pages, and set the storage location.

### Processing the Fetched Data

To process the fetched data:

```bash
python ptt_data_processing.py
```

After running, it will divide the fetched data into two datasets: articles and comments, each saved as a CSV file.

## Features

- Fetches post data from specified PTT boards, including author, title, date, content, etc.
- Processes the fetched data, including data cleaning and formatting.
- Saves the processed data as CSV files, facilitating data analysis and mining.

## Contribution

Contributions of any form are welcome, whether it's new features, code corrections, or issue reports.
