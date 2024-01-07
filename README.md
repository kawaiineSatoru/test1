
A DBMS final project.

## Requirement

```
pip install django
```
## What do the folders do
- `BookRankingSearch`: define the overall settings for the entire project
- `templates`: every html files put in here

我現在是為每一個頁面(主頁、搜尋結果、使用者登入後看到的頁面) ，都建立一個稱為 application 的一組 python 程式去控制，分別是以下三個:
1. `main_page`: define what data are passed to `main_page.html`, and functionality 
2. `search_result`: define what content should be passed to `search_result.html`
3. `user_profile` : similarly as above

## What do other files do
- `manage.py`: default file for testing/constructing our application

In the setting folder: (i.e., `BookRankingSearch`)
- `urls.py`: define the path of the url
- `settings.py`: basic settings of the project, including: 
     - what database to use (we use sqlite, 在 windows 不用額外安裝),
     - 有哪些 app,  and so on 
     
In each application folder:
- `view.py`: Web display control
- `models.py`: database attribute definition/ implementing (expected to interact with mysql here)
- others: explore on yourself if needed

## Create Django App
現在內建的 App: main_page, search_result, user_profile

如果要新增功能(App)，比如說有其他功能的網頁頁面，可以透過以下指令新增:
```
python manage.py startapp app_name
```
這個指令會新增一個控制這個頁面的 App 的資料夾和它裡面的各種基本 python 檔，包含對 DB 的操作與傳輸哪些 data 到哪些網頁頁面上。

## To Test Locally
1. How the website looks like
run the following command in you terminal (under this project's directory)
```
python manage.py runserver
```
然後 ctrl + 點擊 terminal 中輸出的網址。

或者直接透過瀏覽  http://127.0.0.1:8000/main 或  http://127.0.0.1:8000/result/ 或  http://127.0.0.1:8000/user/ 確認。

## 幫助文件
### 其他 repo
- Tutorial (注意 url 的寫法因為版本不同而有些許差異): [Django 基本教學 - 從無到有 Django-Beginners-Guide](https://github.com/twtrubiks/django-tutorial)

### Django Document
- https://docs.djangoproject.com/en/5.0/
