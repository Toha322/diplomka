from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Genre(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


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
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

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
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='genres'
    )
    tags = models.ManyToManyField(
        Tags,
        verbose_name='Tег',
        related_name='tags'
    )
    full_description = models.TextField(
        verbose_name='Полное описание',
        null=True,
        blank=True
    )

    short_description = models.TextField(
        verbose_name='Короткое Описание',
        null=True,
        blank=True
    )
    studio = models.ManyToManyField(
        Studio,
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
        verbose_name='Первоначальная цена'
    )
    default_price = models.PositiveIntegerField(
        verbose_name='Цена с учетом скидоса',
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

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'



class Comment(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра', related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    text = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пост-{self.game}: {self.author}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Like(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='likes')
    user = models.ManyToManyField(User, related_name='likes')


class Dislike(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='dislikes')
    user = models.ManyToManyField(User, related_name='dislikes')




class GameLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='game_library',
                             verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Библиотека пользователя: {self.user.username}'

    class Meta:
        verbose_name = 'Библиотека пользователя'
        verbose_name_plural = 'Библиотеки пользователей'
        ordering = ['-created_at']


class GameLibraryItem(models.Model):
    library = models.ForeignKey(GameLibrary, on_delete=models.CASCADE,
                                related_name='game_library_items', verbose_name='Библиотека')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    is_downloaded = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)  # при создании добавляется время
    updated_at = models.DateTimeField(auto_now=True)  # время меняется при изменении элемента

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = 'Игра в библиотеке'
        verbose_name_plural = 'Игры в библиотеке'
        ordering = ['-updated_at']




class WishLibrary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wish_library',
                             verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Библиотека пользователя: {self.user.username}'

    class Meta:
        verbose_name = 'Библиотека пользователя'
        verbose_name_plural = 'Библиотеки пользователей'
        ordering = ['-created_at']


class WishLibraryItem(models.Model):
    library = models.ForeignKey(WishLibrary, on_delete=models.CASCADE,
                                related_name='wish_library_items', verbose_name='Библиотека')
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    is_downloaded = models.BooleanField(default=False, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True)  # при создании добавляется время
    updated_at = models.DateTimeField(auto_now=True)  # время меняется при изменении элемента

    def __str__(self):
        return self.game.name

    class Meta:
        verbose_name = 'Игра в библиотеке'
        verbose_name_plural = 'Игры в библиотеке'
        ordering = ['-updated_at']