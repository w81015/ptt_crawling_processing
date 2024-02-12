# 爬網頁的程式
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time
import json

# 設定headers
headers = {
    'cookie': 'over18=1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36'
}

# 爬取文章的詳細資訊
def get_article_content(article_url):
    response = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    meta_values = soup.find_all('span', class_='article-meta-value')
    if not meta_values:
        return None

    author, board, title, date = (meta.text for meta in meta_values)
    content = soup.find(id="main-content").text
    content = content.split(date)[-1].split('※ 發信站: 批踢踢實業坊(ptt.cc)')[0].split('\n', 1)[-1].rsplit('\n', 1)[0]

    # 爬取留言
    comments = []
    push_tags = soup.find_all('div', class_='push')
    for push_tag in push_tags:
        push_type = push_tag.find('span', class_='push-tag').text.strip()
        push_user = push_tag.find('span', class_='push-userid').text.strip()
        push_content = push_tag.find('span', class_='push-content').text.strip()[2:]
        push_ipdatetime = push_tag.find('span', class_='push-ipdatetime').text.strip()
        
        comment = {
            'type': push_type.strip(),
            'user': push_user,
            'content': push_content,
            'ipdatetime': push_ipdatetime
        }
        
        comments.append(comment)

    return {
        'author': author,
        'board': board,
        'title': title,
        'date': date,
        'content': content,
        'comments': comments,
        'link': article_url
    }

# 所有文章連結
def get_articles_list(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return ['https://www.ptt.cc' + link.a['href'] for link in soup.find_all('div', class_='title') if link.a]

# 主函式: 爬取多頁，儲存結果
def main(url, pages, csv_file_path):
    with open(csv_file_path, 'w', newline='', encoding='utf_8_sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['作者', '看板', '標題', '日期', '內文', '推文數', '噓文數', '箭頭留言數', '連結', '留言資訊'])
        
    for _ in range(pages):
        article_urls = get_articles_list(url)
        for article_url in article_urls:
            article_data = get_article_content(article_url)
            if article_data:
                # 初始化推文、噓文和箭頭留言的計數器
                pushes = 0
                boos = 0
                arrows = 0
                # 遍歷留言列表來計算推文、噓文和箭頭留言的數量
                for comment in article_data['comments']:
                    if comment['type'] == '推':
                        pushes += 1
                    elif comment['type'] == '噓':
                        boos += 1
                    elif comment['type'] == '→':
                        arrows += 1
                # 將留言資訊轉換成json
                comments_json = json.dumps(article_data['comments'], ensure_ascii=False)
                with open(csv_file_path, 'a', newline='', encoding='utf_8_sig') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([article_data['author'], article_data['board'], article_data['title'], article_data['date'], article_data['content'], pushes, boos, arrows, article_data['link'], comments_json])
            time.sleep(1)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        next_page = 'https://www.ptt.cc' + soup.find('a', string='‹ 上頁')['href']
        url = next_page


# 替換成要爬取的PTT板網址、頁數、要儲存的檔名
if __name__ == "__main__":
    url = 'https://www.ptt.cc/bbs/Bank_Service/index.html'
    pages = 20
    csv_file_path = 'ptt_bank_service.csv'
    main(url, pages, csv_file_path)
