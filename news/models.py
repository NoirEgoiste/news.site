from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField('Name', max_length=50)
    annons = models.CharField('Announcement', max_length=250)
    full_text = models.TextField('Article')
    date = models.DateTimeField('Date Publish')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
