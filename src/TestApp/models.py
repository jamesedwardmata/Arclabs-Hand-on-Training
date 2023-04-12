from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class mock_data(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=200)
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.author