from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=False)
    description = models.TextField()

    def __str__(self):
        return f'Blog name | {self.title}'
