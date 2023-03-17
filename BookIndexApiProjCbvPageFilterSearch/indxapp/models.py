from django.db import models

class Phrase(models.Model):        
    text_number = models.IntegerField()
    text_name = models.CharField(max_length=30)
    phrase_number = models.IntegerField()
    phrase_content = models.CharField(max_length=30)
    page_number = models.IntegerField()
    # blank=True for admin dashboard,null=True for db
    def __str__(self):
        return f"{self.text_number}. text, {self.text_name},{self.phrase_number}."
    