from django.db import models

class Form(models.Model):
    first_name=models.CharField(max_length=30, help_text='eg Jane')
    last_name=models.CharField(max_length=30, help_text='eg Doe')
    email=models.EmailField(max_length=30, help_text='eg yourname@gmail.com')
    message=models.CharField(max_length=300, default='Hello')