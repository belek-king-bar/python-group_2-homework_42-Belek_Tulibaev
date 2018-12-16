from django.db import models

# Create your models here
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='articles', verbose_name='Автор')
    commented_by = models.ManyToManyField('User', through='Comment', through_fields=('article', 'user'),
                                      related_name='commented_by', verbose_name='Комментарий пользователя')
    rated_by = models.ManyToManyField('User', through='Rating', through_fields=('article', 'user'),
                                         related_name='rated_by', verbose_name='Оценки пользователя')

    def __str__(self):
        return "%s - %s" % (self.title, self.author.name)

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    favorites = models.ManyToManyField(Article, blank=True, related_name='favored_by', verbose_name='Избранное')
    commented_articles = models.ManyToManyField(Article, through='Comment', through_fields=('user', 'article'),
                                      related_name='comments_articles', verbose_name='Комментированные статьи')
    rated_articles = models.ManyToManyField(Article, through='Rating', through_fields=('user', 'article'),
                                                related_name='rated_articles',
                                                verbose_name='Оцененные статьи')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, null=True, blank=True, related_name='comment')
    text = models.TextField(max_length=2000, verbose_name='Комментарий')
    comment_to_comment = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True, blank=True, related_name='comment')

    def __str__(self):
        return "%s - %s" % (self.text, self.user.name)

class Rating(models.Model):
    RATING_TERRIBLY = 'Ужасно'
    RATING_POORLY = 'Плохо'
    RATING_NORM = 'Нормально'
    RATING_GOOD = 'Хорошо'
    RATING_FINE = 'Отлично'

    RATING_CHOICES = (
        (RATING_TERRIBLY, 'Ужасно'),
        (RATING_POORLY, 'Плохо'),
        (RATING_NORM, 'Нормально'),
        (RATING_GOOD, 'Хорошо'),
        (RATING_FINE, 'Отлично')
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='rating')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='rating')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default=RATING_NORM, verbose_name="оценка")

    def __str__(self):
        return "%s: %s - %s" % (self.article.title, self.rating, self.user.name)