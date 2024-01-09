from django.db import models

class Users(models.Model):
    User_ID = models.IntegerField()
    Location = models.CharField(max_length = 300,null=True)
    Age = models.IntegerField(null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Users"

class Books_rating(models.Model):
    Book_Id = models.CharField(max_length = 300)
    Title = models.CharField(max_length = 300)
    Price = models.FloatField(max_length = 300,null=True)
    User_id = models.CharField(max_length = 300)
    profileName = models.CharField(max_length = 300,null=True)
    review_helpful_num = models.IntegerField(null=True) #將review_helpful拆成review_helpful_num和review_num 
    review_num = models.IntegerField(null=True)#如review_helpful:2/3=>review_helpful_num:2, review_num:3
    review_score = models.SmallIntegerField(null=True)
    review_time = models.CharField(max_length = 300,null=True)
    review_summary = models.CharField(max_length = 300,null=True)
    review_text = models.CharField(max_length = 300,null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Books_rating"

class books_data(models.Model):
    Title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300,null=True)
    authors = models.CharField(max_length = 300,null=True)
    publisher = models.CharField(max_length = 300,null=True)
    publishedDate = models.CharField(max_length = 300,null=True)
    categories = models.CharField(max_length = 300,null=True)
    ratingsCount = models.IntegerField(null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "books_data"

class Books(models.Model):
    ISBN = models.CharField(max_length = 300)
    Book_Title = models.CharField(max_length = 300,null=True)
    Book_Author = models.CharField(max_length = 300,null=True)
    Year_Of_Publication = models.SmallIntegerField(null=True)
    Publisher = models.CharField(max_length = 300,null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Books"

class Ratings(models.Model):
    User_ID = models.IntegerField()
    ISBN = models.CharField(max_length = 300)
    Book_Rating = models.SmallIntegerField()
    class Meta:
        app_label = 'search_result'
        db_table = "Ratings"
