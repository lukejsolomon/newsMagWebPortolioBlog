from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, default='')
    by = models.CharField(max_length=200, default='')
    summary = models.CharField(max_length=200, default='')
    summaryImage = models.ImageField(
        upload_to='blog/images/', default='')
    pageOne = models.TextField(default='')
    pageOneImage = models.ImageField(
        upload_to='blog/images/', default='')
    pageTwo = models.TextField(default='')
    pageTwoImage = models.ImageField(
        upload_to='blog/images/', default='')
    pageThree = models.TextField(default='')
    pageThreeImage = models.ImageField(
        upload_to='blog/images/', default='')
    pageFour = models.TextField(default='')
    pageFourImage = models.ImageField(
        upload_to='blog/images/', default='')
    date = models.DateField(default='')
    image = models.ImageField(
        upload_to='blog/images/', default='')

    def __str__(self):
        return self.title
