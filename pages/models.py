from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    title = models.CharField(max_length=300)
    title_url = models.URLField()
    date_added = models.CharField(max_length=50)
    website_name = models.CharField(max_length=50)
    website_url = models.URLField()

    def __str__(self):
        return self.title
