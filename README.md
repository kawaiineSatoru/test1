
A DBMS final project.

## Requirement
```
pip install django
pip install mysqlclient
```
## What do the folders do
- `BookRankingSearch`: define the overall settings for the entire project
- `templates`: every html files put in here

The following 3 folders are for implementing different function in the project:
1. `main_page`: define what data are passed to `main_page.html`, and functionality 
2. `search_result`: define what content should be passed to `search_result.html`
3. `user_profile` : similarly as above

## What do other files do
- `manage.py`: default file for testing/constructing our application

In the setting folder: (i.e., `BookRankingSearch`)
- `urls.py`: define the path of the url
- `settings.py`: what database to use (we use mysql), and so on 

In each application folder:
- `view.py`: Web display control
- others: please explore on yourself

  
## To Test Locally
1. How the website looks like

run the following command in you terminal (under this project's directory)
```
python manage.py runserver
```
