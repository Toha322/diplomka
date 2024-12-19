from django.db import models


class Genre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название жанра'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Tags(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название тега'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tег'
        verbose_name_plural = 'Tеги'


class Studio(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название компании'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Game(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name='Жанр',
        related_name='genres'
    )
    tags = models.ForeignKey(
        Tags,
        on_delete=models.CASCADE,
        verbose_name='Tег',
        related_name='tags'
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
    )
    studio = models.ForeignKey(
        Studio,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        related_name='studio'
    )
    preview = models.ImageField(
        verbose_name='Превью',
        upload_to='games/previews/',
        blank=True,
        null=True
    )
    current_price = models.PositiveIntegerField(
        verbose_name='Цена'
    )
    default_price = models.PositiveIntegerField(
        verbose_name='В процентах',
        null=True,
        blank=True,
    )
    added_at = models.DateTimeField(
        verbose_name='Дата добавления',
        auto_now_add=True
    )
    downloads = models.PositiveIntegerField(
        verbose_name='Кол-во скачиваний',
        default=0
    )
    size = models.FloatField(
        verbose_name='Размер',
        default=0.0
    )
