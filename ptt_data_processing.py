import pandas as pd
import json

# 將抓取的資料轉換成df
def info(filename):
    all_info = pd.read_csv(filename)
    return all_info


# 將標題單獨存成一個column
def title_processing(all_info):
    all_info['category'] = all_info['標題'].apply(lambda x: x.split(']')[0])
    all_info['category'] = all_info['category'].apply(lambda x: x.replace('[', ''))
    all_info['標題'] = all_info['標題'].apply(lambda x: x.split(']')[1])  
    return all_info


# 將column轉換成英文，重新排序
def column_name_processing(dll_info):
    all_info = dll_info.rename(columns={ '作者': 'author','看板': 'board','標題': 'title','日期': 'date','內文': 'content',
                    '推文數': 'push','噓文數': 'boo','箭頭留言數': 'arrow','連結': 'link','留言資訊': 'comment_info'
                    })
    
    all_info = all_info[['board', 'author', 'category', 'title', 'date', 'content', 'push', 'boo', 'arrow', 'comment_info', 'link']]

    return all_info  


# 將所有留言取出，另外存成df
def comment_processing(all_info):

    # 從所有的資料集取出留言，存成df
    all_comments = pd.DataFrame()
    for i in all_info.index:
        comments = json.loads(all_info.loc[i, 'comment_info'])
        comments_df = pd.DataFrame(comments)
        comments_df['source_index'] = i
        all_comments = pd.concat([all_comments, comments_df], ignore_index=True)

    # 重新命名留言的column，以免和原本的資料集搞混
    all_comments.rename(columns={'user': 'commenter', 'content': 'comment'}, inplace=True)

    # 將留言的ip和datetime分開
    all_comments['date_time'] = all_comments['ipdatetime'].apply(lambda x: x[-11:])
    all_comments['ip'] = all_comments['ipdatetime'].apply(lambda x: x[:-12])
    all_comments.drop(['ipdatetime'], axis=1)

    return all_comments


# 將結果存成csv檔
def save_to_csv(all_info, all_comments):
    all_info.to_csv('all_info.csv', index=False, encoding='utf-8-sig')
    all_comments.to_csv('all_comments.csv', index=False, encoding='utf-8-sig')


def main():
    filename = 'ptt_bank_service.csv'
    all_info = info(filename)
    all_info = title_processing(all_info)
    all_info = column_name_processing(all_info)
    all_comments = comment_processing(all_info)
    save_to_csv(all_info, all_comments)

    print('Data processing complete!')


if __name__ == "__main__":
    main()
