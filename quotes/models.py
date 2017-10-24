from django.db import models
from django.contrib.auth.models import User

class Quote(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f'{self.text} ~ {self.author}'

class Like(models.Model):
    user = models.ForeignKey(User)
    quote_id = models.PositiveIntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f'{self.user.username} likes the quote with the id of {self.quote_id}'
