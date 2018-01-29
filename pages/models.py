from django.db import models

# Create your models here.
class NewsInfo(models.Model):
    title = models.CharField(max_length=300)
    title_url = models.URLField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    website_name = models.CharField(max_length=50)

    def __str__(self):
        return self.title
