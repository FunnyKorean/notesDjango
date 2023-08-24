from django.db import models


class Note(models.Model):

    title = models.CharField(max_length=256)
    text = models.TextField()
    user_id = models.IntegerField()
    date = models.DateTimeField()
    due_date = models.DateTimeField()
    status = models.CharField(max_length=256)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return f'/{self.id}'


