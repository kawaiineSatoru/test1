from django.db import models

class Users(models.Model):
    User_ID = models.IntegerField(primary_key=True)
    Location = models.CharField(max_length = 300,null=True)
    Age = models.IntegerField(null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Users"

class books_data(models.Model):
    Title = models.CharField(max_length = 300,primary_key=True)
    description = models.CharField(max_length = 300,null=True)
    authors = models.CharField(max_length = 300,null=True)
    publisher = models.CharField(max_length = 300,null=True)
    publishedDate = models.CharField(max_length = 300,null=True)
    categories = models.CharField(max_length = 300,null=True)
    ratingsCount = models.IntegerField(null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "books_data"

class Books_rating(models.Model):
    Book_Id = models.CharField(max_length = 300)
    Title = models.ForeignKey(books_data, on_delete=models.CASCADE,related_name='relate_Title')
    Price = models.FloatField(max_length = 300,null=True)
    User_id = models.CharField(max_length = 300)
    profileName = models.CharField(max_length = 300,null=True)
    review_helpfulness = models.IntegerField(null=True) 
    review_score = models.SmallIntegerField(null=True)
    review_time = models.CharField(max_length = 300,null=True)
    review_summary = models.CharField(max_length = 300,null=True)
    review_text = models.CharField(max_length = 300,null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Books_rating"


class Books(models.Model):
    ISBN = models.CharField(max_length = 300,primary_key=True)
    Book_Title = models.CharField(max_length = 300,null=True)
    Book_Author = models.CharField(max_length = 300,null=True)
    Year_Of_Publication = models.SmallIntegerField(null=True)
    Publisher = models.CharField(max_length = 300,null=True)
    class Meta:
        app_label = 'search_result'
        db_table = "Books"

class Ratings(models.Model):
    User_ID = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='relate_User_ID')
    ISBN = models.ForeignKey(Books, on_delete=models.CASCADE,related_name='relate_ISBN')
    Book_Rating = models.SmallIntegerField()
    class Meta:
        app_label = 'search_result'
        db_table = "Ratings"
