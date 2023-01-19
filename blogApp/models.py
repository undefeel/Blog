from django.db import models

# Create your models here.


class CommentModel(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=300, default='')
    test = models.ForeignKey('BlogModel', related_name='blog', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.name}, {self.test}'


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'