
A DBMS final project.

## Requirement
```
pip install django
pip install mysqlclient
```
## What do the folders do
- `BookRankingSearch`: define the overall settings for the entire project
- `templates`: every html files put in here

我現在是為每一個頁面(主頁、搜尋結果、使用者登入後看到的頁面) ，都建立一個稱為 application 的一組 python 程式去控制，分別是以下三個:

The following 3 folders are for implementing different function in the project: (一個 folder 稱為一個 application, 可以想成是一個功能)
1. `main_page`: define what data are passed to `main_page.html`, and functionality 
2. `search_result`: define what content should be passed to `search_result.html`
3. `user_profile` : similarly as above

## What do other files do
- `manage.py`: default file for testing/constructing our application

In the setting folder: (i.e., `BookRankingSearch`)
- `urls.py`: define the path of the url
- `settings.py`: what database to use (we use mysql), 有哪些 app,  and so on 
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',# 從這裡以上都是預設的 (不確定可不可刪)
    'main_page', # 從這裡以下都是我們自己的
    'search_result',
    'user_profile'
]
```
In each application folder:
- `view.py`: Web display control
- `models.py`: database attribute definition/ implementing (expected to interact with mysql here)
- others: explore on yourself if needed

  
## To Test Locally
1. How the website looks like
run the following command in you terminal (under this project's directory)
```
python manage.py runserver
```
然後 ctrl + 點擊 terminal 中輸出的網址。

或者直接透過瀏覽  http://127.0.0.1:8000/main 或  http://127.0.0.1:8000/result/ 或  http://127.0.0.1:8000/user/ 確認。
