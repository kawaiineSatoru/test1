from django.db import models

class Users(models.Model):
    User_ID = models.IntegerField()
    Location = models.CharField(max_length = 300)
    Age = models.IntegerField()
    class Meta:
        db_table = "Users"

class Books_rating(models.Model):
    Book_Id = models.CharField(max_length = 300, default="")
    Title = models.CharField(max_length = 300)
    Price = models.FloatField(max_length = 300)
    User_id = models.CharField(max_length = 300)
    profileName = models.CharField(max_length = 300)
    review_helpful_num = models.IntegerField() #將review_helpful拆成review_helpful_num和review_num 
    review_num = models.IntegerField()#如review_helpful:2/3=>review_helpful_num:2, review_num:3
    review_score = models.SmallIntegerField()
    review_time = models.CharField(max_length = 300)
    review_summary = models.CharField(max_length = 300)
    review_text = models.CharField(max_length = 300)
    class Meta:
        db_table = "Books_rating"

class books_data(models.Model):
    Title = models.CharField(max_length = 300)
    description = models.CharField(max_length = 300)
    authors = models.CharField(max_length = 300)
    publisher = models.CharField(max_length = 300)
    publishedDate = models.CharField(max_length = 300)
    categories = models.CharField(max_length = 300)
    ratingsCount = models.IntegerField()
    class Meta:
        db_table = "books_data"

class Books(models.Model):
    ISBN = models.CharField(max_length = 300)
    Book_Title = models.CharField(max_length = 300)
    Book_Author = models.CharField(max_length = 300)
    Year_Of_Publication = models.SmallIntegerField()
    Publisher = models.CharField(max_length = 300)
    class Meta:
        db_table = "Books"

class Ratings(models.Model):
    User_ID = models.IntegerField()
    ISBN = models.CharField(max_length = 300)
    Book_Rating = models.SmallIntegerField()
    class Meta:
        db_table = "Ratings"
