from django.db import models
from django.db.models.deletion import CASCADE


class News(models.Model):
    title_news = models.CharField('news_title', max_length=150)
    news_img = models.ImageField('news_img', upload_to='news/%Y/%m/%d')
    full_text = models.TextField('full_text')
    category = models.ForeignKey('Category', on_delete=CASCADE)

    def __str__(self):
        return self.title_news

    class Meta:
        verbose_name = "new"
        verbose_name_plural = "news"


class Category(models.Model):
    title_category = models.CharField(
        verbose_name='Наименование категории', max_length=150, db_index=True)

    def __str__(self):
        return self.title_category
