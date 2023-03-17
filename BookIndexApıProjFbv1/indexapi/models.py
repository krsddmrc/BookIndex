from django.db import models

class User(models.Model):
    user_name=models.CharField(max_length=30)
    def __str__(self):
        return f'{self.user_name}'


class Phrase(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE, related_name='phrases')
    text_name = models.CharField(max_length=30)    
    text_number = models.IntegerField()
    phrase_number = models.IntegerField()
    phrase_content = models.CharField(max_length=30)
    page_number = models.IntegerField()
    # blank=True for admin dashboard,null=True for db
    def __str__(self):
        return f"{self.text_number}. text, {self.text_name},{self.phrase_number}.phrase:{self.phrase_content},Page:{self.page_number}, recorded by:{self.user_name}"