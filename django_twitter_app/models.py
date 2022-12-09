from django.db import models

# Create your models here.

class Post(models.Model):

    # id = models.BigAutoField, autoincrement
    #
    # user = models.IntegerField(  # TODO поле в этой таблице
    #     verbose_name="user",
    #     default=0,
    #     editable=True,
    #     blank=True
    # )
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        unique=True,
        db_index=True,

        max_length=150  # TODO свойство(параметр) этого поля
    )

    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True,

        max_length=300  # TODO свойство(параметр) этого поля
    )

    class Meta:
        app_label = 'django_twitter_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        # db_table

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.id}]"